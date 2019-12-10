import os
import shutil

os.makedirs('corpora-santos')
os.makedirs('corpora-uribe')
os.makedirs('tweets')
os.makedirs('graphs')
os.makedirs('stats')

path = os.getcwd()

#moving around corpora
shutil.move(path + "/corpus_all-santos.txt", path + '/corpora-santos')
shutil.move(path + "/corpus_noCF-santos.txt", path + '/corpora-santos')
shutil.move(path + "/corpus_CF-santos.txt", path + '/corpora-santos')
shutil.move(path + "/corpus-lemma-all-santos.txt", path + '/corpora-santos')
shutil.move(path + "/corpus-lemma-noCF-santos.txt", path + '/corpora-santos')
shutil.move(path + "/corpus-lemma-CF-santos.txt", path + '/corpora-santos')


shutil.move(path + "/corpus_all-uribe.txt", path + '/corpora-uribe')
shutil.move(path + "/corpus_noCF-uribe.txt", path + '/corpora-uribe')
shutil.move(path + "/corpus_CF-uribe.txt", path + '/corpora-uribe')
shutil.move(path + "/corpus-lemma-all-uribe.txt", path + '/corpora-uribe')
shutil.move(path + "/corpus-lemma-noCF-uribe.txt", path + '/corpora-uribe')
shutil.move(path + "/corpus-lemma-CF-uribe.txt", path + '/corpora-uribe')


#moving around graphs

shutil.move(path + "/corpus-lemma-all-santos.png", path + '/graphs')
shutil.move(path + "/corpus-lemma-noCF-santos.png", path + '/graphs')
shutil.move(path + "/corpus-lemma-CF-santos.png", path + '/graphs')
shutil.move(path + "/corpus-lemma-all-uribe.png", path + '/graphs')
shutil.move(path + "/corpus-lemma-noCF-uribe.png", path + '/graphs')
shutil.move(path + "/corpus-lemma-CF-uribe.png", path + '/graphs')



#moving around stats files

shutil.move(path + "/stats-future_tense.csv", path + '/stats')
shutil.move(path + "/stats-past_tense.csv", path + '/stats')
shutil.move(path + "/stats-noCF-vs-CF-periods.txt", path + '/stats')
shutil.move(path + "/stats-santos.txt", path + '/stats')
shutil.move(path + "/stats-uribe.txt", path + '/stats')
shutil.move(path + "/most_frequent_words.txt", path + '/stats')



#moving around tweet files

shutil.move(path + "/tweets_pp_translation-santos.csv", path + '/tweets')
shutil.move(path + "/tweets_pp_translation-uribe.csv", path + '/tweets')
shutil.move(path + "/tweets_pp-santos.csv", path + '/tweets')
shutil.move(path + "/tweets_pp-uribe.csv", path + '/tweets')
shutil.move(path + "/output_got-santos.csv", path + '/tweets')
shutil.move(path + "/output_got-uribe.csv", path + '/tweets')

print('Done. All your files are in folders.')
