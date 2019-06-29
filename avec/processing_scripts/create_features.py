"""
Author: Jakidxav
Date: 06.26.2019

This program loops over the training and development directories and counts common pronouns, filler words, and
absolute words. These features will be used to help build up our correlation analysis on what types of features
correspond to high reported PHQ-8 scores.
"""

import csv
import pandas as pd
import numpy as np
import os

from clean_text import *
from process_features import *

#lists to append each transcript feature to
#append participant number from filename for indexing
participant_nums = []
#count total words, words per sentence
total_words = []
#filler words, personal prnouns lists
pronouns1, pronouns2, pronouns3 = [], [], []

fillers, absolute_words = [], []

#create lists containing fillers, pronouns
filler_list = ['uh', 'uhhh', 'um', 'ummm']

#source: https://en.wikipedia.org/wiki/English_personal_pronouns
singular_list = ['i', "i'm", 'me', 'myself', 'mine', 'my']
plural_list = ['we', 'us', 'ourselves', 'ourself', 'ours', 'our']
third_list = ['he', 'him', 'himself', 'his', 'she', 'her', 'herself', 'hers', 'her',
             'they', 'them', 'themselves', 'themself', 'theirs', 'their']

#create list for absolutist words
absolute_list = ['always', 'nothing', 'completely', 'never', 'all', 'every', 'none', 'only']

#change directory
with_i_dir_train = './trainPart/cleaned_with_i'
with_i_dir_dev = './devPart/cleaned_with_i'
with_i_dir_test = './testPart/cleaned_with_i'

#filenames to save to
to_save_train = 'features_train.csv'
to_save_dev = 'features_dev.csv'
to_save_test = 'features_test.csv'

#change this for train or dev set directory
change_to_dir = with_i_dir_train

#where to save output
to_save = to_save_train

create_features(change_to_dir, to_save, participant_nums, total_words, pronouns1, pronouns2, pronouns3, fillers, absolute_words, filler_list, singular_list, plural_list, third_list, absolute_list)
