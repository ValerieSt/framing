import pandas as pd
import os

print("Compiling English corpus out of peace process related tweets...")
for name in ['santos', 'uribe']:
    filename = 'corpus_all-' + name + '.txt'
    print(filename)
    fout = open(filename, 'w')
    count = 0
    file = 'tweets_pp_translation-' + name + '.csv'
    df = pd.read_csv(file)
    total_rows = df.translation.count()
    for i in range(0, total_rows):
        tweet_en = df.translation[i]
        fout.write(str(tweet_en))
        textend = tweet_en[-1:]
        if any(c.isalpha() for c in textend):
            fout.write(". ")
        else:
            fout.write(" ")
        count = count + 1
    print("English version for ", name, " compiled out of ", str(count), "tweets")

print('Done compiling English corpora for the entire period.')
