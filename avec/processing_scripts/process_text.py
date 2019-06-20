import csv
import pandas as pd
import numpy as np
import os

from clean_text import *


"""
This helper method converts a CSV file to a TXT file, that way we can process it using NLTK.
Input your current directory where the CSV files are held, as well as what your old and new text files end with. Then provide a directory to save to, as well as a redirect for how to get back to your raw directory.
"""
def csv_to_txt(this_dir, to_replace, replace_with, save_dir, original_dir):
    for subdir, dirs, files in os.walk(this_dir):
        for file in files:
            if file.endswith('.csv'):
                #NOTE: the filename should be constructed as 'num_TRANSCRIPT.csv'
                #save output file as the original name, but as a text file
                out_file_part = file.replace(to_replace, replace_with)      #participant only

                #read in the CSV file as a dataframe
                df = pd.read_csv(file)

                #discard all columns but the participant's speech, save as .txt file
                #**CHANGE THIS DIRECTORY when re-routing to train/dev folders
                os.chdir(save_dir)
                np.savetxt(out_file_part, df.Text.values, fmt=['%s'])

                #change back to input directory
                #**CHANGE THIS DIRECTORY when re-routing to train/dev folders
                os.chdir(original_dir)
                this_dir = os.getcwd()



"""
This helper method includes all of the processing steps used on both the old and the newly released DAIC-WOZ datasets.

Input your current directory where the raw TXT files are held, as well as what your old and new text files end with. Then provide a directory to save to, as well as a redirect for how to get back to your raw directory.
"""
def process_daic_woz(this_dir, to_replace, replace_with, save_dir, original_dir):
    for subdirs, dirs, files in os.walk(this_dir):
        for filename in files:
            if filename.endswith('.txt'):
                file = open(filename, 'rt')
                text = file.read()
                file.close()

                #rename file for saving output
                filename = '/' + filename
                out_filename = filename.replace(to_replace, replace_with)
                #PROCESS TEXT
                #whitespace tokenize
                tokens = tokenize(text)

                #convert to lowercase
                lower = lower_case(tokens)

                #take out semantic information
                no_semantics = remove_semantics(lower)

                #convert back to string to split apart contractions
                l2s = list_to_string(no_semantics)

                #split contractions AFTER removing semantic information
                split = split_contractions(l2s)

                #strip punctuation
                no_punct = strip_punctuation(split)

                #remove stopwords
                no_stops = remove_stopwords(split)

                #remove numbers from tokens
                words = remove_numbers(no_stops)

                #change to output directory
                os.chdir(save_dir)
                this_dir = os.getcwd()

                #save processed output
                with open(this_dir+out_filename, "w") as f:
                    for token in words:
                        f.write(token + "\n")

                #change back to input directory
                os.chdir(original_dir)
                this_dir = os.getcwd()


