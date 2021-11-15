#!/usr/bin/env python3

"""This script aligns two DNA sequences such that they are as similar as possible"""
__author__ = 'Booming bonobos'

import sys

# Two example sequences to match
#seq2 = "ATCGCCGGATTACGGG"
#seq1 = "CAATTCGGAT"

# import and prepare input sequences

def ReadInput(x):
    """Read the sequences in the inputs provided and merge them into a string"""
    with open(x, "r") as fileinput:
        temp = fileinput.readlines()[1:] #skip the first line
        temp1 = [i.strip() for i in temp] #remove the new line characters
        seq_input = ''.join(temp1) #merge the sequences into one string
    return seq_input

def main(argv):
    if len(sys.argv) <= 2 : # if there is no input argument or only one argument

        print("Not enough input arguments, Running the alignment on default sequences")
        
        #Read input from default files and define seq1 and seq2
        seq1 = ReadInput("../data/seq1.fasta")
        seq2 = ReadInput("../data/seq2.fasta")

        #print the first 10 nucleotides/sequence
        print("The first sequence is: %s ... \n The second sequence is: %s ..." % (seq1[0:11], seq2[0:11]) )

    else: # If there are 2 input arguments 
        print("Reading the input files....")
            
        # print the name of the input files
        print("This first input sequence is: %s \n This second input sequence is: %s" % (str(sys.argv[1]), (str(sys.argv[2]))))

        #Read input files and define seq1 and seq2
        seq1, seq2 = ReadInput(sys.argv[1]), ReadInput(sys.argv[2])



