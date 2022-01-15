# Regression analyses groupwork practical 
# Author: Uva Fung u.fung21@imperial.ac.uk
# Date: Jan 6 2022

rm(list=ls())

MyDF <- read.csv("../data/EcolArchives-E089-51-D1.csv")

install.packages("tidyverse")
require(ggplot2)
require(plyr)
require(dplyr)
require(tidyr)
require(broom)
require(purrr)


### Set variables as factors
MyDF$Predator.lifestage <- as.factor(MyDF$Predator.lifestage)
MyDF$Type.of.feeding.interaction <- as.factor(MyDF$Type.of.feeding.interaction)
MyDF$Location <- as.factor(MyDF$Location)

### Convert the Prey mass in mg to g and store in a new column

MyDF <- MyDF %>% mutate(Prey.mass = case_when(Prey.mass.unit == "mg" ~ Prey.mass/1000,
                                              Prey.mass.unit == "g" ~ Prey.mass)) %>%
  mutate(New.Prey.mass.unit = case_when(Prey.mass.unit == "mg" ~ "g",
                                        Prey.mass.unit == "g" ~ "g")) %>%
  select(-c('Prey.mass.unit'))


### Calculate linear regression for every combination of the Predator life-stages, the feeding types and locations.

# Calculation done using the group_by (dplyr) and tidy (broom) functions to summarise the results of every combination
# This will give the results with slope, intercept, and their corresponding t-value and P.value

linear <- MyDF %>%
  group_by(Predator.lifestage, Type.of.feeding.interaction, Location) %>%
  do(tidy(lm(log(Predator.mass) ~ log(Prey.mass), data = .))) %>%
  pivot_wider(names_from = term, values_from = c("estimate", "std.error", "statistic", "p.value")) %>% #Transform the data into a wide format for merging
  select(., 1:5) #select only columns with lifestage, feeding types, slope and intercept

overall_stats <- MyDF %>%
  group_by(Predator.lifestage, Type.of.feeding.interaction, Location) %>%
  do(glance(lm(log(Predator.mass) ~ log(Prey.mass), data = .))) %>% #glance function summaries the overall model of each combination as tibble
  select(., c("Predator.lifestage","Type.of.feeding.interaction", "Location", 
              "r.squared","statistic", "p.value")) #select the following columns


### Join the two dataframes together based on the predator lifestage and feeding types
stats_linear_Regress <- left_join(linear, overall_stats, 
                                  by = c("Predator.lifestage","Type.of.feeding.interaction", "Location"))

### Rename the columns to the appropriate column names
colnames(stats_linear_Regress) <- c("Predator.lifestage","Type.of.feeding.interaction","Location",
                                    "Intercept", "Slope",
                                    "R.squared","F-statistic",
                                    "P.value")

### print output ###
write.csv(Regress_results, "../results/PP_Regress_loc_Results.csv") # save as new file in results folder