"""
Author: Jakidxav
Date: 06.25.2019

This program cleans and extends a positive and negative words list (link below). It then passes those lists to our training and development directories to create words counts based off of those lists and saves the output as a CSV file. We are going to use these word counts for our correlation analysis to determine if the rate of positive or negative word usage corresponds to higher reported PHQ-8 score.
"""

import csv
import pandas as pd
import numpy as np
import os

from clean_text import *
from process_word_counts import *

#change directory
with_i_dir_train = './trainPart/cleaned_with_i'
with_i_dir_dev = './devPart/cleaned_with_i'
with_i_dir_test = './testPart/cleaned_with_i'

#filenames to save to
to_save_train = 'pos_neg_counts_train.csv'
to_save_dev = 'pos_neg_counts_dev.csv'
to_save_test = 'pos_neg_counts_test.csv'

#positive and negative word lists obtained from here:
#http://www.wjh.harvard.edu/~inquirer/homecat.htm
pos_neg_file = 'inquirerbasic.xls'

#we need the participant numbers to create TaggedDocument
participant_nums = []

#positive and negative word counts lists
pos, neg = [], []
pos_freq, neg_freq = [], []

#change this for train or dev set directory
change_to_dir = with_i_dir_test

#where to save output
to_save = to_save_test

#extract positive and negative word lists
positive, negative = process_pos_neg_file(pos_neg_file)

#main processing step: creates a dataframe of word counts, then saves it to a CSV
positive_negative_counts(change_to_dir, to_save, participant_nums, positive, pos_freq, negative, neg_freq)
