"""
Author: Jakidxav
Date: 06.20.2019

File creates doc2vec vectors for analyzing the AVEC 2019 dataset. For the most part, this program follows the same setup as `create_frequency_vectors.py. However, for the ease creating word embeddings of a different type and then saving output I have made this its own file.
"""

import csv
import pandas as pd
import numpy as np
import os

from clean_text import *
from process_corpus_vectors import *

from gensim.models.doc2vec import Doc2Vec, TaggedDocument 

#change directory
train_text_dir_raw = './trainPart/raw/'
train_text_dir_with_i= './trainPart/cleaned_with_i'

dev_text_dir_raw = './devPart/raw/'
dev_text_dir_with_i= './devPart/cleaned_with_i'

#only process TXT files
file_ends_with = '.txt'

#save output with different filenames
to_save_train = 'X_train_raw_doc2vec.npy'
to_save_train_clean = 'X_train_i_doc2vec.npy'

to_save_dev = 'X_dev_raw_doc2vec.npy'
to_save_dev_clean = 'X_dev_i_doc2vec.npy'

#list to append each transcript to
docs = []

#we need the participant numbers to create TaggedDocument
participant_nums = []

#change these variables here:
chdir = train_text_dir_raw
to_save = to_save_train

#create doc2vec word embeddings here
document2vectors(docs, participant_nums, chdir, file_ends_with, to_save)
