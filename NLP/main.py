import nltk
# from nltk import *
# from nltk.corpus import gutenberg
# nltk.corpus.gutenberg.fileids()

# for fileid in gutenberg.fileids():
    # num_chars = len(gutenberg.raw(fileid))
    # num_words = len(gutenberg.words(fileid))
    # num_sents = len(gutenberg.sents(fileid))
    # print num_chars
    # print num_words
    # print num_sents

# text5.concordance("boook") # find similar.
from nltk.corpus import brown
print brown.categories()
print brown.words(categories='news')