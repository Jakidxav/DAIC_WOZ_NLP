"""
Author: Joshua Driscol
Date: 03.28.2019

Process a DAIC_WOZ transcript, convert the CSV file to a .txt file

The script depends on the following stardardized input format:
Columns: start_time, stop_time, speaker, value
-start_time, stop_time: these should correspond to only one speaker
-speaker: labelled "Ellie" and "Participant", although the only one that matters for processing is "Participant"
-value: this column **must** be labelled value
"""

import csv
import pandas as pd
import numpy as np
import os

this_dir = './'

for subdir, dirs, files in os.walk(this_dir):
	for file in files:
		if file.endswith('.csv'):
			#print(file)
			#NOTE: the filename should be constructed as 'num_TRANSCRIPT.csv'
			#save output file as the original name, but as a text file
			out_file_part = file.replace('.csv', '_part_raw.txt')         #participant only
			out_file_full = file.replace('.csv', '_full_raw.txt')   #full transcript

			#read in the CSV file as a dataframe, tab delimited
			df = pd.read_csv(file, delimiter='\t')

			#only select the rows that correspond to the participant's speech
			#or comment out the line below for the full transcript
			#df = df[df.speaker=='Participant']

			#discard all columns but the participant's speech, save as .txt file
			np.savetxt(out_file_full, df.value.values, fmt=['%s'])



