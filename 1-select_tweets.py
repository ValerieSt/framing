import pandas as pd
import re
import string

df1 = pd.read_csv("output_got.csv") #uses the GetOldTweets3 Output file in a dataframe

fout = open('stats.txt', 'w') #creates a new file that let's me keep track of statistics
total_rows = df1['text'].count() #counts the total number of tweets from the GetOldTweets3 output file
fout.write('Total number of tweets: ')
fout.write(str(total_rows))
fout.write('\n')

df2 = pd.DataFrame(columns=['timedate', 'date', 'username', 'text', 'permalink']) #creates a new dataframe with the columns date, username, text and permalink (without rows yet)

def remove_hashtags(text):
    for i in range(0, 5):
        atpos = text.find('#')
        sppos = text.find(' ',atpos)
        hashtag = text[atpos:sppos]
        text = re.sub(str(hashtag), "", text)
    return text

def remove_mentions(text):
    for i in range(0, 5):
        atpos = text.find('@')
        sppos = text.find(' ',atpos)
        mention = text[atpos:sppos]
        text = re.sub(str(mention), "", text)
    return text



print('Selecting tweets that are likely related to the peace process & removing hashtags, mentions and URLs...')
count = 0
farccount = 0
colombiacount = 0
for i in range(0, total_rows): #goes through all tweets, strips them down (lower case etc.) and searches for keywords
    tweet = df1.text[i]
    tweet = tweet.rstrip()
    tweet = tweet.casefold()
    tweet = re.sub(r"http\S+", "", tweet)
    tweet = re.sub(r"pic.twitter\S+", "", tweet)
    if (tweet.find('farc') is not -1):
        farccount = farccount + 1
    if (tweet.find('farc') == -1 and tweet.find('paz') == -1 and tweet.find('guerra') == -1 and tweet.find('plebiscito') == -1 and tweet.find('decorazónvotono') == -1 and tweet.find('eldomingovotono') == -1 and tweet.find('todosavotarno') == -1 and tweet.find('eshoradevotarno') == -1 and tweet.find('votonoycorrijoacuerdos') == -1 and tweet.find('colombiadecideno') == -1 and tweet.find('hagahistoriavoteno') == -1 and tweet.find('conargumentosdigono') == -1 and tweet.find('encartagenadecimosno') == -1 and tweet.find('cartagenapitano') == -1 and tweet.find('colombiavotano') == -1 and tweet.find('mirazonparavotarno') == -1 and tweet.find('colombiaconelno') == -1 and tweet.find('todosporelno') == -1 and tweet.find('unidosporelno') == -1 and tweet.find('decimosnoalosacuerdos') == -1 and tweet.find('colombiasabedecirno') == -1 and tweet.find('digonoalosacuerdos') == -1 and tweet.find('yonometragoestesapo') == -1 and tweet.find('conozcalosacuerdos') == -1 and tweet.find('cartaaleyva') == -1 and tweet.find('cartapgn') == -1 and tweet.find('noindultoalterrorismo') == -1 and tweet.find('acuerdodeimpunidad') == -1 and tweet.find('conclusionesforocd') == -1 and tweet.find('noleyhabilitanteparasantos') == -1 and tweet.find('elpaisanuevohéroe') == -1 and tweet.find('resistenciacivil') == -1 and tweet.find('santosincentivaterrorismo') == -1 and tweet.find('ptesantosnovamosbien') == -1 and tweet.find('colombiasabedecirno') == -1 and tweet.find('decimosnoalosacuerdos') == -1 and tweet.find('mirazónparavotarno') == -1 and tweet.find('renegociemoslosacuerdos') == -1 and tweet.find('colombiavotano') == -1 and tweet.find('uribeargumentaporelno') == -1 and tweet.find('conargumentosdigono') == -1 and tweet.find('hagahistoriavoteno') == -1 and tweet.find('sigueelterrorismo') == -1 and tweet.find('quierolapazvotono') == -1 and tweet.find('colombiadecideno') == -1 and tweet.find('colombiadiceno') == -1 and tweet.find('votonoycorrijoacuerdos') == -1 and tweet.find('voteno') == -1 and tweet.find('eshoradevotarno') == -1 and tweet.find('colombiavota') == -1 and tweet.find('elpartidodelahistoria') == -1 and tweet.find('enlineaconelpresidente') == -1 and tweet.find('cesealfuegodefinitivo') == -1 and tweet.find('forodesminado') == -1 and tweet.find('findelconflicto') == -1 and tweet.find('fororeconciliación') == -1 and tweet.find('justiciaconlaup') == -1 and tweet.find('porlossobrevivientes') == -1):
        continue #if none of these terms are found in the text, go to the next tweet (row)
    if (tweet.find('farc') == -1 and tweet.find('eln') is not -1):
        continue #ignore lines that contain keywords above but seem linked to the ELN process rather than the FARC process


    else:
        if (tweet.find('colombia') is not -1):
            colombiacount = colombiacount + 1
        text = df1.text[i]
        if type(text) == 'NoneType':
            continue
        else:
            text = re.sub(r"http\S+", "", text)
            text = re.sub(r"pic.twitter\S+", "", text)
            try:
                text = remove_hashtags(text)
            except:
                pass
            try:
                text = remove_mentions(text)
            except:
                pass
            if len(text) < 10 is True:
                continue
            else:
                timedate = df1.date[i]
                date = timedate #this and next two lines create date out of twitter timestamp
                space = date.find(' ',0)
                date = date[0:space]
                username = df1.username[i]
                permalink = df1.permalink[i]
                df2 = df2.append({'timedate' : timedate, 'date' : date , 'username' : username , 'text' : text , 'permalink' : permalink} , ignore_index=True)
                count = count + 1
                print(text)

df2.to_csv("tweets_pp.csv")

fout.write('Total number of tweets likely related to the peace process: ')
fout.write(str(count))
fout.write('\n')
fout.write('Total number of tweets containing the word FARC: ')
fout.write(str(farccount))
fout.write('\n')
fout.write('Total number of tweets containing the word Colombia: ')
fout.write(str(colombiacount))
fout.write('\n')
print('Done selecting tweets.')
