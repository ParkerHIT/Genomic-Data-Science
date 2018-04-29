#!/usr/bin/python

import shutil
import sys
import os
import operator
os.chdir("C:\\Users\AdminUser\Downloads")
#finalexamfile = open("examtest.txt","r")
finalexamfile = open("dna2.fasta","r")

#initialize the count variable
rec_count=0

#loop through each line in the file 
#for line in open("examtest.txt"):
for line in open("dna2.fasta"):
       if line[0:1] == '>':
        rec_count = rec_count+1
       if line[0:1] != '>' and rec_count == 0:
            print ("No records in this file")
            
#Print the number of records in the file            
if rec_count > 0 :
    print ("The number of records in this DNA FASTA File is", rec_count)

