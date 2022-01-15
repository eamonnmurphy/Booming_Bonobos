# Author: Booming Bonobos
# Script: get_TreeHeight.R
# Desc: calculates tree heights
# Date: Oct 2021

# This function calculates heights of trees given distance of each tree
# from its base and angle to its top, using the trigonometric formula
#
# height = distance * tan(radians)
#
# ARGUMENTS
# degrees: The angle of elevation of tree
# distance: The distance from base of tree (e.g., metres)
#
# OUTPUT
# The heights of the tree, same units as "distance"

# write function to calculate tree height
TreeHeight <- function(Angle.degrees, Distance.m){
    radians <- Angle.degrees * pi / 180
    height <- Distance.m * tan(radians)
    #print(paste("Tree height is:", height))

    return (height)
}


# Main function to get the input data from command line argument - used Chalita's cause was better than what I'd done

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
 
main()  # call the main function
