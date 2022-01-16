# Author: Booming Bonobos
# Script: PP_Regress_loc.R
# Desc: regression practical
# Date: Jan 2022

require(plyr)

# load the data
mydata <- read.csv("../data/EcolArchives-E089-51-D1.csv")


# store linear regressions for each feeding interaction, location and predator lifestage in model 1
lmfunction <- function(mydata){
  summary(lm(Prey.mass ~ Predator.mass, data = mydata))
}
model1 <- dlply(mydata, as.quoted(.(Type.of.feeding.interaction, Predator.lifestage, Location)), lmfunction)


# gets separate stats out of model1
listfunction <- function(m){ 
  slope <- m$coefficients[2]
  intercept <- m$coefficients[1]
  r2 <- m$r.squared
  pvalue <- m$coefficients[8]
  data.frame(slope, intercept, r2, pvalue)
}
output <- ldply(model1, listfunction)


# get f-stat separately bc it's different:
listfunction2 <- function(m){
  fstat <- m$fstatistic[1]
  data.frame(fstat)
}
output2 <- ldply(model1, listfunction2)


# make merged dataframe with all the stats
finaloutput <- merge(output, output2)


# write a csv file
write.csv(finaloutput, "../results/PP_Regress_loc_Results.csv", row.names = FALSE) # gets rid of row names 1, 2, 3
