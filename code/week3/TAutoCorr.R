## This script tests the correlation between the successive years of the annual temperature dataset from Key West, Florida, USA


# Author : Uva Fung u.fung21@imperial.ac.uk
# Version : 0.0.1
rm(list =ls())

require(ggplot2)
load("../data/KeyWestAnnualMeanTemperature.RData")

set.seed(100)


# Compute the appropriate correlation coefficient between years
shift_temp <- ats[2:100,2]
base_cor <- cor(ats[1:99,2], shift_temp)

# Repeat this calculation 10000 times by randomly permuting the
# time series, and then recalculating correlation for each year
# sequence (use sample function)
# test_sample <- sample(ats$Year, nrow(ats))

random_year_order <- function(){
  random_order <- sample(ats$Temp, nrow(ats))
  new_cor <- cor(random_order[1:99], random_order[2:100])
  return(new_cor)
}

cor_vec <- c()

for(i in 1:10000){
  cor_vec <- append(cor_vec, random_year_order())
}

#cor_vec <- replicate(10000, random_year_order())

# Calculate what fraction of the correlation coefficients
# were greater than those of step 1 (approximate p-value)

num <- sum(cor_vec > base_cor)
p_value <- num/10000

# Create images for Latex file
p <- ggplot(data = ats, aes(Year, Temp)) + geom_point() +
  labs(y = "Temperature (C)") +
  geom_smooth(method = "lm", se = TRUE, fullrange = TRUE)


png("../results/temp_year_scatter.png")
print(p)
dev.off()


png("../results/coeff_distri.png")
hist(cor_vec, main = NULL, xlab = "Correlation coefficients")
abline(v = base_cor, col = "red")
dev.off()