import os
import random
from nltk.probability import FreqDist
from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter
from nltk import NaiveBayesClassifier, classify
from sklearn.feature_extraction.text import CountVectorizer
import pickle

def get_data(directory):
    a_list=[]
    file_list=os.listdir(directory)
    #print(file_list)
    for file in file_list:
        try:
            f=open(directory+file,'r',encoding="utf8")
            #print(file)
            a_list.append(f.read())
            f.close()
        except UnicodeDecodeError:
            #print("exception\n")
            pass
    return a_list

spam=get_data('enron2/spam/')
ham=get_data('enron2/ham/')

all_emails=[(email,'spam') for email in spam]
all_emails+=[(email,'ham') for email in ham]
random.shuffle(all_emails)
print("a")
emails=[]

for word,value in all_emails:
    words_fitered=[e.lower() for e in word.split() if len(e)>2]
    emails.append((words_fitered,value))

save_all_emails=open("all_emails.pickle","wb")
pickle.dump(emails,save_all_emails)
save_all_emails.close()
print("b")
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
    classifier = NaiveBayesClassifier.train(train_set)
    return train_set, test_set, classifier

wordList=get_words_in_email(emails)
print("c")
wordFeatures=get_word_features(wordList)
Wfeatures=[k for k in wordFeatures]
save_all_features = open("word_features.pickle","wb")
pickle.dump(Wfeatures, save_all_features)
save_all_features.close()

print("d")
training_set = classify.apply_features(extract_features, emails)
print("e")
train_set, test_set, classifier = train(training_set, 0.8)
save_classifier = open("originalnaivebayes.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()
print ('Accuracy on the training set = ' + str(classify.accuracy(classifier, train_set)*100))
print ('Accuracy of the test set = ' + str(classify.accuracy(classifier, test_set)*100))

