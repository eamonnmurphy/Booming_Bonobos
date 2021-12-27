#!/usr/bin/env Rscript

#####################################################################################
### FUNCTION THAT CALCULATES TREE HEIGHTS

TreeHeight <- function(degrees, distance){
  radians <- degrees * pi / 180  # Converts degrees entered by user to radians
  height <- distance * tan(radians) # Calculates height = distance * tan(radians)
  
  return (height)
}

####################################################################################
### LOADING TREE DATA
args <- commandArgs(trailingOnly=TRUE) # get command line argument
treedata <-read.csv(args, header=TRUE) # load data


#### RUNNING FUNCTION
treedata$Tree.Height.m <- TreeHeight(treedata$Angle.degrees, treedata$Distance.m)

### OUTPUT CSV FILE
args2 <- tools::file_path_sans_ext(basename(args)) # removes .csv extension and the path from filename
outpufilename <- paste0("../results/", args2, "_treeheights.csv") # creates output file name
write.csv(treedata, outpufilename)

####################################################################################