#!/usr/bin/env python3

"""This script is for aligning the two DNA sequences"""

__appname__ = '[ALIGN SEQS BETTER]'
__author__ = 'Booming bonobos'
__version__ = '0.0.1'

## import

import sys
import pickle

# Two example sequences to match
#seq2 = "ATCGCCGGATTACGGG"
#seq1 = "CAATTCGGAT"

## import and prepare the input sequences
def ReadInput(x): 
    with open(x, "r") as fileinput: 
        temp = fileinput.readlines()[1:] #skip the first line
        temp1 = [i.strip() for i in temp] #remove the new line characters
        seq_input = ''.join(temp1) #merge the sequences into a one string
    return seq_input

## Define a function that computes a score by returning the number of matches starting
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

    return score, matched

def find_best_seqs(seqA, seqB):
    # Assign the longer sequence s1, and the shorter to s2
    # l1 is length of the longest, l2 that of the shortest
    l1 = len(seqA)
    l2 = len(seqB)
    if l1 >= l2:
        s1 = seqA
        s2 = seqB
    else:
        s1 = seqB
        s2 = seqA
        l1, l2 = l2, l1 # swap the two lengths

    #now try to find the best match (highest score) for the two sequences
    my_best_align = None
    my_best_score = -1 #even if the score is zero, it will be saved.
    all_best = {}

    for i in range(l1): # Note that you just take the last alignment with the highest score
        z, seqMatch = calculate_score(s1, s2, l1, l2, i)
        if z > my_best_score:
            all_best = {}

            my_best_align = "." * i + s2
            my_best_score = z

            all_best["Align " + str(1)] = [my_best_score, my_best_align]
        elif z == my_best_score:
            my_best_align = "." * i + s2 # think about what this is doing!
            
            value = len(all_best.keys())

            all_best["Align " + str(value + 1)] = [my_best_score, my_best_align]
    
    return(all_best)

def main(argv):
    if len(sys.argv) <= 2 : # if there is no input argument or only one argument

        print("Not enough input arguments, Running the alignment on default sequences")
        
        #Read input from default files and define seq1 and seq2
        seq1 = ReadInput("../data/seq1.fasta")
        seq2 = ReadInput("../data/seq2.fasta")

        #print the first 10 nucleotides/sequence
        print("The first sequence is: %s ... \n The second sequence is: \
            %s ..." % (seq1[0:11], seq2[0:11]) )

    else: # If there are 2 input arguments 
        print("Reading the input files....")
            
        # print the name of the input files
        print("This first input sequence is: %s \n \
            This second input sequence is: %s" % \
                (str(sys.argv[1]), (str(sys.argv[2]))))

        #Read input files and define seq1 and seq2
        seq1, seq2 = ReadInput(sys.argv[1]), ReadInput(sys.argv[2])

    my_best_scores = find_best_seqs(seq1, seq2)
    
    with open("../results/seq_aligns.txt", "w") as f:
        for key, value in my_best_scores.items():
            f.write("%s: %s\n" % (key, value))

    return None

if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)