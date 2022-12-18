from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from format import split_into_sentences
import re

# Open File
fileName = "rawRegional"
file = open("New_Data/Raw/rawRegional.txt")
line = file.read()

# Format data into sentences
sentenceData = split_into_sentences(line)

# Remove Stop Words
stop_words = set(stopwords.words('english'))

def removeStoppedWords(sentence):
    words = word_tokenize(sentence)
    filtered_data = [w for w in words if not w in stop_words]
    return ' '.join(filtered_data)
stoppedData = []
for sentence in sentenceData:
    stoppedSentence = removeStoppedWords(sentence)
    stoppedData.append(stoppedSentence)     

# Stem or Lemmatize Words
ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()
data = []

lemmatizer = WordNetLemmatizer()
def lemmatizeWords(sentence):
    words = word_tokenize(sentence)
    stemmed_data = [ps.stem(w) for w in words]
    return ' '.join(stemmed_data)

lemmatizedData = []
for sentence in stoppedData:
    lemmatizedSentence = lemmatizeWords(sentence)
    lemmatizedData.append(lemmatizedSentence)

# Write into document
for sentence in lemmatizedData:
    appendFile = open("/Users/varunjoshi/Documents/Python/STIA_458/stiaFinalProject/attempt2TestData.txt", 'a')
    if "//" in sentence:
        appendFile.write("\n" + sentence + "\n" + "\n")
        continue
    if "[" in sentence:
        appendFile.write("\n" + "\n" + sentence + "\n")
        continue
    appendFile.write(sentence + " ")
    appendFile.close()
