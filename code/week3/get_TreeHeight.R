# Author: Uva Fung
# Date: Jan 6 2022
# Description: Group practical -- This function calculates height of trees given distance of each tree
# from its base and angle to its top, using the trigonometric formula

# height = distance * tan(radians)

# ARGUMENTS
# degrees: the angle of elevation of tree
# distance: the distance from base of tree (eg. meters)

#OUTPUT
# the height of the tree, same units as "distance"

rm=(list=ls())

# Function to calculate tree height
TreeHeight <- function(degrees, distance){
    radians <- degrees * pi / 180
    height <- distance * tan(radians)
    print(height)
    return(height)
}

#Main function to get the input data from command line argument

main <- function(){
  args <- commandArgs(trailingOnly = TRUE)
  filename <- args[1] 
  Data <- read.csv(file = filename) #read in a file
  Data$Tree.Height.m <- NA #create an empty column for the output
  Data[,4] <- TreeHeight(Data[,2], Data[,3]) # calculate the tree height
  output_file <- tools::file_path_sans_ext(basename(filename)) #get a file name with no extension
  output_path <- paste("../results/",output_file,"_treeheights.csv", sep = "") # create a new file path with new name
  write.csv(Data, output_path, row.names = FALSE) #write a csv file
  
}

main()

print("Script completes!")   # print when run with source() to show that script is working

