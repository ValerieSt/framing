#!/bin/(shell)
export GOOGLE_APPLICATION_CREDENTIALS=[PATH] #Replace the string [path] with your path to the JSON file that contains your service account key, and the filename. The path should look something like this: "/home/user/Downloads/[FILENAME].json"
GetOldTweets3 --username "juanmansantos" --since 2012-08-27 --until 2016-10-03 --maxtweets 0
python3 1-select_tweets.py
python3 2-translate.py
python3 3-complete_translation.py
python3 3-complete_translation.py
python3 4a-rename.py
GetOldTweets3 --username "AlvaroUribeVel" --since 2012-08-27 --until 2016-10-03 --maxtweets 0
python3 1-select_tweets.py
python3 2-translate.py
python3 3-complete_translation.py
python3 3-complete_translation.py
python3 4b-rename.py
python3 5-create_corpora_entire_period.py
python3 6-create_corpora_fighting_vs_ceasefire.py
python3 7-identifying_past_tense.py
python3 8-identifying_future_tense.py
python3 9-stops_and_lemma.py
python3 10-word_frequencies-wordcloud.py
python3 11-create_order.py
