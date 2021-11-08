###############
# Write regression results to csv
# Analysis must be subsetted by Predator.lifestage and location
# 
# Calculate regression results 
# and save to csv delimited table in results directory
# (Init new dataframe and then write.csv() or write.table())
# 
# Linear regression on subsets of the data corresponding to
# Feeding Type x Predator Life stage x Location combination
# 
# Regression results should include: regression slope, regression
# intercept, R**2, F-statistic, p-value
# 
# Use dplyr and ggplot

require(dplyr)
require(tidyverse)
require(ggplot2)
require(broom)

rm(list = ls())

# Read data and look at feeding interaction data
MyDF <- read.csv("../data/EcolArchives-E089-51-D1.csv")
altered_df <- MyDF %>% subset(select = 
                                c(Predator.mass, Prey.mass, 
                                  Type.of.feeding.interaction, 
                                  Predator.lifestage, Location))
altered_df$Type.of.feeding.interaction <- factor(altered_df$Type.of.feeding.interaction)
altered_df$Predator.lifestage <- factor(altered_df$Predator.lifestage)
altered_df$Location <- factor(altered_df$Location)

# First, seperate data by feeding interaction.
# Then, colour data points by predator lifestage

# Calculate regression results
regr_df <- data.frame(matrix(ncol = 5, nrow = 0))
names <- c("slope", "intercept", "r_squared", "F_stat", "p_value")
colnames(regr_df) <- names
rows <- c()

for (type in unique(altered_df$Type.of.feeding.interaction)) {
  # browser()
  for (stage in unique(altered_df$Predator.lifestage)) {
    for (place in unique(altered_df$Location)) {
        quick_df <- altered_df %>% filter(
          Predator.lifestage == stage, Type.of.feeding.interaction == type,
          Location == place
        )
        if (all(is.na(quick_df$Predator.mass))) {
          next
        }
        else if (all(is.na(quick_df$Predator.mass))) {
          next
        }
        else {
          name <- paste(type, stage, place, sep = ".")
          append(rows, name)
          new_lm <- lm(Predator.mass ~ Prey.mass, data = quick_df)
          summary <- summary(new_lm)
          # print(summary)
          # print(summary$fstatistic)
          tidied <- tidy(new_lm)
          # print(tidied)
          glanced <- glance(new_lm)
          # print(glanced)
          try(regr_df[nrow(regr_df)+1,] <- c(
             tidied[2,2], tidied[1,2], glanced[1,1], summary$fstatistic[1],
             pf(summary$fstatistic[1], summary$fstatistic[2], summary$fstatistic[3],
                lower.tail = FALSE)
           ))
          row.names(regr_df)[nrow(regr_df)] <- name
        }
    }
  }
}

write.csv(regr_df, "../results/PP_Regress_loc_Results.csv")

