"""
Author: Jakidxav
Date: 06.18.2019

Process a DAIC_WOZ transcript for the AVEC challenge, convert the CSV file to a .txt file

The script depends on the following stardardized input format:

Columns: start_time, stop_time, Text
- start_time, stop_time: these should correspond to only one speaker
- Text: this column **must** be labelled Text. This differs from the old DAIC-WOZ data attribute "value".
- Note that there is no "speaker" column like in the old DAIC-WOZ data, as Ellie's portions of the transcripts have been stripped. Only those parts corresponding to the participant's speech are included.
"""

import csv
import pandas as pd
import numpy as np
import os

from clean_text import *
from process_text import *

train_folder = './train/'
change_dir_train = '../../train/'

#we will need to change directories for the dev CSV files
dev_folder = './dev/'
change_dir_dev = '../../dev/'

#where to store the actual transcripts
train_part_dir = '../trainPart/raw/'
dev_part_dir = '../devPart/raw/'

to_replace = '.csv'
replace_with = '_part_raw.txt'

#change to correct directory to start; either train or dev folder
os.chdir(dev_folder)
this_dir = os.getcwd()

#convert csv files to txt files
csv_to_txt(this_dir, to_replace, replace_with, dev_part_dir, change_dir_dev)
