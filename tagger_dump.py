from cPickle import dump
from nltk.corpus import brown
import nltk
brown_tagged_sents = brown.tagged_sents()
brown_sents = brown.sents()
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)

output = open('t2.pkl', 'wb')
dump(unigram_tagger, output, -1)
output.close()

