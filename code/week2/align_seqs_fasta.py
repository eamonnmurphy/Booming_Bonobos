#!/user/bin/env python3
# Author: Uva Fung uf21@imperial.ac.uk
# Script: align_seqs_fasta.py
# Desc: align seqeunces -- groupwork
# Date: Jan 6 2022

"""Align two seqeunces and gives the best alignment as output"""

__appname__ = 'AlignSequence'
__author__ = 'Booming Bonobos'
__version__ = '0.0.1'


## import and prepare the input sequences
def ReadInput(x): 
    """ Modify the seqeunce file so that only the seqeunce is retained """
    with open(x, "r") as fileinput: 
        temp = fileinput.readlines()[1:] #skip the first line
        temp1 = [i.strip() for i in temp] #remove the new line characters
        seq_input = ''.join(temp1) #merge the sequences into a one string
    return seq_input

## Define a function that computes a score by returning the number of matches starting
# from arbitrary startpoint (chosen by user)
def calculate_score(s1, s2, l1, l2, startpoint): # it will run with the startpoint of 0 if not specify
    """ Calculate the matching score of the two DNA seqeunces """
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

def main(argv):
    """ To confirm if the two seqeunce files are being inported correctly """
    if len(sys.argv) <= 2 : # if there is no input argument or only one argument

        print("Not enough input arguments, Running alignment on default sequences")
        
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
    return None

if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)