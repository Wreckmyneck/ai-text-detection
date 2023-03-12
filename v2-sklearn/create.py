# import functions 
import template

# import pacakages
import csv
import pickle
from os import system

# gets sklearn and needed packages
import sklearn 
from sklearn.naive_bayes import MultinomialNB

# get stopwords from nltk
"""
nltk.download(['stopwords'])
"""

system('clear')
print("Getting data...")

# how many lines are read and put into the model
DATACOUNT = 50000

# gets the data from the wiki
wikiDataWords, wikiDataResult = template.getWikiData(0, DATACOUNT)

# transforms data
wikiDataWords = template.vectorize(wikiDataWords)

# creates model
classifier = MultinomialNB()

system('clear')
print("Training model...")

# trains model
classifier.fit(wikiDataWords, wikiDataResult)

# saves model
with open('models/sklearnmodel.pkl', "wb") as f:
    pickle.dump(classifier, f)

system('clear')
print("Model saved.")