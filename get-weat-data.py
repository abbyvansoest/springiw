from gensim.models.keyedvectors import KeyedVectors
import numpy as np
import glob
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.patches as mpatches


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

def S(X,Y,A,B):
	sum1 = 0.0
	for x in X:
		sum1 = sum1 + s(x,A,B)
	sum2 = 0.0
	for y in Y:
		sum2 = sum2 + s(y,A,B)
	return sum1 - sum2

def effect_size(X,Y,A,B):
	mean1 = 0.0
	for x in X: 
		mean1 = mean1 + s(x,A,B)
	mean1 = mean1/float(len(X))
	mean2 = 0.0
	for y in Y:
		mean2 = mean2 + s(y,A,B)
	mean2 = mean2/float(len(Y))
	sd = []
	for w in X+Y:
		sd.append(s(w,A,B))
	return (mean1-mean2)/np.std(sd)


global wv

depend = [] # list of dependent effect sizes for each country
arts = []   # list of arts effect sizes for each country
work = []   # list of work effect sizes for each country
preg = []

countries = glob.glob("vecs/*")

outfile = open("weat-data.txt","w")

outfile2 = open("expanded-weat-data.txt","w")

for country in countries:

	print "~~~~~~~~~~~~~~ " + country.split("/")[1] + " ~~~~~~~~~~~~~~"

	wv = KeyedVectors.load_word2vec_format(country, binary=True)

	woman = ["she","woman","female","her","hers","girl","daughter","mother","sister","aunt"]
	man = ["he","man","male","his","him","boy","son","brother","father","uncle"]
	woman = [i for i in woman if i in wv.vocab]
	man = [i for i in man if i in wv.vocab]


	career = ["executive", 'management', 'professional', 'corporation', 'salary', 'office', 'business', 'career']
	family = ['home', 'parents', 'children', 'family', 'cousins', 'marriage', 'wedding', 'relatives','homemaker']
	career = [i for i in career if i in wv.vocab]
	family = [i for i in family if i in wv.vocab]

	# val = abs(effect_size(woman,man,career,family))
	# print "career/family effect size: " + str(round(val,4))
	# outfile.write(str(round(val,4)) + '\n')
	# work.append(val)
	for w in career:
		outfile2.write(str(s(w,woman,man))+",")
	for w in family:
		outfile2.write(str(s(w,woman,man))+",")

	math = ['math', 'algebra', 'geometry', 'calculus', 'equations', 'computation', 'mathematics','science','engineering','biology','chemistry','physics']
	art = ['poetry', 'art', 'dance', 'literature', 'novel', 'symphony', 'drama', 'sculpture', 'paint','painting','ceramics','creative','writing']
	math = [i for i in math if i in wv.vocab]
	art = [i for i in art if i in wv.vocab]

	# val = abs(effect_size(woman,man,art,math))
	# print "art/stem: " + str(round(val,4))
	# outfile.write(str(round(val,4))+ '\n')
	# arts.append(val)
	for w in math:
		outfile2.write(str(s(w,woman,man))+",")
	for w in art:
		outfile2.write(str(s(w,woman,man))+",")


	dep = ["dependent","fragile","needy","innocent","childlike","dependence","weak","frail","feeble","timid"]
	indp = ["independent","strong","willful","brave","autonomous","powerful","forceful"]
	dep = [i for i in dep if i in wv.vocab]
	indp = [i for i in indp if i in wv.vocab]

	# val = abs(effect_size(woman,man,dep,indp))
	# print "independence/dependence: " + str(round(val,4))
	# outfile.write(str(round(val,4))+'\n')
	# depend.append(val)
	for w in dep:
		outfile2.write(str(s(w,woman,man))+",")
	for w in indp:
		outfile2.write(str(s(w,woman,man))+",")

	pregnant = ["pregnant","fertile","menstruation","childbearing","babies"]
	god = ["violent","powerful","righteous","warrior","fighter","hero","champion","victor"]
	pregnant = [i for i in pregnant if i in wv.vocab]
	god = [i for i in god if i in wv.vocab]

	# val = abs(effect_size(woman,man,pregnant,god))
	# print "preg/god: " + str(round(val,4))
	# outfile.write(str(round(val,4))+'\n')
	# preg.append(val)
	for w in pregnant:
		outfile2.write(str(s(w,woman,man))+",")
	for w in god:
		outfile2.write(str(s(w,woman,man))+",")

	outfile2.write("\n")



