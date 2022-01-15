#!/bin/bash
# Author: Booming Bonobos
# Script: run_get_TreeHeight.sh
# Description:  UNIX shell script to test the scripts get_TreeHeight.R and get_TreeHeight.py
# Date: Jan 2022

# run R script

echo "Running the R script"

Rscript get_TreeHeight.R ../data/trees.csv

echo "Finished running the R script"


# Check that output file exists

FILE = ../results/trees_treeheights.csv

if [ -f "$FILE" ]; then
    echo "R script ran successfully"
else
    echo "Output file was not created from the R script"
fi


# remove the output file from the R script so that can test the python script

cd ../results
rm trees_treeheights.csv


# run python script

echo "Running the python script"

python3 get_TreeHeight.py ../data/trees.csv

echo "Finished running the python script"


# Check that output file exists

FILE = ../results/trees_treeheights.csv

if [ -f "$FILE" ]; then
    echo "Python script ran successfully"
else
    echo "Output file was not created from the python script"
fi


