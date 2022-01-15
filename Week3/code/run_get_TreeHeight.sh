#!/bin/bash
# Author: Chalita Chomkatekaew chalita.chomkatekaew20@imperial.ac.uk
# Script: run_get_TreeHeight.sh
# Description:  UNIX shell script to test the get treeheight R script
# Saves the output into the a csv file
# Date: 6 Oct 2021

#Create a variable for an input file
Inputfile='../data/trees.csv'

#Run the get_Treeheights.R

if [ $# -eq 0 ]
then
	echo "Running the get_TreeHeight.R with default script"
    
    Rscript get_TreeHeight.R ${Inputfile}

    echo "Writing an output file to a result directory as trees_treeheights.csv"

    echo "Done"

else
    echo "Running the get_TreeHeight.R with an user file .. $1 .."
    
    Rscript get_TreeHeight.R $1

    echo "Writing an output file to a results directory as ${1%.*}_treeheights.csv "
    echo "Done!"

fi

