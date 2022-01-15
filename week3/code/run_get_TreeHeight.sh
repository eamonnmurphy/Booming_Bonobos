#!/bin/bash
# Author: Booming Bonobos (github.com/eamonnmurphy/Booming_Bonobos)
# Script: run_get_TreeHeight.sh
# Description: tests get_TreeHeight.R and get_TreeHeight.py
# Arguments: 1 argument
# Date: Jan 2022

if [ -f "$1" ]; then # checks if file exists
# if file exists:

echo "Running get_TreeHeight.R"
Rscript get_TreeHeight.R $1

echo "Running get_TreeHeight.py"
python3 get_TreeHeight.py $1

else # if file doesn't exist, run on example file:

echo "Running scripts on example file ../data/trees.csv"

echo "Running get_TreeHeight.R"
Rscript get_TreeHeight.R ../data/trees.csv

echo "Running get_TreeHeight.py"
python3 get_TreeHeight.py ../data/trees.csv

fi # close if else statements