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

#Define a function to calculate the tree height

TreeHeight <- function(degrees, distance){ 
            radians <- (degrees * pi)/ 180
            Tree.Height <- distance * tan(radians)
}

#Main function to get the input data from command line argument

main <- function(){
  args <- commandArgs(trailingOnly = TRUE)
  filename <- args[1] 
  Data <- read.csv(file = filename) #read in a file
  Data$Tree.Height.m <- NA #create an empty column for the output
  Data[,4] <- TreeHeight(Data[,3], Data[,2]) # calculate the tree height
  output_file <- tools::file_path_sans_ext(basename(filename)) #get a file name with no extension
  output_path <- paste("../results/",output_file,"_treeheights.csv", sep = "") # create a new file path with new name
  write.csv(Data, output_path, row.names = FALSE) #write a csv file

}
 
main()  #call the main function
