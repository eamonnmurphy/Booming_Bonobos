#!/usr/bin/env python3

"""This script is for aligning the two DNA sequences"""

__appname__ = '[ALIGN SEQS]'
__author__ = 'Chalita Chomkatekaew chalita.chomkatekaew20@imperial.ac.uk'
__version__ = '0.0.1'

## import

import sys
import csv

# Two example sequences to match
#seq2 = "ATCGCCGGATTACGGG"
#seq1 = "CAATTCGGAT"

## import and prepare the sequences from arguments

print("Start the alignment!")

new_lst = [] #create a empty list to store the first input sequence in
new_lst2 = [] #create a empty list to store the second input sequence in

def ReadInput(x, y): 
    with open(x, 'r') as first_input: # read the first input sequence
        with open(y, 'r') as second_input: # read the second input sequence
            a = first_input.readlines()[1:] # skip the first line
            for i in a:
                new_lst.append(i.strip())
            b = second_input.readlines()[1:]
            for i in b:
                new_lst2.append(i.strip())

            

with open("../data/seq1.fasta", "r") as first_seq: # read default first sequence
    with open("../data/seq2.fasta", "r") as second_seq: # read default second sequence
        if len(sys.argv) <= 2: # if there is no input argument or only one argument
            print("Not enough input arguments, Running the alignment on default sequences")
            
            #seq1 is the default sequence which then skip the first line and remove '\n'
            seq1 = ''.join(first_seq.readlines()[1:]).replace('\n','') 
            
            #seq2 is the default sequence
            seq2 = ''.join(second_seq.readlines()[1:]).replace('\n','')
            
            #print the first 10 nucleotides/sequence
            print("First sequence: %s ... \n Second sequence: %s ..." % (seq1[0:11], seq2[0:11]) )
        else: # If there are 2 input arguments 
            print("Reading the input files")
            
            # print the name of the input files
            print("This is a first input sequence: %s \n This is a second input sequence: %s" % (str(sys.argv[1]), (str(sys.argv[2]))))
            
            ReadInput(sys.argv[1],sys.argv[2]) # run ReadInput function
            seq1 = ''.join(new_lst) # join the sequence together and store it in seq1
            seq2 = ''.join(new_lst2) 
            

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

## function
# A function that computes a score by returning the number of matches starting
# from arbitrary startpoint (chosen by user)
def calculate_score(s1, s2, l1, l2, startpoint): # it will run with the startpoint of 0 if not specify
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
    print("." * startpoint + matched) # "." * startpoint means how many time "*" is repeated based on the number of startpoint          
    print("." * startpoint + s2)
    print(s1)
    print(score) 
    print(" ")

    return score

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

def main(argv):
    return print(f"Done!")

if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)

