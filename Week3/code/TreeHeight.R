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

TreeData <- read.csv("../data/trees.csv")

Tree.degrees <- TreeData$Angle.degrees
Tree.distance <- TreeData$Distance.m

#To create empty vector

results <- rep(NA, length(Tree.degrees))

TreeHeight <- function(degrees, distance){ 
            radians <- degrees * pi/ 180
            Tree.Height <- distance * tan(radians)
            print(Tree.Height)
        }
   
TreeData$Tree.Height.m <- TreeHeight(Tree.degrees, Tree.distance)
write.csv(TreeData, "../results/TreeHts.csv")
