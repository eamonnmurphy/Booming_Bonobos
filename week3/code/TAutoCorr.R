## Autocorrelation in Weather practical
## Are temperatures of one year correlated with the next year?
## Calculate the correlation between n-1 pairs of years (n is total years)
## Values are not independent (so no standard correlation p-value)
## 

# Load in temperature for Key West for the 20th century
rm(list = ls())
set.seed(12345)
library(ggplot2)
load('../data/KeyWestAnnualMeanTemperature.RData')

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


png("../results/coeff_distro.png")
hist(cor_vec, main = NULL, xlab = "Correlation coefficients")
dev.off()