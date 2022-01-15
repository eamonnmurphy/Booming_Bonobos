#!/usr/bin/env python3

"""This script is for aligning the two DNA sequences"""

__appname__ = '[ALIGN SEQS BETTER]'
__author__ = 'Booming bonobos'
__version__ = '0.0.1'

## import

import sys
import pickle
import os

def ReadInput(x): 
    with open(x, "r") as fileinput: 
        temp = fileinput.readlines()[1:] #skip the first line
        temp1 = [i.strip() for i in temp] #remove the new line characters
        seq_input = ''.join(temp1) #merge the sequences into a one string
    return seq_input

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
    nulmatched = "." * startpoint + s2
    template = s1        

    return score, matched, nulmatched, template

def main(argv):
    seq1 = ReadInput("../data/seq1.fasta")
    seq2 = ReadInput("../data/seq2.fasta")

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

    my_best_align = None
    my_best_score = -1
    all_best = {}
    
    for i in range(l1):
        z, bestmatched, line1, line2 = calculate_score(s1, s2, l1, l2, i)
        if z > my_best_score:
            my_best_score = z
            my_best_matched = bestmatched
            my_best_align = line1
            tempseq = line2
            if os.path.isfile('best_align.pkl'):
                with open('best_align.pkl', 'rb') as align:
                    pickle.dump([my_best_score, my_best_matched, my_best_align, tempseq], align)
            else:
                with open('best_align.pkl', 'wb') as out:
                    pickle.dump([my_best_score, my_best_matched, my_best_align, tempseq], align)






    



    return 0


if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)


seq1 = ReadInput("../data/testseq1.fasta")
seq2 = ReadInput("../data/testseq2.fasta")

if l1 >= l2:
    s1 = seq1
    s2 = seq2
else:
    s1 = seq2
    s2 = seq1
    l1, l2 = l2, l1