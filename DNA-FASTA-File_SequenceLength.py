#!/usr/bin/python

import shutil
import sys
import os
import operator
import struct
os.chdir("C:\\Users\AdminUser\Downloads")
finalexamfile = open("examtest.txt","r")
#finalexamfile = open("dna2.fasta","r")

# To initliaze the variables
rec_count=0
DNA_char_count = 0
rec_pair = {}
seq_pair = {}

# To read through each line in the FASTA File
for line in open("examtest.txt"):
#for line in open("dna2.fasta"):
       
    if line[0:1] == '>':
        rec_count = rec_count+1
        # To store each record by its row number and the Sequence ID
        seq_pair.update({rec_count:line}) 
        DNA_char_count = 0
    if line[0:1] in ('A','G','C','T'):
        # To start counting the DNA characters in each sequence
        DNA_char_count = DNA_char_count + len(line.strip())

    # To store each record by its row number and the length of sequence
    rec_pair.update({rec_count:DNA_char_count})


#Print the number of records in the file            
if rec_count > 0 :
    print ("The number of records in this DNA FASTA File is", rec_count)
    print ("The maximum sequence length in this DNA FASTA File is",max(rec_pair.values()))
    print ("The minimum sequence length in this DNA FASTA File is",min(rec_pair.values()))
    #print (seq_pair)

