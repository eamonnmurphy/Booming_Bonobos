#!/usr/bin/env python3
"""Reads an input file of tree names and outputs the oaks to a csv.
Robust to slight typos and misspellings."""

__author__ = 'Eamonn Murphy (eamonn.murphy21@imperial.ac.uk)'
__version__ = '0.0.1'

import csv
import sys

#Define function
def is_an_oak(name):
    """ Returns True if name is starts with 'quercus'

    >>> is_an_oak('Quercus cirrus')
    True

    >>> is_an_oak('quercus cirrus')
    True

    >>> is_an_oak('Quercuss cirrus')
    False

    >>> is_an_oak(' Quercus cirrus')
    True

    >>> is_an_oak('Fagus sylvatica')
    False
    """

    return name.lower().strip().startswith('quercus ')

def main(argv):
    """Writes only the oak species to a new csv, from a file of tree species."""
    with open('../data/TestOaksData.csv','r') as f,\
            open('../data/JustOaksData.csv','w') as g:
        taxa = csv.reader(f)
        csvwrite = csv.writer(g)
        for row in taxa:
            if row[0].lower() == "genus":
                csvwrite.writerow(["Genus", " species"])
                continue
            print(row)
            print ("The genus is: ") 
            print(row[0] + '\n')
            if is_an_oak(" ".join(row)):
                print('FOUND AN OAK!\n')
                csvwrite.writerow([row[0], row[1]])    

    return 0
    
if (__name__ == "__main__"):
    import doctest
    doctest.testmod()
    status = main(sys.argv)
    sys.exit(status)