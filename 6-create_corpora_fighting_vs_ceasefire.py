
import pandas as pd
import os
from datetime import date

statsfile = open('stats-noCF-vs-CF-periods.txt', 'w')
print('Compiling corpus for Santos during fighting periods')
fout = open('corpus_noCF-santos.txt', 'w')
count = 0

noCFdaycount = 0
for period in ['1', '3', '5', '7', '9', '11']:

    if period == '1':
        start = '2012-08-26'
        end = '2012-11-18'
    if period == '2':
        start = '2012-11-18'
        end = '2013-01-18'
    if period == '3':
        start = '2013-01-18'
        end = '2013-12-07'
    if period == '4':
        start = '2013-12-07'
        end = '2014-01-07'
    if period == '5':
        start = '2014-01-07'
        end = '2014-05-19'
    if period == '6':
        start = '2014-05-19'
        end = '2014-05-28'
    if period == '7':
        start = '2014-05-28'
        end = '2014-06-08'
    if period == '8':
        start = '2014-06-08'
        end = '2014-06-30'
    if period == '9':
        start = '2014-06-30'
        end = '2014-12-19'
    if period == '10':
        start = '2014-12-19'
        end = '2015-05-20'
    if period == '11':
        start = '2015-05-20'
        end = '2015-07-19'
    if period == '12':
        start = '2015-07-19'
        end = '2016-10-02'

    startyear = start[0:4]
    startmonth = start[5:7]
    startday = start[8:]
    if startmonth[0:1] == "0":
        startmonth = startmonth[1:2]
    if startday[0:1] == "0":
        startday = startday[1:2]
    endyear = end[0:4]
    endmonth = end[5:7]
    endday = end[8:]
    if endmonth[0:1] == "0":
        endmonth = endmonth[1:2]
    if endday[0:1] == "0":
        endday = endday[1:2]

    delta = date(int(endyear), int(endmonth), int(endday)) - date(int(startyear), int(startmonth), int(startday))
    noCFdaycount = noCFdaycount + delta.days
    data = pd.read_csv('tweets_pp_translation-santos.csv')
    total_tweets = data.text.count()
    mask = (data['date'] > start) & (data['date'] <= end)
    df = data.loc[mask]
    df.to_csv("df.csv")
    df = pd.read_csv("df.csv")
    total_rows = df.text.count()

    for i in range(0, total_rows):
        tweet_en = df.translation[i]
        fout.write(str(tweet_en))
        textend = tweet_en[-1:]
        if any(c.isalpha() for c in textend):
            fout.write(". ")
        else:
            fout.write(" ")
        count = count + 1
    os.remove("df.csv")


print(str(count), ' tweets included in corpus Santos no CF')

statsfile.write("\n")
statsfile.write("Santos total pp related tweets: ")
statsfile.write(str(total_tweets))
statsfile.write("\n")
statsfile.write(str(count))
statsfile.write(" during fighting")
statsfile.write("\n")



print('Compiling corpus for Santos during ceasefire periods')

fout = open('corpus_CF-santos.txt', 'w')
count = 0
CFdaycount = 0
for period in ['2', '4', '6', '8', '10', '12']:

    if period == '1':
        start = '2012-08-26'
        end = '2012-11-18'
    if period == '2':
        start = '2012-11-18'
        end = '2013-01-18'
    if period == '3':
        start = '2013-01-18'
        end = '2013-12-07'
    if period == '4':
        start = '2013-12-07'
        end = '2014-01-07'
    if period == '5':
        start = '2014-01-07'
        end = '2014-05-19'
    if period == '6':
        start = '2014-05-19'
        end = '2014-05-28'
    if period == '7':
        start = '2014-05-28'
        end = '2014-06-08'
    if period == '8':
        start = '2014-06-08'
        end = '2014-06-30'
    if period == '9':
        start = '2014-06-30'
        end = '2014-12-19'
    if period == '10':
        start = '2014-12-19'
        end = '2015-05-20'
    if period == '11':
        start = '2015-05-20'
        end = '2015-07-19'
    if period == '12':
        start = '2015-07-19'
        end = '2016-10-02'

    startyear = start[0:4]
    startmonth = start[5:7]
    startday = start[8:]
    if startmonth[0:1] == "0":
        startmonth = startmonth[1:2]
    if startday[0:1] == "0":
        startday = startday[1:2]
    endyear = end[0:4]
    endmonth = end[5:7]
    endday = end[8:]
    if endmonth[0:1] == "0":
        endmonth = endmonth[1:2]
    if endday[0:1] == "0":
        endday = endday[1:2]

    delta = date(int(endyear), int(endmonth), int(endday)) - date(int(startyear), int(startmonth), int(startday))
    CFdaycount = CFdaycount + delta.days

    data = pd.read_csv('tweets_pp_translation-santos.csv')
    mask = (data['date'] > start) & (data['date'] <= end)
    df = data.loc[mask]
    df.to_csv("df.csv")
    df = pd.read_csv("df.csv")
    total_rows = df.text.count()

    for i in range(0, total_rows):
        tweet_en = df.translation[i]
        fout.write(str(tweet_en))
        textend = tweet_en[-1:]
        if any(c.isalpha() for c in textend):
            fout.write(". ")
        else:
            fout.write(" ")
        count = count + 1
    os.remove("df.csv")
