"""
Author: Jakidxav
Date: 04.13.2019

Wrapper methods for NLTK processing. These methods assume that nltk.download() has been run at least once.

Generally each method requires a list (or list of lists) and then returns a processed list.
"""

import string
import nltk
import spacy

#Input a document and receive a list of lists detailing individual word tokens.
#Note, this is a Whitespace tokenizer, which preserves contractions.
def tokenize(doc):

    return nltk.tokenize.WhitespaceTokenizer().tokenize(doc)



#Input a document and receive a list of lists detailing individual sentence tokens.
def sentence_tokenize(doc):

    return nltk.tokenize.sent_tokenize(doc)



#Input a string or document and output a list of tokens that has split contractions.
#Note, this is a WordPunct tokenizer, which splits apart contractions. However, the stopwords included in 
#NLTK should delete the split contractions if converted to lowercase.
def split_contractions(doc):

    return nltk.tokenize.wordpunct_tokenize(doc)



#Input a list of list containing tokenized document or corpus. Return all tokens if not of the format: [token] or <token>
#This is an attempt to remove semantic information that would skew training.
#NOTE: this should be done before removing punctuation, otherwise you will not find the correct tokens.
def remove_semantics(tokens):
    #first remove semantic information surrounded by brackets: []
    tokens =  [token for token in tokens if not token.startswith('[') and  not token.endswith(']')]
    #then remove semantic information surround by: <>
    return [token for token in tokens if not token.startswith('<') and  not token.endswith('>')]



#Input a tokenized text as a list of lists. 
#POS tag, and then return a list containing all tokens that are not proper nouns.
def remove_proper_nouns(tokens):
	pos = nltk.pos_tag(tokens)
	to_remove = ['NNP', 'NNPS']

	return [pos[0] for pos in pos if pos[1] not in to_remove]



#Input a list of tokens and output a single string
def list_to_string(tokens):
    string_ = ""
    whitespace = " "
    for token in tokens:
        string_ = string_ + token + whitespace
        
    return string_



#Convert all tokens to lowercase. Assumes that tokenizing has already occurred.
def lower_case(tokens):
     
    return [token.lower() for token in tokens]



#This method removes NLTK stopwords. Currently, this method works for English stopwords.
#More work can be done to input a "language" parameter to make it more customizable by language.
def remove_stopwords(tokens):
    #Create stopwords set for English.
    #This list can be modified in the english.txt file for NLTK, or use this syntax:
    # stopwords.extend(your_list_here)
    stopwords = nltk.corpus.stopwords.words('english')
    
    #add bad tokens into stopwords list
    stopwords.extend(['mmm', 'k', 'xxx'])

    #update stop words to keep certain words
    keep_list = ['uh', 'uhhh', 'um', 'ummm', 'i', "i'm", 'me', 'myself', 'mine', 'my',
                 'we', 'us', 'ourselves', 'ourself', 'ours', 'our', 'he', 'him', 'himself', 'his', 			 			'she', 'her', 'herself', 'hers', 'her', 'they', 'them', 'themselves', 'themself', 'theirs', 'their', 			'always', 'nothing', 'completely', 'never', 'all', 'every', 'none', 'only']

    stopwords = [word for word in stopwords if word not in keep_list]
    stops = set(stopwords)

    return [token for token in tokens if token not in stops]



#Remove punctuation and replace it with an empty string character.
#Example: can't --> cant
def strip_punctuation(tokens):
    #Create punctuation list: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    punctuation = string.punctuation

    #See docs: str.maketrans() will make a table to pass to str.translate()
    table = str.maketrans('', '', string.punctuation)

    return [token.translate(table) for token in tokens]



#Strip any non-alphabetic characters.
def remove_numbers(tokens):
    return [token for token in tokens if token.isalpha()]



#Input a list of tokens, output a list of tokens minus people and places.
#NOTE: SpaCy's entity recognition should be done before converting tokens to lowercase, and at this time
#does not recognize lowercase entities. So it will recognize United States, but not UNITED STATES or united states. Likewise, it may recognize Sarah and SARAH, but not sarah.
def remove_people_places(doc):
    nlp = spacy.load('en')
    
    document = list_to_string(doc)
    document = nlp(document)
    
    #create list of removable words
    ppl_plcs = ['PERSON', 'GPE']
    to_remove = [ent.text for ent in document.ents if ent.label_ in ppl_plcs]
    
    #now remove those words and 
    return [token for token in doc if token not in to_remove]



#Input a file that has text on separate lines (separated by breakline characters or otherwise).
#Output number of lines in that file.
def count_sentences(filename):
    sentences = 0

    doc = open(filename, 'rt')

    for line in doc:
        sentences += 1

    doc.close()

    return sentences



#Input a custom list of words you would like to count in a list of tokenized words.
#Outputs the total count of the words in your_list based on the frequency in tokens.
def list_in_text(your_list, tokens):
    count = 0

    for word in your_list:
        for token in tokens:
            if token == word:
                count += 1

    return count


