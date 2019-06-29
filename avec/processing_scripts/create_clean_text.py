"""
Author: Jakidxav
Date: 06.19.2019

Process AVEC text files:
- tokenize by word
- convert tokens to lowercase
- remove semantic information
- split contractions for removal
- remove punctuation
- remove stop words
- remove non-alphabetic characters

The script depends on the following stardardized input format:
Each document should end in .txt
"""

import csv
import pandas as pd
import numpy as np
import os

from clean_text import *
from process_text import *

#directory declarations
train_part_dir_raw = './trainPart/raw/'
train_part_dir = './devPart/cleaned/'
train_part_dir_with_i = './devPart/cleaned_with_i/'

dev_part_dir_raw = './devPart/raw/'
dev_part_dir = './devPart/cleaned/'
dev_part_dir_with_i = './devPart/cleaned_with_i/'

test_part_dir_raw = './testPart/raw/'
test_part_dir = './testPart/cleaned/'
test_part_dir_with_i = './testPart/cleaned_with_i/'

#create directory for saving output
change_dir_clean = '../cleaned/'
change_dir_clean_with_i = '../cleaned_with_i/'
change_dir_raw = '../raw/'

to_replace = '_raw.txt'
replace_with = '_cleaned.txt'

#change to correct directory
change_to_dir = dev_part_dir_raw

os.chdir(change_to_dir)
this_dir = os.getcwd()

#process text here
process_daic_woz(this_dir, to_replace, replace_with, change_dir_clean_with_i, change_dir_raw)