print(str(count), ' tweets included in corpus Santos CF')


statsfile.write(str(count))
statsfile.write(" during CF")
statsfile.write("\n")
statsfile.write("\n")
statsfile.write("\n")
print('Compiling corpus for Uribe during fighting periods')
fout = open('corpus_noCF-uribe.txt', 'w')
count = 0

for period in ['1', '3', '5', '7', '9', '11']:

    if period == '1':
        start = '2012-08-26'
        end = '2012-11-18'
    if period == '2':
        start = '2012-11-18'
        end = '2013-01-18'
    if period == '3':
        start = '2013-01-18'
        end = '2013-12-07'
    if period == '4':
        start = '2013-12-07'
        end = '2014-01-07'
    if period == '5':
        start = '2014-01-07'
        end = '2014-05-19'
    if period == '6':
        start = '2014-05-19'
        end = '2014-05-28'
    if period == '7':
        start = '2014-05-28'
        end = '2014-06-08'
    if period == '8':
        start = '2014-06-08'
        end = '2014-06-30'
    if period == '9':
        start = '2014-06-30'
        end = '2014-12-19'
    if period == '10':
        start = '2014-12-19'
        end = '2015-05-20'
    if period == '11':
        start = '2015-05-20'
        end = '2015-07-19'
    if period == '12':
        start = '2015-07-19'
        end = '2016-10-02'

    data = pd.read_csv('tweets_pp_translation-uribe.csv')
    total_tweets = data.text.count()
    mask = (data['date'] > start) & (data['date'] <= end)
    df = data.loc[mask]
    df.to_csv("df.csv")
    df = pd.read_csv("df.csv")
    total_rows = df.text.count()

    for i in range(0, total_rows):
        tweet_en = df.translation[i]
        fout.write(str(tweet_en))
        textend = tweet_en[-1:]
        if any(c.isalpha() for c in textend):
            fout.write(". ")
        else:
            fout.write(" ")
        count = count + 1
    os.remove("df.csv")
print(str(count), ' tweets included in corpus Uribe no CF')

statsfile.write("Uribe total pp related tweets: ")
statsfile.write(str(total_tweets))
statsfile.write("\n")
statsfile.write(str(count))
statsfile.write(" during fighting")
statsfile.write("\n")


print('Compiling corpus for Uribe during ceasefire periods')

fout = open('corpus_CF-uribe.txt', 'w')
count = 0

for period in ['2', '4', '6', '8', '10', '12']:

    if period == '1':
        start = '2012-08-26'
        end = '2012-11-18'
    if period == '2':
        start = '2012-11-18'
        end = '2013-01-18'
    if period == '3':
        start = '2013-01-18'
        end = '2013-12-07'
    if period == '4':
        start = '2013-12-07'
        end = '2014-01-07'
    if period == '5':
        start = '2014-01-07'
        end = '2014-05-19'
    if period == '6':
        start = '2014-05-19'
        end = '2014-05-28'
    if period == '7':
        start = '2014-05-28'
        end = '2014-06-08'
    if period == '8':
        start = '2014-06-08'
        end = '2014-06-30'
    if period == '9':
        start = '2014-06-30'
        end = '2014-12-19'
    if period == '10':
        start = '2014-12-19'
        end = '2015-05-20'
    if period == '11':
        start = '2015-05-20'
        end = '2015-07-19'
    if period == '12':
        start = '2015-07-19'
        end = '2016-10-02'

    data = pd.read_csv('tweets_pp_translation-uribe.csv')
    mask = (data['date'] > start) & (data['date'] <= end)
    df = data.loc[mask]
    df.to_csv("df.csv")
    df = pd.read_csv("df.csv")
    total_rows = df.text.count()

    for i in range(0, total_rows):
        tweet_en = df.translation[i]
        fout.write(str(tweet_en))
        textend = tweet_en[-1:]
        if any(c.isalpha() for c in textend):
            fout.write(". ")
        else:
            fout.write(" ")
        count = count + 1
    os.remove("df.csv")
print(str(count), ' tweets included in corpus Uribe CF')

statsfile.write(str(count))
statsfile.write(" during ceasefire")
statsfile.write("\n")
statsfile.write("\n")
statsfile.write("\n")
statsfile.write("\n")
totaldays = noCFdaycount + CFdaycount
statsfile.write(str(totaldays))
statsfile.write(" days in entire period")
statsfile.write("\n")
statsfile.write(str(noCFdaycount))
statsfile.write(" days of fighting")
statsfile.write("\n")
statsfile.write(str(CFdaycount))
statsfile.write(" days of ceasefire")
statsfile.write("\n")

print('Done compiling.')
