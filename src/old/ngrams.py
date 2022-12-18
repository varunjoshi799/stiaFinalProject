import nltk
from nltk import ngrams
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
import re
from format import split_into_sentences

def createbigrams(file, fileName, type):

    file1 = open(file)

    line = file1.read()

    array = split_into_sentences(line)


    # for sentence in array:
    #     if ':' in sentence: sentence = sentence.replace(':', "")
    #     if ';' in sentence: sentence = sentence.replace(';', "")
    #     if ',' in sentence: sentence = sentence.replace(',', "")
    #     if '.' in sentence: sentence = sentence.replace('.', "")
    #     if "(" in sentence: sentence = sentence.replace("(", "")
    #     if ")" in sentence: sentence = sentence.replace(")", "")
    #     if "?" in sentence: sentence = sentence.replace("?", "")
    #     if "  " in sentence: sentence = sentence.replace("  ", " ")
        # print(sentence)

    for sentence in array:
        appendFile = open("stiaFinalProject/Data/N-gram/" + fileName + ".txt", 'a')
        if "//" in sentence:
            appendFile.write("\n" + " " + sentence + "\n" + "\n")
            continue
        if "[" in sentence:
            appendFile.write("\n" + " " + sentence + "\n")
            continue
        if ':' in sentence: sentence = sentence.replace(':', "")
        if ';' in sentence: sentence = sentence.replace(';', "")
        if ',' in sentence: sentence = sentence.replace(',', "")
        if '.' in sentence: sentence = sentence.replace('.', "")
        if "(" in sentence: sentence = sentence.replace("(", "")
        if ")" in sentence: sentence = sentence.replace(")", "")
        if "?" in sentence: sentence = sentence.replace("?", "")
        if "  " in sentence: sentence = sentence.replace("  ", " ")
        # n_grams = ngrams(sentence.split(), 2)
        # for grams in n_grams:
        #     print(grams)
        # print(sentence)    
        appendFile.write(" " + sentence + "\n")
        appendFile.close()

    file2 = open("stiaFinalProject/Data/N-gram/" + fileName + ".txt")

    line2 = file2.read()

    words = line2.split()

    # BIGRAMS

    word_fd = nltk.FreqDist(words)
    bigram_fd = nltk.FreqDist(nltk.bigrams(words))

    # print(bigram_fd.most_common())

    result = open("stiaFinalProject/Data/Results/" + type + "/" + fileName + ".txt", "a", encoding='utf-8')
    result.write('\n'.join(f'{bigram[0]} {bigram[1]}' for bigram in bigram_fd.most_common()))


# REGULAR WORD FREQUENCY

# word_fd = nltk.FreqDist(words)

# print(word_fd.most_common())
