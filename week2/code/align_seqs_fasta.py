#!/usr/bin/env python3

''' This script is for aligning two dna sequences
from different files. If no input files are given,
it will use default inputs.'''

## imports ##
import csv
from os import kill
import sys

## functions ##

# Check inputs to check if we will use defaults
if len(sys.argv) == 3:
    # Read input files if there are 2
    with open()
else:
# Read input .csv files
    with open('../data/seq.csv','r') as f:
        csvread = csv.reader(f)
        for row in csvread:
            seq1 = row[0]
            seq2 = row[1]
    


# Assign the longer sequence s1, and the shorter to s2
# l1 is length of the longest, l2 that of the shortest

l1 = len(seq1)
l2 = len(seq2)
if l1 >= l2:
    s1 = seq1
    s2 = seq2
else:
    s1 = seq2
    s2 = seq1
    l1, l2 = l2, l1 # swap the two lengths

# A function that computes a score by returning the number of matches starting
# from arbitrary startpoint (chosen by user)
def calculate_score(s1, s2, l1, l2, startpoint):
    """ Calculate the score 
    """
    matched = "" # to hold string displaying alignements
    score = 0
    for i in range(l2):
        if (i + startpoint) < l1:
            if s1[i + startpoint] == s2[i]: # if the bases match
                matched = matched + "*"
                score = score + 1
            else:
                matched = matched + "-"

    # some formatted output
    print("." * startpoint + matched)           
    print("." * startpoint + s2)
    print(s1)
    print(score) 
    print(" ")

    return score

# Test the function with some example starting points:
# calculate_score(s1, s2, l1, l2, 0)
# calculate_score(s1, s2, l1, l2, 1)
# calculate_score(s1, s2, l1, l2, 5)

# now try to find the best match (highest score) for the two sequences
my_best_align = None
my_best_score = -1

for i in range(l1): # Note that you just take the last alignment with the highest score
    z = calculate_score(s1, s2, l1, l2, i)
    if z > my_best_score:
        my_best_align = "." * i + s2 # think about what this is doing!
        my_best_score = z 
print(my_best_align)
print(s1)
print("Best score:", my_best_score)

with open('../results/bestseq.txt', 'w') as f:
    f.write("Best score: " + str(my_best_score) +
    "\n" + my_best_align)


def main(argv):
    return 0

if __name__ == '__main__':
    '''Makes sure the 'main' function is called from command line'''
    status = main(sys.argv)
    sys.exit(status)
