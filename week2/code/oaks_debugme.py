#!/usr/bin/env python3

""" Finds oaks from a list of species. """
__author__= "Emma (emma.macdonald21@imperial.ac.uk)"
__version__= "0.0.1"

################################################# Imports
import csv
import sys

##########################################################
# function to see if it is an oak
def is_an_oak(name):
    """ Function returns True if name starts with 'quercus' """
    return name.lower().startswith('quercus') ## if this is true, it will return true

# function that checks for a header
def has_header(file):
    """ Function to check if a given file has a header.  """
    with open(file, 'r') as csvfile:
        sniffer = csv.Sniffer()
        return sniffer.has_header(csvfile.read())

### Main Function to run the script
def main(argv):
    """ Main function """

    # opens the files for reading and writing
    f = open('../data/TestOaksData.csv','r')
    g = open('../data/JustOaksData.csv','w')
    taxa = csv.reader(f)
    csvwrite = csv.writer(g)

    # write header
    csvwrite.writerow(["Genus", "species"])

    for row in taxa:
    # print results
        print(row)
        print ("The genus is: ") 
        print(row[0] + '\n')

        ## if function 1 returns true when it finds an oak, it will "print found an oak!" and write it to JustOaksData.csv
        if is_an_oak(row[0]):
            print('FOUND AN OAK!\n')
            csvwrite.writerow([row[0], row[1]])

if (__name__ == "__main__"):
    status = main(sys.argv)