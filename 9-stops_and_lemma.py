# Creates a clean corpus without stopwords, and with all words lemmatized

import pandas as pd
import re
import string
import nltk
from nltk.corpus import stopwords
import os
import spacy

for period_name in ['all-santos', 'noCF-santos', 'CF-santos', 'all-uribe', 'noCF-uribe', 'CF-uribe']:
    file = "corpus_" + str(period_name) + ".txt"
    text = open(file, 'r').read()
    #'''Make text lowercase, remove punctuation, remove words containing numbers, remove stop words.'''
    text = text.lower() #make text lowercase
    text = re.sub('&#39;', '', text) #remove additional punctation
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text) #remove punctation
    text = re.sub('\w*\d\w*', '', text) #remove words containing numbers
    text = re.sub('[‘’“”…]', '', text) #remove additional puncation
    text = re.sub('\n', '', text) #remove additional punctation
    text = re.sub('&quot;', '', text) #remove additional punctation
    text = re.sub('quot', '', text) #remove additional punctation
    text = re.sub('#', '', text) #removes hashtags
    text = re.sub('guerra', 'war', text) #missed translations
    text = re.sub('paz ', 'peace ', text) #missed translations
    #removing stopwords
    text = ' '.join([word for word in text.split() if word not in (stopwords.words('english'))])
    #Lemmatizing all words
    nlp = spacy.load('en_core_web_sm')
    count = 0
    output = "corpus-lemma-" + str(period_name) + ".txt"
    fout = open(output, 'w+')
    doc = nlp(text)
    count = 0
    out_sent = [w.lemma_ if w.lemma_ !='-PRON-' else w.text for w in doc]
    out_sent = ' '.join(out_sent)
    out_sent = re.sub('santo ', "santos ", out_sent) #corrects for falsly lemmatized version of Santos
    print(out_sent)
    fout.write(out_sent + '\n')
    print(count)
    fout.close()

print('Done. Your lemmatized corpora are in your folder')
