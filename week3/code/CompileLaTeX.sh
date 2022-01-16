#!/bin/bash
# Author: Lizzie Bru eab21@imperial.ac.uk
# Script: CompileLaTeX.sh
# Desc: compiles LaTeX with Bibtex
# Arguments: 1 -> .tex file
# Date: Oct 2021

# compile LaTeX wth Bibtex
pdflatex $notex.tex
bibtex $notex
pdflatex $notex.tex
pdflatex $notex.tex
evince $notex.pdf &

## Cleanup
[ -e *.aux ] && rm *.aux
[ -e *.aux ] && rm *.log
[ -e *.aux ] && rm *.bbl
[ -e *.aux ] && rm *.blg


# how to run this: type into terminal:
    # bash CompileLaTeX.sh FirstExample
    ##--> don't include the .tex ending for the file name
    ##--> if you're doing it for a .tex file in a different directory, just use the relative path to CompileLateX.sh