# !/usr/bin/env Rscript
# This function calculates heights of trees given distance of each tree
# from its base and angle to its top, using trigonometry
#
# height = distance * tan(radians)
# 
# ARGUMENTS
# degrees: The angle of elevation of tree
# distance: The distance from base of tree (e.g., meters)
# 
# OUTPUT
# The heights of the tree, same units as "distance"

# Load in tree data from csv

arg <- commandArgs(trailingOnly = TRUE)
stringsAsFactors = FALSE
TreesData <- read.csv(arg, stringsAsFactors=FALSE)

# Function to measure tree height given angle and distance
TreeHeight <- function(degrees, distance){
  radians <- degrees * pi / 180
  height <- distance * tan(radians)
  #print(paste('Tree height is:', height))
  return(height)
}

# Example call
TreeHeight(37, 40)

# Create empty dataframe
TreeHts <- data.frame(Species=numeric(), Distance.m=numeric(),
                      Angle.degrees=numeric(),Tree.Height.m=numeric())

# Add each necessary row iteratively to the dataframe
for (row in 1:nrow(TreesData)){
  # Calculate height for this tree
  height <- TreeHeight(TreesData[[row,2]],TreesData[[row,3]])
  new_row <- c(TreesData[[row,1]],TreesData[[row,2]],TreesData[[row,3]],height)
  TreeHts[nrow(TreeHts) + 1,] = new_row
}

# Transform columns to numeric data type
TreeHts <- transform(TreeHts, Distance.m = as.numeric(Distance.m),
                     Angle.degrees = as.numeric(Angle.degrees),
                     Tree.Height.m = as.numeric(Tree.Height.m))

# Write dataframe to csv
stripped <- tools::file_path_sans_ext(basename(arg))
write.csv(TreeHts, paste("../results/", stripped, "_treeheights.csv", sep = ""),
          row.names=FALSE)