from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.cloud import translate_v2 as translate
import pandas as pd
from pandas import DataFrame
import re
import os

client = language.LanguageServiceClient()
translate_client = translate.Client()

old = pd.read_csv("tweets_pp_translation.csv") #creates a dataframe from an existing csv file
new = old.copy() #creates a new dataframe taking defined columns from an existing dataframe
total_rows = new['text'].count()
count = 0
failed = 0

print('Idenfifying tweets that had not yet been translated and translating them...')

for i in range(0, total_rows):
    if new.translation[i] == '-':
        try:
            text = new.text[i]
            translation = translate_client.translate(text, target_language='en')
            transl = translation['translatedText']
            transl = re.sub('&quot;', "\"", transl)
            transl = re.sub('&#39;', "\'", transl)
            new.translation[i] = transl
            count = count + 1
        except:
            failed = failed + 1

print(count, ' additional translations done')
print('Failed to translate ', failed, ' tweets')
os.remove('tweets_pp_translation.csv')
new.to_csv("tweets_pp_translation.csv")
print('Your revised file is in your folder.')
