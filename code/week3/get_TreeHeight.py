#!/user/bin/env python3
# Author: Uva Fung uf21@imperial.ac.uk
# Script: get_TreeHeight.py
# Desc: calculate tree height -- groupwork
# Date: Jan 6 2022

"""This script is for calculating the tree height. The script only needs one input file, with
the second column storing distance of each tree and the third column storing angle of evaluation of the tree"""

__appname__ = 'get_TreeHeight'
__author__ = 'Uva Fung u.fung21@imperial.ac.uk'
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
    """ Calculates the tree height from degree and distance """
    radians = degree * np.pi / 180
    TreeHeight = distance * np.tan(radians)

    return TreeHeight


def main(argv):
    """ Check the format of the input file and calculates tree height when input file is correct. """
    if len(sys.argv) > 2: #check if input file is more than one
        print("Too many input files, please only input one.")

    elif len(sys.argv) == 2: #If there is one input file

        print("Using the user input data %s " % (str(sys.argv[1])))

        Inputdata = pd.read_csv(sys.argv[1]) #Import the input file

        filename = os.path.basename(sys.argv[1]) #get the name of the file

        base = os.path.splitext(filename)[0] #get the basename of the file with no extension

        if len(Inputdata.columns) >= 3 and list(Inputdata.columns).index('Distance.m') == 1 and list(Inputdata.columns).index('Angle.degrees') == 2:
            #Check if the input file has at least 3 columns with the right format

            print("Correct data format. Proceed to tree height calculatiion.")

            data = Inputdata

            data['Tree.Height.m'] = data.apply(lambda x: TreeHeight(x['Angle.degrees'], x['Distance.m']), axis = 1)
            #Apply the tree height calculator function with the appropriate columns
            
            newfile = f"../results/{base}_treeheights.csv" #Create a new filename and path
            
            data.to_csv(newfile,index=False) #write a csv file

            print("Done!")
        else: #If data is not in the right format, print this
            print("The data file is not in the correct format. Please ensure the file has at least three columns with distance and degree stored in the second and third column respectively. ")

    else: #If run the script by itself - use the default data
        print("Running the script using default data. ")
        
        data = pd.read_csv('../data/trees.csv')
        
        data['Tree.Height.m'] = data.apply(lambda x: TreeHeight(x['Angle.degrees'], x['Distance.m']), axis = 1)
        
        data.to_csv('../results/tree_results.csv',index=False)

        print("Done!")

    return None

if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)


