from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from format import split_into_sentences

def stemWords(file, fileName):

    file1 = open(file)
    line = file1.read()
    array = split_into_sentences(line)

    ps = PorterStemmer()

    for sentence in array:
        appendFile = open("stiaFinalProject/Data/Stemmed/" + fileName + ".txt", 'a')
        if "//" in sentence:
            appendFile.write("\n" + " " + sentence + "\n" + "\n")
            continue
        if "[" in sentence:
            appendFile.write("\n" + " " + sentence + "\n")
            continue
        words = word_tokenize(sentence)
        for w in words:
            appendFile.write(" " + ps.stem(w))
        appendFile.write("\n")
        appendFile.close()