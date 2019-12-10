import spacy
import pandas as pd
import os
nlp = spacy.load("en_core_web_sm")
from pandas import DataFrame


def futurecount(text):
    '''estimating the percentage of sentences that are in future tense, i.e. where the sentence contains the modal auxiliary 'will' or 'shall' '''
    sentencecount = 0
    futurecount = 0

    df_temp = DataFrame(columns = ['sentencecount', 'futurecount'])

    for sent in doc.sents:
        if len(sent) < 10: #ignoring sentences with less than 10 characters, as they will likely have been misidentified as sentences (e.g. numbering, etc.)
            continue
        else:

            sentencecount = sentencecount + 1
            auxcount = 0
            for word in sent:
                if word.dep_ == 'aux':
                    if word.text in ['will', 'shall']:
                        auxcount = auxcount + 1
            if auxcount is not 0:
                futurecount = futurecount + 1
                print(sent)

    df_temp = df_temp.append({'sentencecount' : sentencecount, 'futurecount' : futurecount} , ignore_index=True)
    df_temp.to_csv("df_temp.csv")

for name in ['santos', 'uribe']:
    for period in ['_all', '_noCF', '_CF']:
        filename = "corpus" + str(period) + "-" + str(name) + ".txt"
        corpus = open(filename).read()
        doc = nlp(corpus)
        futurecount(doc)
        outputname = "corpus" + str(period) + "-" + str(name) + "-future-stats.csv"
        os.rename('df_temp.csv', outputname)

df = pd.DataFrame(columns=['name', 'period', 'sentencecount', 'futurecount', 'percentage']) #creates a new dataframe with the columns name, period, sentencecount, futurecount, percentage (without rows yet

for name in ['santos', 'uribe']:
    for period in ['_all', '_noCF', '_CF']:
        filename = "corpus" + str(period) + "-" + str(name) + "-future-stats.csv"
        data = pd.read_csv(filename)
        sentencecount = data.sentencecount[0]
        futurecount = data.futurecount[0]
        percentage = int(futurecount)/int(sentencecount)
        percentage = '{:.0%}'.format(percentage)
        df = df.append({'name' : name, 'period' : period, 'sentencecount' : sentencecount, 'futurecount' : futurecount, 'percentage' : percentage} , ignore_index=True)
        os.remove(filename)

df.to_csv("stats-future_tense.csv")
print('Done.')
