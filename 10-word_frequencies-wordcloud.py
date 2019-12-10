from collections import Counter
import re
from wordcloud import WordCloud
wc = WordCloud(normalize_plurals=False, background_color="white", color_func=lambda *args, **kwargs: "black", max_font_size=120, random_state=42)
import matplotlib.pyplot as plt

fout = open("most_frequent_words.txt", "w")
for period_name in ['all-santos', 'noCF-santos', 'CF-santos', 'all-uribe', 'noCF-uribe', 'CF-uribe']:
    short = "corpus-lemma-" + str(period_name)
    filename = short + ".txt"
    words = re.findall(r'\w+', open(filename).read())
    fout.write(period_name)
    fout.write("\n")
    fout.write("\n")
    fout.write(str(Counter(words).most_common(300)))
    fout.write("\n")
    fout.write("\n")
    fout.write("\n")
    text = open(filename).read()
    wc.generate(text)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(short)
print('Most frequent words are in a textfile in your folder, wordclouds saved as graphs.')
