"""
Author: Jakidxav
Date: 06.25.2019

Process a DAIC_WOZ transcript for the AVEC challenge, calculating total participant speech time in the transcript. This information will be used later to calculate the "words per minute" feature in our correlation analysis.

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
from process_pnums import *
from process_time import *

#lists to append each transcript feature to
#append participant number from filename for indexing
participant_nums = []

#count total time per transcript
total_time = []

#change directory
change_dir_train = './train/'
change_dir_dev = './dev/'

to_save_train = './transcript_times_train.csv'
to_save_dev = './transcript_times_dev.csv'

###change values here to redirect output
change_to_dir = change_dir_dev

#filename to save to
to_save = to_save_dev
###

#get the time per transcript for a given participant, save to a csv file
time_per_transcript(change_to_dir, to_save, participant_nums, total_time)
