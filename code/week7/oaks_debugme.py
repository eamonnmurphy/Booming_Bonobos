#!/user/bin/env python3
# Author: Uva Fung uf21@imperial.ac.uk
# Script: oaks_debugme.py
# Desc: runs a function that searches and returns oak species, with doctests for unit testing
# Date: Nov 16 2021

"""This script runs the is_an_oak function that finds and returns oak species"""

__author__ = 'Uva Fung uf21@imperial.ac.uk'
__version__ = '0.0.1'


import csv
import sys
import doctest # import doctest module

#Define function
def is_an_oak(name):
    """Find whether a species belongs to the Quercus genus
    
    >>> is_an_oak('Quercus robur')
    True

    >>> is_an_oak('Fraxinus excelsior')
    False

    >>> is_an_oak('Pinus sylvestris')
    False

    >>> is_an_oak('Quercus cerris')
    True

    >>> is_an_oak('Quercus petraea')
    True

    >>> is_an_oak('Quercus ')
    True

    >>> is_an_oak('Quercus abcsdecd')
    True

    >>> is_an_oak('Quercusabscd robur')
    False

    >>> is_an_oak('Quercas ')
    False

    >>> is_an_oak('Quercusss')
    False

    >>> is_an_oak('Happyquercusss')
    False

    
    """
    
    # define function to be tested
    return name.lower().startswith('quercus ')

def main(argv): 
    
    """print the genus of each species and save the oak species in a new csv output file"""

    f = open('../data/TestOaksData.csv','r')
    g = open('../results/JustOaksData.csv','w') # write the output in a new csv file
    taxa = list(csv.reader(f)) # read TestOaksData.csv as a list so that it can be used in indexing
    csvwrite = csv.writer(g)
    oaks = set()

    for row in taxa[1:]: # skip the first row as row 0 is a header
        print(row)
        print ("The genus is: ") 
        print(row[0] + '\n')
        if is_an_oak(row[0] + " "): # space added so that only "Quercus" genus would return true
            print('FOUND AN OAK!\n')
            csvwrite.writerow([row[0], row[1]])  
        else: 
            print('No oak found. If you believe it is an oak, check for spelling mistakes. The genus name of oak is spelled as Quercus.\n')  

    return 0
    
if (__name__ == "__main__"):
    status = main(sys.argv)

doctest.testmod()

