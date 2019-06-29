"""
Author: Jakidxav
Date: 06.20.2019

Helper methods for creating frequency and doc2vec vector word embeddings for the AVEC 2019 challenge dataset.
"""

import csv
import pandas as pd
import numpy as np
import os

from clean_text import *
from process_pnums import *

from sklearn.feature_extraction.text import CountVectorizer
from gensim.models.doc2vec import Doc2Vec, TaggedDocument


"""
Create frequency vectors from a corpus, or a list of files in a directory.

Input a list to save each processed document to, and where the list of files are located.

- file_ends_with: here, I am inputing '.txt', so that the method only processes TXT files.
- dir_ends_with: use 'raw'; this means do one processing step for the raw data text files 	 before processing, or else do a different step for the cleaned text files before creating the word vectors
- to save: the filename for the frequency vectors

Generally, each time you run the script you should only have to change `chdir` and `to_save`.
"""

def frequency_vectors(docs_list, chdir, file_ends_with, dir_ends_with, to_save):
    
    #change to input directory
    change_dir = os.chdir(chdir)

    #get current working directory
    this_dir = os.getcwd()
    filenames = os.listdir(this_dir)

    #sort filenames for sorting vectors
    filenames = sorted(filenames)
    
    #need to iterate through documents
    #create a list of *strings*, each one containing the transcript of a participant
    for filename in filenames:
        if filename.endswith(file_ends_with):
            #read in file contents
            file = open(filename, 'rt')
            text = file.read()
            file.close()

            #if processing raw data, do the following two steps
            if this_dir.endswith(dir_ends_with):
                #whitespace tokenize
                tokens = tokenize(text)

                #convert back to string
                l2s = list_to_string(tokens)

            #else process cleaned data, replace linebreaks with spaces
            else:
                l2s = text.replace('\n', ' ')

            #append each transcript to docs list and use CountVectorizer
            docs_list.append(l2s)
            
            
    #instantiate our vectorizer
    #use if trying to include "i"
    vectorizer = CountVectorizer(analyzer='word', token_pattern='[a-zA-Z0-9]{1,}')
    #vectorizer = CountVectorizer()

    #fit to our list of transcripts, learn vocabulary
    #now we can use our vectorizer to generate vectors for each document
    vectors = vectorizer.fit_transform(docs_list).toarray()
        
    #change to directory where all scripts and data are held
    os.chdir('../..')

    #then save features to csv
    features_i.to_csv(to_save, sep='\t')



"""
Create doc2vec vectors from a corpus, or a list of files in a directory.

Input a list to save each processed document to, as well as a list of participant numbers, and where the list of files are located.

- file_ends_with: here, I am inputing '.txt', so that the method only processes TXT files.
- to save: the filename for the doc2vec word embeddings

Generally, each time you run the script you should only have to change `chdir` and `to_save`.
"""

def document2vectors(docs_list, pnums_list, chdir, file_ends_with, to_save):

    change_dir = os.chdir(chdir)

    #get current working directory
    this_dir = os.getcwd()
    filenames = os.listdir(this_dir)

    #sort filenames for sorting vectors
    filenames = sorted(filenames)

    #need to iterate through documents
    #create a list of *strings*, each one containing the transcript of a participant
    for filename in filenames:
        if filename.endswith(file_ends_with):
            #read in file contents
            file = open(filename, 'rt')
            text = file.read()
            file.close()
            
            #set keyword for correctly extracting participant number
            if filename.startswith('training'):
                keyword = 'train'
            elif filename.startswith('develop'):
                keyword = 'dev'
            else:
                keyword = 'test'
            
            #get participant number
            pnum = get_pnum(keyword)
            pnums_list.append(pnum)

            #whitespace tokenize
            tokens = tokenize(text)

            #create our list of lists, each list containing tokens in document
            docs_list.append(tokens)

    #create documents and tags 
    Documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(docs_list)]
    tags = [i for i, doc in enumerate(docs_list)]

    #create the model here
    #i am choosing min_count=1 here, because the majority of words seem to only occur once in file
    model = Doc2Vec(Documents, vector_size=100, window=10, min_count=1)

    #get document vectors
    docvecs = model.docvecs

    #now extract vectors from keyedvectors.Doc2VecKeyedVectors object
    vectors = []

    for i in tags:
        vectors.append(docvecs[i])

    #convert vectors list to array for saving, loading, and training
    vectors = np.array(vectors)
    
    #change to directory where all scripts and data are held
    os.chdir('../..')

    #then save features to csv
    features_i.to_csv(to_save, sep='\t')

