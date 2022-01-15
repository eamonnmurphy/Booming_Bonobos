#!/usr/bin/python 

""" This script that calculates tree height from a given csv file """

__author__ = 'Booming Bonobos (github.com/eamonnmurphy/Booming_Bonobos)'
__version__ = '0.0.1'

####################################################################################
### PACKAGES
import sys
import os
import math 
import pandas as pd

####################################################################################
### FUNCTION THAT CALCULATES TREE HEIGHTS

def TreeHeight(degrees, distance):
    """ Function that calculates tree height """
    radians = degrees * math.pi / 180 # Converts degrees entered by user to radians
    height = distance * math.tan(radians) # Calculates height = distance * tan(angle in radians)
    return height

####################################################################################

#### Load the tree data
arg = sys.argv[1] # get file that is argued
treedata = pd.read_csv(arg) # read file

#### unpack columns from panda data frames into lists
angles = [i for i in treedata.loc[:,"Angle.degrees"]]
distance = [i for i in treedata.loc[:,"Distance.m"]]

#### run function on lists, add results to a list called height
height = []
for x in range(len(angles)):
    height.append(TreeHeight(angles[x], distance[x]))

#### merge height list with the data frame:
# make height list into a data frame
hcolumn = pd.DataFrame(height, columns = ['Height.m'])
# make temporary columns to make merging easier
treedata['tmp'] = 1
hcolumn['tmp'] = 1
# merge original tree data and height column
treedata = pd.merge(treedata, hcolumn, on=['tmp'])
# remove temporary column from final output
treedata = treedata.drop('tmp', axis=1)

#### output csv file
arg = arg.split("/")[2] # remove path to help make output file name
arg = arg.split(".")[0] # remove .csv to help make output file name
outputfilename = ("../results/" + str(arg) + "_treeheights.csv") # create output file name
pd.DataFrame.to_csv(treedata, outputfilename) # save tree data to output file
