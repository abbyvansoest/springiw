from gensim.models.keyedvectors import KeyedVectors
import numpy as np
import glob

def s(w,A):
	# get mean of similarity btwn w and all in A
	mean1 = 0.0
	mean2 = 0.0
	for a in A:
		mean1 = mean1 + wv.similarity(w,a)
		mean2 = mean2 + wv2.similarity(w,a)
	mean1 = mean1/float(len(A))
	mean2 = mean2/float(len(A))

	return mean1 - mean2


def effect_size(X,Y,A):
	mean1 = 0.0
	for x in X: 
		mean1 = mean1 + s(x,A) # distance of all x from A in set 1 vs. set 2
	mean1 = mean1/float(len(X))

	mean2 = 0.0
	for y in Y:
		mean2 = mean2 + s(y,A)  # distance of all y from A in set 1 vs. set 2
	mean2 = mean2/float(len(Y))
	
	sd = []
	for w in X+Y:
		sd.append(s(w,A))
	return (mean1-mean2)/np.std(sd)


global wv
global wv2

base = 'vecs/pk_vectors.bin'
countries = glob.glob("vecs/*")

wv = KeyedVectors.load_word2vec_format(base, binary=True)

print "PK VS THE WORLD"

for country in countries:

	print "~~~~~~~~~~~~~~ " + country.split("/")[1] + " ~~~~~~~~~~~~~~"

	wv2 = KeyedVectors.load_word2vec_format(country, binary=True)

	woman = ["she","woman","female","her","hers","girl","daughter","mother","sister","aunt"]
	man = ["he","man","male","his","him","boy","son","brother","father","uncle"]
	jobs1 = ["programmer","engineer","doctor","scientist","computer"]

	print "effect size: " + str(round(abs(effect_size(woman, man, jobs1)),4))

	print "\n"




# one is simialrtiy of woman/target words in one coutnry
# other is similartit of woman/target words in the other country




