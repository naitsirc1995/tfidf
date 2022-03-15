import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize


import string 
import os 

from nltk.stem.porter import PorterStemmer


def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = []

    for item in tokens:
        stems.append(PorterStemmer().stem(item))
    
    return " ".join(stems)     


def punctuation(text):    
    return text.lower().translate(str.maketrans('','',string.punctuation))
    
def stop_words(text,language = 'english'):
    stop_words = set(stopwords.words(language))
    final_words = []

    for word in word_tokenize(text):
        if word not in stop_words:
            final_words.append(word)
    
    return " ".join(final_words)



preprocess_dict = {
    'stem' : tokenize, 
    'punctuation' : punctuation,
    'stop_words' : stop_words
}


def pre_procesor(text , transforms_array):

    for transformation in transforms_array:        
        trasnformation_func = preprocess_dict[transformation]
        text = trasnformation_func(text)


    return text 
