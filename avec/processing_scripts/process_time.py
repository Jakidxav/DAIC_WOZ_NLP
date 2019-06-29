import csv
import pandas as pd
import numpy as np
import os

from clean_text import *
from process_pnums import *

"""
This helper method loops through all of the files in a directory and and calculates the total time per transcript of each participant. It needs to be passed a list to hold the participant numbers and the corresponding transcript time.

change_to_dir is the directory you want to change to holding either the training, development, or test sets, and the to_save parameter is the what you want the filename to be called.
"""

def time_per_transcript(change_to_dir, to_save, participant_nums, total_time):
	
        #change to correct directory
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
		
		#set keyword for correctly extracting participant number
		if filename.startswith('training'):
		    keyword = 'train'
		elif filename.startswith('develop'):
		    keyword = 'dev'
		else:
		    keyword = 'test'
		    
		#get participant number
		pnum = get_pnum(keyword)
		participant_nums.append(pnum)

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
	transcript_times = pd.DataFrame({'id': participant_nums,
		                         'total_time': total_time})

	#change to directory where all scripts and data are held
	os.chdir('../..')

	#then save features to csv
	transcript_times.to_csv(to_save, sep='\t')
