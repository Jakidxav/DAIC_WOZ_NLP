"""
Author: Jakidxav
Date: 06.26.2019

This helper method is the main processing step in the feature_selection.py script.
"""

import csv
import pandas as pd
import numpy as np
import os

from clean_text import *

"""
Input lists of pronouns, filler words, and absolute words and loop over a directory.
Then save each set of features to a dataframe with the participant number as the index.
"""
def create_features(change_to_dir, keyword, to_save, participant_nums, total_words, wps, pronouns1, pronouns2, pronouns3, fillers, absolute_words, filler_list, singular_list, plural_list, third_list, absolute_list):
    #change directory
    change_dir = os.chdir(change_to_dir)

    #get current working directory
    this_dir = os.getcwd()
    filenames = os.listdir(this_dir)

    #sort filenames for sorting vectors
    filenames = sorted(filenames)

    #need to iterate through documents
    #create a list of *strings*, each one containing the transcript of a participant
    for filename in filenames:
        if filename.endswith('.txt'):

            #read in file contents
            file = open(filename, 'rt')
            text = file.read()

            #count sentences in file
            sentence_count = count_sentences(filename)

            file.close()

            #participant numbers will differ in placement between training and development sets
            #training set files start with "training_", and development set files start with "developement_"
            if keyword == 'train':
                participant_nums.append(int(filename[9:12]))
            else:
                participant_nums.append(int(filename[12:14]))

            #whitespace tokenize
            tokens = tokenize(text)

            #count tokens here for total words
            total = len(tokens)
            total_words.append(total)

            #calculate words per sentence
            average_words = total / sentence_count
            wps.append(average_words)

            #now loop through fillers, pronouns, absolute words
            fill = list_in_text(filler_list, tokens)
            fillers.append(fill)

            single = list_in_text(singular_list, tokens)
            pronouns1.append(single)

            plural = list_in_text(plural_list, tokens)
            pronouns2.append(plural)

            third = list_in_text(third_list, tokens)
            pronouns3.append(third)

            absolute = list_in_text(absolute_list, tokens)
            absolute_words.append(absolute)

    #save features to dataframe     
    features_i = pd.DataFrame({'id': participant_nums,
                            'num_words': total_words,
                            'wps': wps,
                            'fillers': fillers,
                            'p1': pronouns1,
                            'p2': pronouns2,
                            'p3': pronouns3,
                            'abs': absolute_words})
    
    #then save features to csv
    features_i.to_csv(to_save, sep='\t')
