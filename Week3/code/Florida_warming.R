## This script is to test the correlation between the temperature in Florida and
## year 1901 and 2000

# Author : Chalita Chomkatekaew (chalita.chomkatekaew@ic.ac.uk)
# Version : 0.0.1

#Load a required package(s)

require(ggplot2)

# Load the dataset
rm(list =ls())
load("../data/KeyWestAnnualMeanTemperature.RData")

#Observed the correration coefficient of the dataset

CorCoeff <- cor(ats$Year, ats$Temp, method = c("spearman"))

#The number of observations in the given sample
n <- length(ats$Temp)

#The number of permutation samples test to take

P <- 100000

#The variable we will resample from

variable <- ats$Temp

#Martrix to store the permutation data

MatrixSamp <- matrix(0, nrow = n, ncol = P)

#Create a permutation sample and store in each column of the matrix
for (i in 1:P){
  MatrixSamp[,i] <- sample(variable, size = n, replace=FALSE)
}

#Create an empty vector for storing the calculated correlation coefficient tests
#in each permutation

CorCoeff.test <- rep(0, P)

#Perform a correlation coefficient test on each column of MatrixSamp while the
#ats$Year remains in the same order

for (i in 1:P){
  CorCoeff.test[i] <- cor(ats$Year, MatrixSamp[,i],method = c("spearman"))
}

#Calculate the P-value
#N.B. The calculated P-value is only an estimated one.
#P-values is the probability of how many permutation test > the observed test stat
#and divide by the total number of permutation test

P_value <- mean(CorCoeff.test >= CorCoeff)

#Visualise the permutation test

#Convert the permutation stat test from vector to a dataframe for plotting with
#ggplot

data <- as.data.frame(CorCoeff.test)

#Plot the data distribution

Florida <- ggplot(ats, aes(x = Year, y = Temp))+
  geom_point() +
  ylab("Temperature")+
  ggtitle("Temperature in Florida from 1901 to 2000") +
  theme_bw()


#Plot the density graph of the permutation tests
CorPlot <- ggplot(data, aes(x=CorCoeff.test))+
  geom_density(stat = "density",
               position = "identity") +
  xlim(-0.6, 0.6)+
  geom_vline(xintercept = CorCoeff, #Illustrate the observed Correlation coefficient
             colour = "red", 
             linetype = "dashed")+
  annotate(geom = "text", x = 0.38, y = 3,size = 2,
           label = "Observed cor = 0.53") +
  xlab("Permutation test of correlation coefficient between Florida temp/year ") +
  ylab("Frequency") +
  theme_bw()+
  theme(aspect.ratio = 1)

#Save the plot into a file

ggsave("../results/DistributionFlorida.pdf", plot = Florida ,
       width = 14.8, height = 10.5, units = "cm")

ggsave("../results/PermuCorCoeff_Florida.pdf", plot = CorPlot ,
       width = 14.8, height = 10.5, units = "cm")

 