# from nltk import tokenize

# -*- coding: utf-8 -*-
import re
alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr|Fr|Prof)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"
digits = "([0-9])"

def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    text = re.sub(digits + "[.]" + digits,"\\1<prd>\\2",text)
    if "..." in text: text = text.replace("...","<prd><prd><prd>")
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    text = re.sub('\"', "", text)
    text = re.sub('"', "", text)
    text = re.sub("”", "", text)
    text = re.sub("“", "", text)
    text = re.sub('"', "", text)
    text = re.sub("’", "", text)
    # sentence = sentence.replace(".","")
    # text = re.sub(".", "", text)
    # text = re.sub(",", "", text)
    # text = re.sub('.', '', text)
    # text = re.sub(',', '', text)
    # text = re.sub("\[", " ", text)
    # text = re.sub("].", ".", text)
    text = text.replace('"', "")
    if "”" in text: text = text.replace("”","")
    if "\"" in text: text = text.replace(".\"","")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    if "  " in text: text = text.replace("  ", " ")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    if "." in text: text = text.replace(".","")
    if "," in text: text = text.replace(",","")
    if "’" in text: text = text.replace("’","")
    if "'" in text: text = text.replace("'","")
    if ":" in text: text = text.replace(":","")
    if "?" in text: text = text.replace("?","")
    if "!" in text: text = text.replace("!","")
    if ")" in text: text = text.replace(")","")
    if "(" in text: text = text.replace("(","")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

def formatDataset(file, fileName):

    file1 = open(file)
    line = file1.read()

    array = split_into_sentences(line)

# print(array)

    for sentence in array:
        appendFile = open("stiaFinalProject/Data/Formatted/" + fileName + ".txt", 'a')
        if "//" in sentence:
            appendFile.write("\n" + " " + sentence + "\n" + "\n")
            continue
        if "[" in sentence:
            appendFile.write("\n" + " " + sentence + "\n")
            continue
        appendFile.write(" " + sentence + "\n")
        appendFile.close()
# print(array)