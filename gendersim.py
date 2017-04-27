from gensim.models.keyedvectors import KeyedVectors
import glob


global wv

countries = glob.glob("vecs/*")

for country in countries:

	print "~~~~~~~~~~~~~~ " + country.split("/")[1] + " ~~~~~~~~~~~~~~"

	wv = KeyedVectors.load_word2vec_format(country, binary=True)

	# print "FEMALE: "
	# print wv.most_similar(positive=["she","seems"],negative=["he"])

	# print "MALE: "
	# print wv.most_similar(positive=["he","seems"],negative=["she"])

	print "FEMALE: "
	print wv.most_similar(positive=["woman"], topn=50)

	print "MALE: "
	print wv.most_similar(positive=["man"],topn=50)	

	# print "FEMALE: "
	# print wv.most_similar(positive=["female"],negative=["male"])

	# print "MALE: "
	# print wv.most_similar(positive=["male"],negative=["female"])

	# print "FEMALE: "
	# print wv.most_similar(positive=["woman"])

	# print "MALE: "
	# print wv.most_similar(positive=["man"])