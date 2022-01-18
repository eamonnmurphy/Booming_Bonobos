#!/bin/bash
# Test get_TreeHeight.R script

# Run file
Rscript get_TreeHeight.R ../data/trees.csv

# Check that output file exists
FILE=../results/trees_treeheights.csv

if [ -f "$FILE" ]; then
    echo "R Script run successfully"
else
    echo "Output file was not created"
fi

# Test get_TreeHeight.py script
rm $FILE

# Run file
python3 get_TreeHeight.py ../data/trees.csv

# Check that output file exists
FILE=../results/trees_treeheights.csv

if [ -f "$FILE" ]; then
    echo "Python script run successfully"
else
    echo "Output file was not created"
fi

