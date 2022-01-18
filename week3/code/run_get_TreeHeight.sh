#!/bin/bash
# Author: Booming Bonobos
# Script: run_get_TreeHeight.sh
# Description:  UNIX shell script to test the get treeheight R script
# Saves the output into the a csv file

#Create a variable for an input file

Inputfile='../data/trees.csv'

#Run the get_Treeheights.R

echo "Checking the get_TreeHeight.R"

if [ $# -eq 0 ]
then
	echo "Running the get_TreeHeight.R with default data file"
    
    Rscript get_TreeHeight.R ${Inputfile}

    echo "Writing an output file to a result directory as trees_treeheights.csv"

    echo "Done!"

    #Check if there is a result file in the correct directory and remove the file so it is ready to test with python script.

    FILE="../results/trees_treeheights.csv"

    if [ -f $FILE ]
    then

        echo "R script ran successfully"
        rm $FILE

    else
        echo "Output file was not create from the R script"

    fi


else
    echo "Running the get_TreeHeight.R with an user file .. $1 .."
    
    Rscript get_TreeHeight.R $1

    BASENAME="${1##*/}" #get a basename of the input file

    echo "Writing an output file to a results directory as ${BASENAME%.*}_treeheights.csv "
    
    echo "Done!"

    FILE="../results/${BASENAME%.*}_treeheights.csv" #get the path directory with the correct result file name

    #Check if there is a result file in the correct directory and remove the file so it is ready to test with python script.
    
    if [ -f $FILE ]
    then

        echo "R script ran successfully"
        
        rm $FILE

    else
        echo "Output file was not create from the R script"

    fi

fi


#Run the get_TreeHeight.py

echo "Checking the get_TreeHeight.py"

if [ $# -eq 0 ]
then

    echo "Running the get_TreeHeight.py with default data file"

    python3 get_TreeHeight.py ${Inputfile}

    echo "Writing an output file to a result directory as trees_treeheights.csv"

    echo "Done!"

    FILE="../results/trees_treeheights.csv"

    #Check if the python script run successfully and produce a result file in the correct directory

    if [ -f $FILE ]
    then

        echo "Python script ran successfully"

    else
        echo "Output file was not create from the python script"

    fi

else

    echo "Running the get_TreeHeight.py with an user file .. $1 .."

    python3 get_TreeHeight.py $1

    BASENAME="${1##*/}" #get a basename from the user input file

    echo "Writing an output file to a results directory as ${BASENAME%.*}_treeheights.csv "
    
    echo "Done!"

    FILE="../results/${BASENAME%.*}_treeheights.csv"

    #Check if the python script run successfully and produce a result file in the correct directory
    
    if [ -f $FILE ]
    then

        echo "Python script ran successfully"

    else
        echo "Output file was not create from the python script"

    fi

fi