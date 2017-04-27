import nltk
import glob
from nltk.collocations import *

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

female = ["she","woman","female","her","girl","daughter","mother","sister"]


for filename in glob.glob("final/*.txt"):

	print filename

	with open(filename, "rw+") as f:
		#read in text and tokenize
		text = f.read()
		tokens = nltk.wordpunct_tokenize(text)

		# score bigrams
		finder2 = BigramCollocationFinder.from_words(tokens)
		finder2.apply_ngram_filter(lambda w1, w2: w1 not in female and w2 not in female)

		# score trigrams
		finder3 = TrigramCollocationFinder.from_words(tokens)
		finder3.apply_ngram_filter(lambda w1, w2, w3: w1 not in female and w2 not in female and w3 not in female)

		scored2 = finder2.nbest(bigram_measures.raw_freq,50)
		scored3 = finder3.nbest(trigram_measures.raw_freq, 50)

		print scored2
		print scored3

	break