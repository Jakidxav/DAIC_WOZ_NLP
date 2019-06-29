"""
Author: Jakidxav
Date: 06.18.2019

Process a DAIC_WOZ transcript for the AVEC challenge, convert the CSV file to a .txt file

The script depends on the following stardardized input format:

Columns: Start_Time, End_Time, Text, Confidence
- Start_Time, End_Time: these should correspond to only one speaker
- Text: this column **must** be labelled Text. This differs from the old DAIC-WOZ data attribute "value".
- Note that there is no "speaker" column like in the old DAIC-WOZ data, as Ellie's portions of the transcripts have been stripped. Only those parts corresponding to the participant's speech are included.
"""

import csv
import pandas as pd
import numpy as np
import os

from clean_text import *
from process_text import *

#we will need to change directories for the CSV files
dir_train = './train/'
change_dir_train = '../../train/'

dir_dev = './dev/'
change_dir_dev = '../../dev/'

dir_test = './test/'
change_dir_test = '../../test/'

#where to store the actual transcripts
part_dir_train = '../trainPart/raw/'
part_dir_dev = '../devPart/raw/'
part_dir_test = '../testPart/raw'

to_replace = '.csv'
replace_with = '_part_raw.txt'

#change to correct directory to start; either train, dev, or test folder
change_to_dir = dir_test
original_dir = change_dir_test
part_dir = part_dir_test

os.chdir(change_to_dir)
this_dir = os.getcwd()

#convert csv files to txt files
csv_to_txt(this_dir, to_replace, replace_with, part_dir, original_dir)
