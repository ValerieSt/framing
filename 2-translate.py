
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.cloud import translate_v2 as translate
import pandas as pd
from pandas import DataFrame
import re

client = language.LanguageServiceClient()
translate_client = translate.Client()

old = pd.read_csv("tweets_pp.csv") #creates a dataframe from an existing csv file
new = old[['date', 'username', 'text', 'permalink']].copy() #creates a new dataframe taking defined columns from an existing dataframe
total_rows = new['text'].count()
count = 0

new.insert(3, 'translation', '-')
print('Translating tweets to English...')

for i in range(0, total_rows):
    try:
        text = new.text[i]
        translation = translate_client.translate(text, target_language='en')
        transl = translation['translatedText']
        transl = re.sub('&quot;', "\"", transl)
        transl = re.sub('&#39;', "\'", transl)
        new.translation[i] = transl
        count = count + 1
        if count == 100:
            print('100 done')
        if count == 1000:
            print('1000 done')
        if count == 3000:
            print('3000 done')
        if count == 4000:
            print('4000 done')

    except:
        continue

new.to_csv("tweets_pp_translation.csv")
print(count)
print('Done translating tweets.')
