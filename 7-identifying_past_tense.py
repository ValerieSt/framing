import spacy
import pandas as pd
from pandas import DataFrame
import os
nlp = spacy.load("en_core_web_sm")

def pastcount(text):
    '''estimating the percentage of sentences that are in past tense, i.e. sentences where either the root of the sentence is a verb in past simple, or one of the dependency children of the root is an auxiliary verb in past simple.'''
    sentencecount = 0
    pastcount = 0

    df_temp = DataFrame(columns = ['sentencecount', 'pastcount'])
    for sent in doc.sents:
        if len(sent) < 10: #ignoring sentences with less than 10 characters, as they will likely have been misidentified as sentences (e.g. numbering, etc.)
            continue
        else:
            sentencecount = sentencecount + 1
            pastform = 0
            dependencies = list(sent.root.children)
            for word in sent:
                if sent.root.tag_ == 'VBD': #if the root verb of the sentence is past tense
                    pastform = pastform + 1
                else:
                    if word in dependencies:
                        if word.dep_ == 'aux' and word.tag_ == 'VBD':
                            pastform = pastform + 1

            if pastform is not 0:
                pastcount = pastcount + 1
                print(sent)
    df_temp = df_temp.append({'sentencecount' : sentencecount, 'pastcount' : pastcount} , ignore_index=True)
    df_temp.to_csv("df_temp.csv")

for name in ['santos', 'uribe']:
    for period in ['_all', '_noCF', '_CF']:
        filename = "corpus" + str(period) + "-" + str(name) + ".txt"
        corpus = open(filename).read()
        doc = nlp(corpus)
        pastcount(doc)
        outputname = "corpus" + str(period) + "-" + str(name) + "-past-stats.csv"
        os.rename('df_temp.csv', outputname)

df = pd.DataFrame(columns=['name', 'period', 'sentencecount', 'pastcount', 'percentage']) #creates a new dataframe with the columns name, period, sentencecount, pastcount, percentage (without rows yet

for name in ['santos', 'uribe']:
    for period in ['_all', '_noCF', '_CF']:
        filename = "corpus" + str(period) + "-" + str(name) + "-past-stats.csv"
        data = pd.read_csv(filename)
        sentencecount = data.sentencecount[0]
        pastcount = data.pastcount[0]
        percentage = int(pastcount)/int(sentencecount)
        percentage = '{:.0%}'.format(percentage)
        df = df.append({'name' : name, 'period' : period, 'sentencecount' : sentencecount, 'pastcount' : pastcount, 'percentage' : percentage} , ignore_index=True)
        os.remove(filename)

df.to_csv("stats-past_tense.csv")
print('Done.')
