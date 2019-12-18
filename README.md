# framing
Code used in academic paper on elite framing of peace negotiations


README

Here are some steps that you will need to go through before running the scripts. 

1. Download all code files to a folder destination on your computer

2. Make sure Python3 is installed on your computer.

Python 3.7 is recommended.

3. Install the required packages.

For the analysis, you will need the following packages:

pandas
spacy
matplotlib
nltk
google.cloud
wordcloud


From nltk, download 'stopwords' (nltk.download('stopwords’))
From spacy, download ‘en_core_web_sm’ (python -m spacy download en_core_web_sm)

Note: pandas, spacy, Matplotlib and nltk can be installed through Anaconda 

4. Set up your authentication for the Google Natural Language API Client Libraries.

See here: https://cloud.google.com/natural-language/docs/reference/libraries#client-libraries-install-python

If you do not want to set up a Google Cloud account, you may change the code in the translation file (2-translate.py) to use another translation service.

5. Copy your Google authentication credentials into the shell file.

In the shell file (0-run_scripts.sh), replace the string [PATH] with the path to the file that contains the service account key, including the filename. See here: https://cloud.google.com/natural-language/docs/reference/libraries#client-libraries-install-python for instructions.

6. Make sure you are connected to the internet.

7. Run the shell
On a mac, you can run the shell file in your terminal. Make sure you are in the right file directory, type “sh”, drag and drop the shell file into the terminal, and press enter.

For questions, please contact the author at sticher@sipo.gess.ethz.ch

Important note: The results may change over time as the NLP libraries and models evolve. The findings, as presented in the paper, were done with the code run on 7 December 2019.
