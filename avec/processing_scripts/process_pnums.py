"""
Author: Jakidxav
Date: 06.28.2019

This code is used by a variety of processing steps, so I am making it its own helper method.

Participant numbers will differ in placement between training, development, and test sets. We can run this method to correctly save the participant number to organize our feature dataframes.
"""

def get_pnum(keyword, filename):
#training set files start with "training_", development set files start with "developement_", and
#testing set files start with "test_"
    if keyword == 'train':
        pnum = int(filename[9:12])

    elif keyword == 'dev':
        pnum = int(filename[12:14])

    else:
        pnum = int(filename[5:7])

    return pnum

