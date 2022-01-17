# CMEE Booming Bonobos Groupwork

This repository contains codes and data for Computational Methods in Ecology and Evolution (CMEE) groupwork.
Instructions to run the codes can be found [here](https://mhasoba.github.io/TheMulQuaBio/intro.html).

Data required to run the coding scripts can be downloaded from the following [repository](https://github.com/mhasoba/TheMulQuaBio).

***

#### Languages:
Python 3.9.7

R version 3.6.3

RStudio 2021.09.0


***********
#### Dependencies:
A UNIX based Operating System is needed to run the projects. Linux and Mac OS are both possible options. Linux Ubuntu can be downloaded [here](https://ubuntu.com/)


******************
#### Installation:

###### Python 3.9.7 can be installed [here](https://www.python.org/downloads/release/python-397/)

###### R version 3.6.3 for MacOS can be installed [here](https://cran.r-project.org/bin/macosx/)
###### R version 3.6.3 for Linux can be installed [here](https://cran.r-project.org/)
###### RStudio 2021.09.0 can be installed [here](https://www.rstudio.com/products/rstudio/download/)

***********

#### Project structure and usage:
This project contains three folders (week2, week3, week7).
Within each folder there are four sub-folders: code, data, results, sandbox.

Code stores all the codes written for groupwork practicals. Data stores all the data needed to run the scripts stored in code. Results store the output of coding scripts.

##### Files in folders:
###### Week2:

    code:
          align_seqs_fasta.py: take any two fasta sequences (in separate files) to be aligned as input
          align_seqs_better.py: take any two fasta sequences (in separate files) to be aligned as input, taking into account all the equally-best alignments
    data:
          407228326.fasta
          407228412.fasta
          seq1.fasta
          seq2.fasta


###### Week3:
    code:
          get_TreeHeight.R: R script that calculates tree heights for all trees and saves output as new csv
          get_TreeHeight.py: Python script that calculates tree heights for all trees and saves output as new csv
          run_get_TreeHeight.sh: Bash script that runs both get_TreeHeight.R and run_get_TreeHeight.sh
          TAutoCorr.R: calculates the correlation between pairs of years to analysis temperature trends in Florida
          TAutoCorr_writeup.tex: latex file for compiling a report on Florida temperatures
          Floridabiblio.bib: stores the bibliography for the report
          PP_Regress_loc.R: calculates linear regression on subsets of the data corresponding to i) Feeding Type, ii) Predator life Stage and iii) Location
    data:
          EcolArchives-E089-51-D1.csv
          KeyWestAnnualMeanTemperature.RData
          trees.csv

###### Week7:
    code:
          oaks_debugme.py: search for oaks in a given dataset while handling for slight typos
    data:
          TestOaksData.csv



*****************
#### Author name and contact:
Chalita Chomkatekaew chalita.chomkatekaew20@imperial.ac.uk

Eamonn Murphy eamonn.murphy21@imperial.ac.uk

Emma MacDonald emma.macdonald21@imperial.ac.uk

Lizzie Bru e.bru21@imperial.ac.uk

Uva Fung uf21@imperial.ac.uk
