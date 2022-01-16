#!/usr/bin/env python3

""" This script compares two sequences to find the best alignment """
__appname__ = '[ALIGN SEQS]'
__author__= "The booming bonobos (github.com/eamonnmurphy/Booming_Bonobos)"
__version__= "0.0.1"

####################################################################################
######### IMPORT PACKAGES

import sys

####################################################################################
######### PREPARING THE FASTA FILES

def ReadInput(x):
    """ This function takes out the sequence from a given fasta file and puts it into one usable string. """
    with open(x, "r") as fileinput: 
        temp = fileinput.readlines()[1:] #skip the first line
        temp1 = [i.strip() for i in temp] #remove the new line characters
        seq_input = ''.join(temp1) #merge the sequences into a one string
    return seq_input

####################################################################################
######### CALCULATE SEQUENCE LENGTH 

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

####################################################################################
######### CALCULATE ALIGNMENT SCORE

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

####################################################################################
######### CHOOSING THE BEST ALIGNMENT SCORE

def bestscore(s1, s2, l1, l2):
    """ This function decides which score was best. """
    my_best_align = None
    my_best_score = -1
    best_align_storage = []

     # loops through alignments and calculates score
    for i in range(l1): 
        z = calculate_score(s1, s2, l1, l2, i)

        # if new highest best score found
        if z > my_best_score:
            best_align_storage = [] # clear list
            best_score_storage = []
            my_best_align = "." * i + s2 ## Adds correct amount of dots in then sequence to show best alignment
            my_best_score = z
            best_align_storage.append(my_best_align) # asign new results to a list

        # if equally good score found
        if z == my_best_score:
            my_best_align = "." * i + s2 ## Adds correct amount of dots in then sequence to show best alignment
            my_best_score = z
            best_align_storage.append(my_best_align) # append results to lists 

    for i in range(len(best_align_storage)):
        print(best_align_storage[i])
    print(s1)
    print("Best score:", my_best_score)
    return best_align_storage, my_best_score

####################################################################################
######### MAIN ARGUMENT

def main(argv):
    """ This is the main function """

######### INPUT
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

######### RUNNING THE FUNCTIONS
    l1,l2,s1,s2= seqlength(seq1,seq2)
    score = calculate_score(s1, s2, l1, l2, 0)
    best_align_storage, my_best_score = bestscore(s1 ,s2 ,l1, l2)

######### OUTPUT
    with open("../results/seq_aligns_better.txt", "w") as f:
        for i in range(len(best_align_storage)):
            f.write(best_align_storage[i])
            f.write(str("\n"))
        f.write(str(s1))
        f.write("\nBest score: " + str(my_best_score))
        f.close()
        print("Your results can be found in the results directory!")

    return None

if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)