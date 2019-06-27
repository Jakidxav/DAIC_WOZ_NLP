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

#lists to append each transcript feature to
#append participant number from filename for indexing
participant_num = []

#count total time per transcript
total_time = []

#change directory
change_dir_train = './train/'
change_dir_dev = './dev/'

to_save_train = './transcript_times_train.csv'
to_save_dev = './transcript_times_dev.csv'

###change values here to redirect output
change_to_dir = change_dir_dev

#for extracting participant numbers correctly
keyword = 'dev'

#filename to save to
to_save = to_save_dev
###

change_dir = os.chdir(change_to_dir)

#get current working directory
this_dir = os.getcwd()
filenames = os.listdir(this_dir)

#sort filenames for sorting vectors
filenames = sorted(filenames)


#need to iterate through documents
#create a list of *strings*, each one containing the transcript of a participant
for filename in filenames:
    if filename.endswith('.csv'):
        
        #participant numbers will differ in placement between training and development sets
        #training set files start with "training_", and development set files start with "developement_"
        if keyword == 'train':
            participant_num.append(int(filename[9:12]))
        else:
            participant_num.append(int(filename[12:14]))
            
        #read in tab-delimited files
        df = pd.read_csv(filename)

        #drop unnecessary columns
        df.drop(['Text', 'Confidence'], axis=1, inplace=True)

        #create time difference column
        df['time_per_sent'] = df.End_Time - df.Start_Time

        #get total transcript time in minutes
        #rounded to five decimal places
        time = np.round((df.time_per_sent.sum() / 60.0), 5)

        total_time.append(time)
        
        
#create dataframe of transcript times for EDA later on
transcript_times = pd.DataFrame({'id': participant_num,
                                 'total_time': total_time})

transcript_times.to_csv(to_save, sep='\t')
