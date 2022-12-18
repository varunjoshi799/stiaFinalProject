import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from format import split_into_sentences
from nltk import ngrams
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from stopwords import stopWords
from format import formatDataset
from stemmer import stemWords
from ngrams import createbigrams

def main (file1, fileName, type):
    stopWords(file1, fileName)
    formatDataset("stiaFinalProject/Data/Stopped/" + fileName + ".txt", fileName)
    stemWords("stiaFinalProject/Data/Formatted/" + fileName + ".txt", fileName)
    createbigrams("stiaFinalProject/Data/Stemmed/" + fileName + ".txt", fileName, type)


main("stiaFinalProject/Data/Raw/rawRegional.txt", "rawRegional", "Regional")
