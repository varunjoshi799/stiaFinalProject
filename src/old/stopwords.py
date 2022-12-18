import nltk
from nltk.corpus import stopwords
# nltk.download('stopwards')

stop_words = set(stopwords.words('english'))

def stopWords(file, fileName):

    file1 = open(file)

    line = file1.read()
    words = line.split()

# for r in words:
#     if not r in stop_words:
#         appendFile = open("Data/Stopped/filteredRegional.txt", 'a')
#         for sentence in array:
#             if "//" and r in sentence:
#                 appendFile.write("\n" + " " + sentence + "\n" + "\n")
#                 continue
#             if "[" and r in sentence:
#                 appendFile.write("\n" + " " + sentence + "\n")
#                 continue
#         appendFile.write(" "+r)
#         appendFile.close()

    for r in words:
        if not r in stop_words:
            appendFile = open("stiaFinalProject/Data/Stopped/" + fileName + ".txt", 'a')
            appendFile.write(" "+r)
            appendFile.close()

# print(line)

# import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context

# nltk.download('stopwords')