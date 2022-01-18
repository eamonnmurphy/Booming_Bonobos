#!/usr/bin/env python3

"""This script is for aligning the two DNA sequences"""

__appname__ = '[ALIGN SEQS]'
__author__ = 'Booming bonobos'
__version__ = '0.0.1'

## import

import sys

# Two example sequences to match
#seq2 = "ATCGCCGGATTACGGG"
#seq1 = "CAATTCGGAT"

## import and prepare the input sequences
def ReadInput(x): 
    """Read the sequences in the inputs provided and merge them into a string"""
    with open(x, "r") as fileinput: 
        temp = fileinput.readlines()[1:] #skip the first line
        temp1 = [i.strip() for i in temp] #remove the new line characters
        seq_input = ''.join(temp1) #merge the sequences into a one string
    return seq_input


## Define a function that computes a score by returning the number of matches starting
# from arbitrary startpoint (chosen by user)
def calculate_score(s1, s2, l1, l2, startpoint): # it will run with the startpoint of 0 if not specify
    """Compute a score of similarity between the 2 sequences"""
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
    # print("." * startpoint + matched) # "." * startpoint means how many time "*" is repeated based on the number of startpoint          
    # print("." * startpoint + s2)
    # print(s1)
    # print(score) 
    # print(" ")

    return score

## Define a function to find a best sequence alignment

def find_best_seqs(seqA, seqB):
    """Find the best alignment of the sequences"""
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
    my_best_score = -1
 
    for i in range(l1): # Note that you just take the last alignment with the highest score
        z = calculate_score(s1, s2, l1, l2, i)
        if z > my_best_score:
            my_best_align = "." * i + s2 # think about what this is doing!
            my_best_score = z 
    print(my_best_align)
    print(s1)
    print("Best score:", my_best_score)
    print("Done!")

    return my_best_align, my_best_score, s1

def main(argv):
    """Read in data, find the best alignments, and save these to the results folder"""
    if len(sys.argv) <= 2 : # if there is no input argument or only one argument

        print("Not enough input arguments, Running the alignment on default sequences")
        
        #Read input from default files and define seq1 and seq2
        seq1 = ReadInput("../data/seq1.fasta")
        seq2 = ReadInput("../data/seq2.fasta")

        #print the first 10 nucleotides/sequence
        print("The first sequence is: %s ... \nThe second sequence is: %s ..." % (seq1[0:11], seq2[0:11]) )

    else: # If there are 2 input arguments 
        print("Reading the input files....")
            
        # print the name of the input files
        print("The first input sequence is: %s \nThe second input sequence is: %s" % (str(sys.argv[1]), (str(sys.argv[2]))))

        #Read input files and define seq1 and seq2
        seq1, seq2 = ReadInput(sys.argv[1]), ReadInput(sys.argv[2])

    my_best_align, my_best_score, s1 = find_best_seqs(seq1, seq2)

    ######### OUTPUT
    with open("../results/seq_aligns.txt", "w") as f:
         f.write(str(my_best_align))
         f.write(str("\n"))
         f.write(str(s1))
         f.write("\nBest score: " + str(my_best_score))
         print("Your results can be found in the results directory!")

    return None

if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)