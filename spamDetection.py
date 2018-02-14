import os
import random
from nltk.probability import FreqDist
from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter
from nltk import NaiveBayesClassifier, classify
from sklearn.feature_extraction.text import CountVectorizer
import pickle

def get_words_in_email(emails):
    all_words=[]
    for words,value in emails:
        all_words.extend(words)
    return all_words

def get_word_features(wordList):
    wordList=FreqDist(wordList)
    word_features=wordList.keys()
    return word_features

def extract_features(document):
    document_words=set(document)
    features={}
    for word in Wfeatures:
        features['contains(%s)' % word] = (word in document_words)
    return features

def train(features, samples_proportion):
    train_size = int(len(features) * samples_proportion)
    train_set, test_set = features[:train_size], features[train_size:]
    print ('Training set size = ' + str(len(train_set)) + ' emails')
    print ('Test set size = ' + str(len(test_set)) + ' emails')
    return train_set, test_set

all_emailsf=open("all_emails.pickle","rb")
emails=pickle.load(all_emailsf)
all_emailsf.close()

word_featuresf=open("word_features.pickle","rb")
Wfeatures=pickle.load(word_featuresf)
word_featuresf.close()

training_set = classify.apply_features(extract_features, emails)
train_set, test_set = train(training_set, 0.8)
#print(train_set[0])
classifierf=open("originalnaivebayes.pickle","rb")
classifier=pickle.load(classifierf)
classifierf.close()

def spamOrHam(text):
    a=[e.lower() for e in text.split()]
    feats = extract_features(a)
    return classifier.classify(feats),classifier.show_most_informative_features(15)
