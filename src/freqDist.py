import nltk
from nltk import ngrams
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

file = open("/Users/varunjoshi/Documents/Python/STIA_458/stiaFinalProject/attempt2TestData.txt")

line = file.read()

words = line.split()

word_fd = nltk.FreqDist(words)

result = open("/Users/varunjoshi/Documents/Python/STIA_458/stiaFinalProject/freqDist.txt", "a", encoding='utf-8')
result.write('\n'.join(f'{word[0]} {word[1]}' for word in word_fd.most_common()))