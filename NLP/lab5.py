import nltk
# text = nltk.word_tokenize("And now for something completely different")
# print text
# print nltk.pos_tag(text)
text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())

# print text.similar('woman')
# print text.similar('bought')
# print text.similar('over')
# print text.similar('the')

print nltk.corpus.brown.tagged_words()
print nltk.corpus.brown.tagged_words(simplify_tags=True)