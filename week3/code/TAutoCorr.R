## This script is to test the correlation between the successive years of the
## annual temperature dataset from Key West, Florida, USA


# Author : Booming Bonobos
# Version : 0.0.1

#Load a required package(s)

require(ggplot2)

# Load the dataset
rm(list =ls())
load("../data/KeyWestAnnualMeanTemperature.RData")

#set the seed ...make sure the results same everytime it runs

set.seed(1)

#Observed the correlation between pairs of years

N <- ats[1:99, 2]
N_1 <- ats[2:100, 2] #select the successive years

ObsCor <- cor(N, N_1, method = c("spearman"))

#The number of observations in the given sample
n <- length(ats$Year)

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

#Perform a correlation coefficient test on each column of MatrixSamp between the
#successive years

for (i in 1:P){
  CorCoeff.test[i] <- cor(MatrixSamp[1:99,i], MatrixSamp[2:100,i],method = c("spearman"))
}

#Calculate the P-value
#N.B. The calculated P-value is only an estimated one.
#P-values is the probability of how many permutation test > the observed test stat
#and divide by the total number of permutation test

P_value <- mean(CorCoeff.test >= ObsCor)

paste("The correlation coefficient between the successive years is", round(ObsCor, digits = 3), "with the estimated P-value of", P_value)

#Visualise the permutation test

#Convert the permutation stat test from vector to a dataframe for plotting with
#ggplot

data <- as.data.frame(CorCoeff.test)

#Plot the data distribution

Florida <- ggplot(ats, aes(x = Year, y = Temp))+
  geom_point() +
  scale_x_continuous(breaks = seq(1900,2000, by = 10))+
  ylab("Temperature (Celsius)")+
  theme_bw() +
  theme(aspect.ratio = 1,
        panel.grid = element_blank())


#Plot the density graph of the permutation tests
CorPlot <- ggplot(data, aes(x=CorCoeff.test))+
  geom_density(stat = "density",
               position = "identity") +
  xlim(-0.6, 0.6)+
  geom_vline(xintercept = ObsCor, #Illustrate the observed Correlation coefficient
             colour = "blue", 
             linetype = "dashed")+
  annotate(geom = "text", x = 0.5, y = 3,
           label = "Observed cor = \n0.341\n P-value = \n0.00018",
           size = 3) +
  xlab("Correlation coefficient for successive years ") +
  ylab("Density") +
  theme_bw()+
  theme(aspect.ratio = 1,
        panel.grid = element_blank())

#Save the plot into a file

ggsave("../results/DistributionFlorida.png", plot = Florida ,
       width = 10, height = 10, units = "cm")

ggsave("../results/PermuCorCoeff_TAutoCorr.png", plot = CorPlot ,
       width = 10, height = 10, units = "cm")