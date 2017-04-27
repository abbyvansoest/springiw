from gensim.models.keyedvectors import KeyedVectors
import glob
import sys

FEMALE = True

global wv

countries = glob.glob("vecs/*")

adjs = open("dendro/adjectives.txt","rw+").read().split()
#verbs = open("verbs.txt","rw+").read().split()

woman = ["she","woman","female","her","girl","daughter","mother","sister"]
man = ["he","man","male","him","boy","son","father","brother"]

if (FEMALE):
	use = woman
	name = "w"
else:
	use = man
	name = "m"

# adjectives
#f = open('out_adjs_'+name,'w')
i = 0
for country in countries:

	wv = KeyedVectors.load_word2vec_format(country, binary=True)


	for a in adjs:
		avg = 0.
		count = 0

		for w in use:
			avg = avg + wv.similarity(a,w)
			print str(avg) + " " + str(wv.similarity(a,w))
		avg = avg/float(len(use))
		print avg

	if (i == 2):
		break
	i = i+1

# # verbs
# f = open('out_verbs_'+name,'w')
# for country in countries:

# 	wv = KeyedVectors.load_word2vec_format(country, binary=True)

# 	vec = []

# 	for v in verbs:
# 		avg = 0.
# 		count = 0

# 		for w in use:
# 			avg = avg + wv.similarity(a,w)
# 		avg = avg/float(len(use))

# 		vec.append(avg)
# 		f.write("%.8f, "% avg)

# 	f.write("\n")
