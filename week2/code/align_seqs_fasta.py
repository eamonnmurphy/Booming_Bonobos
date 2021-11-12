#!/usr/bin/env python3

""" This script compares two sequences to find the best alignment """
__author__= "Emma (emma.macdonald21@imperial.ac.uk)"
__version__= "0.0.1"

#########################################################################
### IMPORT PACKAGES
import sys

########################################################################
### CALCULATE SEQUENCE LENGTH 

def seqlength(seq1, seq2):
    """ Measures sequences and assigns the longest sequence to s1 and the shortest sequence to s2. """
    l1 = len(seq1)
    l2 = len(seq2)
    if l1 >= l2:     # if seq1 is shorter, assign seq1 to s1
        s1 = seq1
        s2 = seq2
    else:           #  if seq2 is shorter, assign seq2 to s1
        s1 = seq2
        s2 = seq1
        l1, l2 = l2, l1 # swap the two lengths so s1 still corresponds with l1 even if swapped

    return l1, l2, s1, s2

#########################################################################'
### CALCULATE ALIGNMENT SCORE

def calculate_score(s1, s2, l1, l2, startpoint):
    """ Aligns sequence 1 and 2 and calculates a score for each alignment. """
    matched = "" # to hold string displaying alignements,
    score = 0
    for i in range(l2):
        if (i + startpoint) < l1:
            if s1[i + startpoint] == s2[i]: # if the bases match, add a * to the string and add to score
                matched = matched + "*"
                score = score + 1
            else:                          # if the bases don't match, add a - to the string
                matched = matched + "-"

    # Printing the different alignments
    print("." * startpoint + matched)           
    print("." * startpoint + s2)
    print(s1)
    print(score) 
    print(" ")

    return score

#####################################################################################
######### CHOOSING THE BEST ALIGNMENT SCORE

def bestscore(s1, s2, l1, l2):
    """ Decides which score was best and outputs it. """
    my_best_align = None
    my_best_score = -1

    for i in range(l1): # Note that you just take the last alignment with the highest score, this loops through alignments
        z = calculate_score(s1, s2, l1, l2, i)
        if z > my_best_score:   ### Finds best output of calculate score
            my_best_align = "." * i + s2 ## Adds correct amount of dots in then sequence to show best alignment
            my_best_score = z
    print(my_best_align)
    print(s1)
    print("Best score:", my_best_score)
    return my_best_align, my_best_score

####################################################################################
########### MAIN FUNCTION TO MAKE IT A PROGRAMME

def main(argv):
######### GETTING THE INPUT SEQUENCES ###############
    """ Main function """
    tmp = []
    try: 
        f1 = open(sys.argv[1]) # If user has ran code with file name, opens that
        for line in f1:
            tmp.append(line)
        f1.close()

        f2 = open(sys.argv[2]) # If user has ran code with a 2nd file name, opens that
        for line in f2:
            tmp.append(line)
        f2.close()
    
    except:
        f1 = open('../data/seq1.csv','r') # uses two files from data directory if user has not ran with a file
        for line in f1:
            tmp.append(line)
        f1.close()

        f2 = open('../data/seq2.csv','r')
        for line in f2:
            tmp.append(line)
        f2.close()

    tmp2 = [x[:-1] for x in tmp]   #### List comprehension that removes \n from tmp list 
    print(tmp2)

    seq1 = tmp2[0]
    seq2 = tmp2[1]

####### RUNNING THE FUNCTIONS ###################
    l1,l2,s1,s2= seqlength(seq1,seq2)
    score = calculate_score(s1, s2, l1, l2, 0)
    my_best_align, my_best_score = bestscore(s1 ,s2 ,l1, l2)

####### WRITING TO AN OUTPUT FILE ###############
    f = open('../results/align_seqs_fasta_results.txt','w')
    f.write(str(my_best_align))
    f.write(str("\n"))
    f.write(str(s1))
    f.write("\nBest score: " + str(my_best_score))
    f.close()
    print("Your results can be found in the results directory!")

    return 0

if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)