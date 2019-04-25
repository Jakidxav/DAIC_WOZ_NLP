"""
Author: Jakidxav
Date: 04.10.2019

Process DAIC_WOZ text files:
-tokenize by word
-remove semantic information
-split contractions for removal
-remove punctuation
-remove stop words
-remove non-alphabetic characters

The script depends on the following stardardized input format:
Each document should end in .txt
"""

import csv
import pandas as pd
import numpy as np
import os

from clean_text import *


#directory declarations
part_dir_raw = './Part/raw/'
part_dir = './Part/clean_tokens/'

#create directory for saving output
change_dir_clean = '../clean_tokens'
change_dir_raw = '../raw'

#make sure directories exist; if not, create them
if os.path.isdir(part_dir) == False:
    os.makedirs(part_dir)


#change to correct directory
os.chdir(part_dir_raw)
this_dir = os.getcwd()

for subdirs, dirs, files in os.walk(this_dir):
    for filename in files:
        if filename.endswith('.txt'):
            file = open(filename, 'rt')
            text = file.read()
            file.close()
                        
            #rename file for saving output
            filename = '/' + filename
            out_filename = filename.replace('_raw.txt', '_cleaned.txt')
            
            #PROCESS TEXT
            #whitespace tokenize
            tokens = tokenize(text)
            
            #take out semantic information
            no_semantics = remove_semantics(tokens)

            #convert back to string to split apart contractions
            l2s = list_to_string(no_semantics)
            
            #split contractions AFTER removing semantic information
            split = split_contractions(l2s)

            #strip punctuation
            no_punct = strip_punctuation(split)

            #remove stopwords
            no_stops = remove_stopwords(no_punct)

            #remove numbers from tokens
            words = remove_numbers(no_stops)

            #change to output directory
            os.chdir(change_dir_clean)
            this_dir = os.getcwd()
            
            #save processed output
            with open(this_dir+out_filename, "w") as f:
                for token in words:
                    f.write(token + "\n")
            
            #change back to input directory
            os.chdir(change_dir_raw)
            this_dir = os.getcwd()
