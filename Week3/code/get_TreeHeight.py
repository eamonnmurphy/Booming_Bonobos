#!/usr/bin/env python3

"""This script is for calculating the tree height. The script only needs one input file with, given
the second column is distance of each tree and the third column is angle of evaluation of the tree"""

__appname__ = '[get_TreeHeight]'
__author__ = 'Chalita Chomkatekaew chalita.chomkatekaew20@imperial.ac.uk'
__version__ = '0.0.1'

## import

import sys
import numpy as np
import pandas as pd
import os

##Define a function to calculate the tree height
# This function calculates heights of trees given distance of each tree
# from its base and angle to its top, using the trigonometric formula
#
# height = distance * tan(radians)
#
# ARGUMENTS
# degrees: The angle of elevation of tree
# distance: The distance from base of tree (e.g., metres)

def TreeHeight(degree, distance):
    radians = degree * np.pi / 180
    TreeHeight = distance * np.tan(radians)

    return TreeHeight

def main(argv):
    if len(sys.argv) > 2: #check if input file is more than one
        print("There are too many input files, please select one.")

    elif len(sys.argv) == 2: #If there is one input file

        print("Using the user input data %s " % (str(sys.argv[1])))

        Inputdata = pd.read_csv(sys.argv[1]) #Import the input file

        filename = os.path.basename(sys.argv[1]) #get the name of the file

        base = os.path.splitext(filename)[0] #get the basename of the file with no extension

        if len(Inputdata.columns) >= 3 and list(Inputdata.columns).index('Distance.m') == 1 and list(Inputdata.columns).index('Angle.degrees') == 2:
            #Check if the input file has at least 3 columns with the right format

            print("Correct the data format")

            data = Inputdata

            data['Tree.Height.m'] = data.apply(lambda x: TreeHeight(x['Angle.degrees'], x['Distance.m']), axis = 1)
            #Apply the tree height calculator function with the appropriate columns
            
            newfile = f"../results/{base}_treeheights.csv" #Create a new filename and path
            
            data.to_csv(newfile,index=False) #write a csv file

            print("Done!")
        else: #If data is not in the right format, print this
            print("Not enough data to calculate the tree height. Please check the file")

    else: #If run the script by itself - use the default data
        print("Running the script with the default data")
        
        data = pd.read_csv('../data/trees.csv')
        
        data['Tree.Height.m'] = data.apply(lambda x: TreeHeight(x['Angle.degrees'], x['Distance.m']), axis = 1)
        
        data.to_csv('../results/tree_results.csv',index=False)

    return None

if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)










