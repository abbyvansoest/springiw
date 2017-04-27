
from gensim.models.keyedvectors import KeyedVectors
import glob
import sys
import numpy as np
from sklearn.metrics import jaccard_similarity_score

# FEMALE = True

# global wv

countries = glob.glob("vecs/*")
# words = open("500.txt","rw+").read().split()

# matrix = []
# for country in countries:

# 	print country
# 	wv = KeyedVectors.load_word2vec_format(country, binary=True)

# 	vec = []
# 	# get list of most similar words to 
# 	for word in words:
# 		sim = wv.most_similar(word, topn=100)
# 		for item in sim:
# 			vec.append(item[0])

# 	matrix.append(vec)
	

# out = open("usage_lists.txt",'w')
# for l in matrix:
# 	for item in l:
# 		out.write(item+ " ")
# 	out.write("\n")

# print matrix

w = len(countries)
h = len(countries)

# Get jaccard similarity
# jac_matrix = [[0 for x in range(w)] for y in range(h)] 

# for i in range(w):
# 	for j in range(h): 
# 		score = jaccard_similarity_score(matrix[i], matrix[j])
# 		jac_matrix[i][j] = score

# out2 = open("usage_sim_jac",'w')
# for l in jac_matrix:
# 	out2.write("[")
# 	for item in l:
# 		out2.write(str(item)+ " ")
# 	out2.write("]\n")


# get cosine similarity

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.corpus import stopwords
import numpy as np
import numpy.linalg as LA
import re

lists = open('usage_lists.txt', 'rw+').read().split('\n')
print lists

stopWords = stopwords.words('english')
vectorizer = CountVectorizer(stop_words = stopWords)
#print vectorizer
transformer = TfidfTransformer()
#print transformer

array = vectorizer.fit_transform(lists).toarray()
cx = lambda a, b : round(np.inner(a, b)/(LA.norm(a)*LA.norm(b)), 3)

cos_matrix = [[0 for x in range(w)] for y in range(h)] 

for i in range(w):
    for j in range(h):
        #print str(vector) + " : "  +str(testV)
        vector = array[i]
        testV = array[j]
        cosine = cx(vector, testV)
        cos_matrix[i][j] = cosine

out3 = open("usage_sim_cos",'w')
for l in cos_matrix:
	for item in l:
		out3.write(str(item)+ " ")
	out3.write("\n")




