#usr/bin/env python3

#!/usr/bin/env python3

"""This script loads in data and searches for oaks in it"""

__appname__ = '[OAKS DEBUGME]'
__author__ = 'Booming bonobos'
__version__ = '0.0.1'


import csv
import sys
import doctest
from difflib import SequenceMatcher

# NOTE: I am taking the instruction of making this script able to 'handle cases where there is a typo etc' to mean: allow for leeway to include names which could be oaks but just have a typo in them

#Define function
def is_an_oak(name):
    """ Returns a measure of how similar a name is to 'Quercus' (i.e. how close it is to being an oak)

    >>> is_an_oak('Quercus')
    1.0

     >>> is_an_oak('Fraxinus')
     0.4

    whenever there is a typo, returns a value close enough to 1.0
    >>> is_an_oak('QQuercus')
    0.9333333333333333
    >>> is_an_oak('Quercuss')
    0.9333333333333333
    >>> is_an_oak('Quercyuss')
    0.875

    Let's define 'close enough' as being up to three typos:
    >>> is_an_oak('uwercuss')
    0.8

    """
    return SequenceMatcher(None, name.lower(), "quercus").ratio() # returns the similarity of the input name to 'quercus' as a ratio (.lower makes it all lower-case to standardize comparisons)


def main(argv):
    """Open the input data from TestOaksData.csv and write the outputs (= only the species which have names close enough to being oaks) to JustOaksData.csv"""
    f = open('../data/TestOaksData.csv','r') # this csv contains 5 oak species names laid out in 2 columns (genus & species)
    # exclude the header row if it exists:
    if f.readline(1).lower() == "genus":
        f_lines = f.readlines()[1:] # if there is a header row, start reading from the second line
    else:
        f_lines = f.readlines()[0:] # if there is not a header row, start reading from the first line
    g = open('../data/JustOaksData.csv','w') # this csv is empty
    taxa = csv.reader(f_lines)
    csvwrite = csv.writer(g)
    oaks = set()
    for row in taxa:
        print(row)
        print ("The genus is: ") 
        print(row[0] + '\n')
        if is_an_oak(row[0]) == 1.0: # if it's got the exact name 'Quercus'
            print('FOUND AN OAK!\n')
            csvwrite.writerow([row[0], row[1]])
        elif is_an_oak(row[0]) >= 0.8: # if it's 'close enough' to being an oak (defined here as having a similarity of 0.8)
            print('Close enough to being an oak - but check for typos') # that way it flags the uncertainty and you can manually check these
    f.close() # need to close the csvs after opening them
    g.close()
    return 0
    
if (__name__ == "__main__"):
    status = main(sys.argv)

doctest.testmod() # to run with embedded tests
