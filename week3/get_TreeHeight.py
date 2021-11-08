# !/usr/bin/env python 3
'''This function calculates heights of trees given distance of each tree
from its base and angle to its top, using trigonometry

height = distance * tan(radians)

ARGUMENTS
degrees: The angle of elevation of tree
distance: The distance from base of tree (e.g., meters)

OUTPUT
The heights of the tree, same units as "distance"
'''

import math

# Load in tree data from csv

# Function to measure tree height given angle and distance
def TreeHeight(degrees, distance):
    radians = degrees * math.pi / 180
    height = distance * math.tan(radians)
    return height

# Example call
TreeHeight(37, 40)

# Create empty dataframe
TreeHts = []

# Add each necessary row iteratively to list
for row in len(TreesData):
    height = TreeHeight(TreesData[[row,2]], TreesData[[row,3]])
    new_row = [TreesData[[row,1]], TreesData[[row,2]],
        TreesData[[row,3]], height]
    TreeHts[len(TreeHts) + 1,] = new_row

# Write to csv