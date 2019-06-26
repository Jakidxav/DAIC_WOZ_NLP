import csv
import pandas as pd
import numpy as np
import os

from clean_text import *


"""
Here we are inputing the CSV that contains our positive and negative words list, and outputing a cleaned and extended word lists. At the end of the script, you can customize further words that you would like to end to each word list. I have included some that I felt were lacking in my analysis.
"""
def process_pos_neg_file(filename):
    #let's read in the spreadsheet, and then save the word lists
    df = pd.read_excel(filename)

    #right now we have all word lists, we need to isolate just the positive and negative words
    df = df[['Entry', 'Positiv', 'Negativ', 'PosAff', 'NegAff']]

    #we need to get rid of nan values, only take explicitly labeled data
    positive = df['Entry'][df['Positiv']=='Positiv']
    positive.dropna(inplace=True)

    negative = df['Entry'][df['Negativ']=='Negativ']
    negative.dropna(inplace=True)

    pos_aff = df['Entry'][df['PosAff']=='PosAff']
    pos_aff.dropna(inplace=True)

    neg_aff = df['Entry'][df['NegAff']=='NegAff']
    neg_aff.dropna(inplace=True)

    #we should also convert each word list to lowercase
    #and the pandas series object to a list
    positive = positive.str.lower().tolist()
    negative = negative.str.lower().tolist()
    pos_aff = pos_aff.str.lower().tolist()
    neg_aff = neg_aff.str.lower().tolist()

    #let's check the shapes
    #according to the website, there are 1915 pos, 2291 neg
    len_pos = len(positive)
    len_neg = len(negative)

    #we can combine the word list for positive and pos_aff, 
    #and do the same thing for negative and neg_aff
    positive.extend(pos_aff)
    negative.extend(neg_aff)

    #now convert to a set to remove any duplicates
    positive = list(set(positive))
    negative = list(set(negative))

    #let's add in good, great, love, happy, and like
    positive.append('good')
    positive.append('great')
    positive.append('love')
    positive.append('happy')
    positive.append('like')

    #and now depressed, tired, bored, alone, plus some others
    negative.append('depressed')
    negative.append('tired')
    negative.append('bored')
    negative.append('alone')
    negative.append('annoying')
    negative.append('irritate')
    negative.append('irritated')
    negative.append('bother')
    negative.append('bothered')

    return positive, negative


"""
This helper method loops through all of the files in a directory and uses the positive and negative words lists output by process_pos_neg_file() above. It then creates a frequency dictionary, and saves the output as a CSV file with the participant number as the index.

Input the directory that you would like to change to as well as the name of the file you would like to save the output to. The "keyword" argument is well-documented below. 
"""
def positive_negative_counts(change_to_dir, keyword, to_save, positive, negative):
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
        if filename.endswith('.txt'):
            #read in file contents
            file = open(filename, 'rt')
            text = file.read()
            file.close()

            #participant numbers will differ in placement between training and development sets
            #training set files start with "training_", and development set files start with "developement_"
            if keyword == 'train':
                participant_nums.append(int(filename[9:12]))
            else:
                participant_nums.append(int(filename[12:14]))

            #whitespace tokenize
            tokens = tokenize(text)

            #append tokens to document list
            docs.append(tokens)

            #count positive words unions
            pos_in_tokens = list(set(positive) & set(tokens))
            pos.append(len(pos_in_tokens))

            #do the same for negative words
            neg_in_tokens = list(set(negative) & set(tokens))
            neg.append(len(neg_in_tokens))

            #now let's look at positive and negative word *frequency*, not count
            count_pos = 0
            count_neg = 0
            for word in tokens:
                if word in pos_in_tokens:
                    count_pos += 1
                if word in neg_in_tokens:
                    count_neg += 1

            pos_freq.append(count_pos)
            neg_freq.append(count_neg)

    #now let's create a dataframe object and save it as a csv
    dataframe = pd.DataFrame({'part_num':participant_nums,
                             'num_pos':pos,
                             'num_neg':neg, 
                             'pos_freq':pos_freq,
                             'neg_freq':neg_freq})

    #change to main directory, save as a csv
    os.chdir('../../')
    dataframe.to_csv(to_save)
