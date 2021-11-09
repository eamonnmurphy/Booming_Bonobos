#Visualising Regression analyses practical

#Author: Chalita Chomkatekaew (chalita.chomkatekaew20@ic.ac.uk)
#version: 0.0.1

#Clean everything
rm(list = ls())

#Load a required package

require(ggplot2)
require(tidyverse)
require(broom)

#load dataset

MyDF <- read.csv("../data/EcolArchives-E089-51-D1.csv")

#check the dataset
str(MyDF)

#Set the variables to act as a factor i.e categorical
MyDF$Predator.lifestage <- as.factor(MyDF$Predator.lifestage)
MyDF$Type.of.feeding.interaction <- as.factor(MyDF$Type.of.feeding.interaction)

#Convert the Prey mass in mg to g and create a new prey mass unit column instead

MyDF <- MyDF %>% mutate(Prey.mass = case_when(Prey.mass.unit == "mg" ~ Prey.mass/1000,
                                              Prey.mass.unit == "g" ~ Prey.mass)) %>%
  mutate(New.Prey.mass.unit = case_when(Prey.mass.unit == "mg" ~ "g",
                                        Prey.mass.unit == "g" ~ "g")) %>%
  select(-c('Prey.mass.unit'))


#The relationship between the prey and predator mass in different Predator life styles Linear model regression

#Calculate the linear regression for every combination of the Predator lifestage and the feeding types

#Calculation done using the group_by (dplyr) and tidy (broom) functions to summarise the results of every combination
#This will give the results with slope, intercept, and their corresponding t-value and P.value

linear <- MyDF %>%
  group_by(Predator.lifestage, Type.of.feeding.interaction) %>%
  do(tidy(lm(log(Predator.mass) ~ log(Prey.mass), data = .))) %>%
  #Transform the data into a wide format so easier to merge with the overall stats dataframe
  pivot_wider(names_from = term, values_from = c("estimate", "std.error", "statistic", "p.value")) %>%
  #select only columns with lifestage, feeding types, slope and intercept
  select(., 1:4)

#glance function will allow the overall model of each combination to be summarise in a tibble table

overall_stats <- MyDF %>%
  group_by(Predator.lifestage, Type.of.feeding.interaction) %>%
  do(glance(lm(log(Predator.mass) ~ log(Prey.mass), data = .))) %>%
  #select the following columns
  select(., c("Predator.lifestage","Type.of.feeding.interaction", "r.squared","statistic", "p.value"))

#Join the 2 dataframes together based on the predator lifestage and feeding types
stats_linear_Regress <- left_join(linear, overall_stats, by = c("Predator.lifestage","Type.of.feeding.interaction"))

#Rename the columns to the appropriate column names
colnames(stats_linear_Regress) <- c("Predator.lifestage","Type.of.feeding.interaction",
                    "Intercept", "Slope",
                    "R.squared","F-statistic",
                    "P.value")
  
#Export the calculated statistics of the linear regression into the a csv file in results directory
write.csv(stats_linear_Regress, "../results/PP_Regress_results.csv", row.names = FALSE)


#Visualised the models
P_Regress <- ggplot(data = MyDF, aes(x = Prey.mass, y = Predator.mass,
                        colour = Predator.lifestage)) +
  geom_point(shape = I(3)) + #scatterplot with point in shape +
  geom_smooth(method = "lm", fullrange = TRUE) + # apply linear model which
  #extend beyond available data
  scale_y_continuous(trans = 'log10', # log10 as scale
                     labels = function(x) format(x, scientific = TRUE))+ 
  #scientific notation for labeling
  scale_x_continuous(trans = 'log10',
                     labels = function(x) format(x, scientific = TRUE))+
  facet_grid(Type.of.feeding.interaction ~.) + #illustrate the regression between
  #each predator lifestyle
  theme_bw() +
  theme(legend.position = "bottom") +
  guides(colour = guide_legend(nrow = 1)) + # make sure the the legend is in one row
  xlab("Prey mass in grams") + # change the x axis label
  ylab("Predator mass in grams") + # change the y axis label
  theme(aspect.ratio = 0.5) # resize the plot illustrated


# save the plot to the result directory

ggsave("../results/PP_Regress_plot.pdf", plot = P_Regress ,
       width = 21.0, height = 29.7, units = "cm")

