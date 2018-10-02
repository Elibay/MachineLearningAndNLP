import nltk
from urllib import urlopen
url = "http://www.gutenberg.org/files/2554/2554-0.txt"
raw = urlopen(url).read()
# print type(raw)
# print len(raw)
# print raw[:75]

tokens = nltk.word_tokenize(raw.decode("UTF8"))
# print type(tokens)
# print len(tokens)
# print tokens[:10]

text = nltk.Text(tokens)
# print type(text)
# print text[1024:1062]
# print text.collocations()

# print raw.find("PART I")
# print raw.rfind("End of Project Gutenberg's Crime")
# raw = raw[5384:1157743]
# print raw.find("PART I")

