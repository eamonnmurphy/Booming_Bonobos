#!/bin/bash
# Author: Uva Fung u.fung21@imperial.ac.uk
# Script: run_get_TreeHeight.sh
# Description:  UNIX shell script to run get_treeheight R script and saves output as new csv file
# Date: Jan 6 2022

#Create a variable for an input file
Inputfile='../data/trees.csv'

#Run get_Treeheights.R

# Error message when no file is entered
if [[ -z "$1" ]]; then
   printf '%s\n' "No file entered"
   exit 1
fi 

# Run with default data
if [ $# -eq 0 ]
then
	echo "Running get_TreeHeight.R on default script"
    
    Rscript get_TreeHeight.R ${Inputfile}

    echo "Writing trees_treeheights.csv output file to result directory "

    echo "Done!"
fi

if [ $# -eq 1 ]
then
    echo "Running get_TreeHeight.R on user file .. $1 .."
    
    Rscript get_TreeHeight.R $1

    echo "Writing ${1%.*}_treeheights.csv output file to results directory "
    echo "Done!"

else
    echo " Cannot run file. Make sure only one data file is being input. "
fi

#Run get_Treeheights.py
