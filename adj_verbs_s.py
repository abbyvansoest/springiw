from gensim.models.keyedvectors import KeyedVectors
import glob
import sys


def s(w,A,B):
	# get mean of similarity btwn w and all in A
	mean_a = 0.0
	for a in A:
		mean_a = mean_a + wv.similarity(w,a)
	mean_a = mean_a/float(len(A))
	# and all in B
	mean_b = 0.0
	for b in B:
		mean_b = mean_b + wv.similarity(w,b)
	mean_b = mean_b/float(len(B))
	return mean_a - mean_b


global wv

countries = glob.glob("vecs/*")

adjs = open("dendro/adjectives.txt","rw+").read().split()
verbs = open("dendro/verbs.txt","rw+").read().split()

woman = ["she","woman","female","her","girl","daughter","mother","sister"]
man = ["he","man","male","him","boy","son","father","brother"]


# adjectives
f = open('out_adj_s','w')
# verbs
f2 = open('out_verbs_s','w')
for country in countries:

	wv = KeyedVectors.load_word2vec_format(country, binary=True)

	for a in adjs:
		val = s(a, woman, man)
		f.write("%.8f, "% val)
	for v in verbs:
		val = s(v, woman, man)
		f2.write("%.8f, "% val)

	f.write("\n")
	f2.write("\n")
	