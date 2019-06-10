"""

Author: Jakidxav
Date: 03.28.2019

Process a DAIC_WOZ transcript, convert the CSV file to a .txt file

The script depends on the following stardardized input format:

Columns: start_time, stop_time, speaker, value
- start_time, stop_time: these should correspond to only one speaker
- speaker: labelled "Ellie" and "Participant", although the only one that matters for processing is "Participant"
- value: this column **must** be labelled value
"""

import csv
import pandas as pd
import numpy as np
import os

#directories on disk
first_dir = './CSV_original/'
change_dir = '../../CSV_original/'

part_dir = '../Part/raw/'
ellie_dir = '../ellie/


#make sure directories exist; if not, create them
if os.path.isdir(part_dir) == False:
    os.makedirs(part_dir)

if os.path.isdir(ellie_dir) == False:
    os.makedirs(ellie_dir)

#boolean for rerouting output: participant = True for participant only, participant = False for full transcript
participant = False

#change to correct directory to start
os.chdir(first_dir)
this_dir = os.getcwd()


for subdir, dirs, files in os.walk(this_dir):
    for file in files:
        if file.endswith('.csv'):
            #NOTE: the filename should be constructed as 'num_TRANSCRIPT.csv'
            #save output file as the original name, but as a text file
            out_file_part = file.replace('.csv', '_part_raw.txt')      #participant only
            out_file_ellie = file.replace('.csv', '_ellie_raw.txt')      #full transcript

            #read in the CSV file as a dataframe, tab delimited
            df = pd.read_csv(file, delimiter='\t')

            #only select the rows that correspond to the participant's speech or select full transcript
            if participant == True:
                df = df[df.speaker=='Participant']
            else:
                #else do nothing
                df = df

            #discard all columns but the participant's speech, save as .txt file

            if participant == True:
                os.chdir(part_dir)
                #np.savetxt(out_file_part, df.value.values, fmt=['%s'])
            else:
                os.chdir(ellie_dir)
                np.savetxt(out_file_ellie, df.value.values, fmt=['%s'])

            #change back to input directory
            os.chdir(change_dir)
            this_dir = os.getcwd()
