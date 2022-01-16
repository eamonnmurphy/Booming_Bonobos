############################# LOADING AND SUBSETTING THE DATA ###############################

##### Load the data
load("../data/KeyWestAnnualMeanTemperature.RData") # loads as "ats"

##### Subset the data
ats_y1 <- ats[-c(100),] # years 1901 - 1999
ats_y2 <- ats[-c(1),] # years 1902 - 2000

################ RANDOMLY SHUFFLING DATA & GETTING COEFFICIENTS #############################

##### Create empty vector
correlationshuffle <- vector()

##### Shuffle data randomly and get correlation coefficients, put results in empty vector
for (x in 1:1000){
    tempshuffle <- sample(ats_y1$Temp, 99, replace=FALSE)
    correlationshuffle <- c(correlationshuffle, cor(ats_y2$Temp, tempshuffle))
} # creates normal distr. of different possible correlation coefficients

############################## STATISTICS ####################################################

##### Coefficient for the original data
correlation <- cor(ats_y1$Temp, ats_y2$Temp)
print(correlation)
# 0.3261697

##### Comparison of coefficient for original data to coefficients from shuffled data
result <- pnorm(correlation, mean=mean(correlationshuffle), sd=sd(correlationshuffle))
print(result)
# 0.9992149

############################ PLOTTING THE DATA ###############################################

##### Present results in a histogram
pdf("../results/TAutoCorr_figure.pdf")
hist(correlationshuffle, xlim = c(-0.6, 0.6), xlab = "Correlation Coefficient", 
     col = "lightblue", main = "Distribution of Correlation Coefficients from Shuffled Samples")
abline(v = correlation, col = "red")
text(0.425, 150, col = "red", labels = paste0("Observed \n Correlation: \n", round(correlation, digits = 5)))

##### Plot of original Florida data
pdf("../results/Florida_original.pdf")
plot(ats, main = "Change in Temperature over time in Florida")

