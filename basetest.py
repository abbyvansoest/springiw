from gensim.models.keyedvectors import KeyedVectors
import numpy as np
import glob

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

countries = glob.glob("vecs/*")

for country in countries:

	print "~~~~~~~~~~~~~~ " + country.split("/")[1] + " ~~~~~~~~~~~~~~"

	wv = KeyedVectors.load_word2vec_format(country, binary=True)

	bugs = ["ant", "caterpillar", "flea", "locust", "spider", "bedbug", "centipede", "fly", "maggot", "tarantula", "bee", "cockroach", "gnat", "mosquito",
	"termite", "beetle", "cricket", "hornet", "moth", "wasp", "dragonfly", "horsefly", "roach", "weevil"]
	flowers = ["aster", "clover", "hyacinth", "marigold", "poppy", "azalea", "crocus", "iris", "orchid", "rose", "bluebell", "daffodil", "lilac", "pansy", "tulip",
	"buttercup", "daisy", "lily", "peony", "violet", "carnation", "magnolia", "petunia", "zinnia"]

	pos = ["caress", "freedom", "health", "love", "peace", "cheer", "friend", "heaven", "loyal", "pleasure", "diamond", "gentle", "honest", "lucky",
	"rainbow", "diploma", "gift", "honor", "miracle", "sunrise", "family", "happy", "laughter", "paradise", "vacation"]
	neg = ["abuse", "crash", "filth", "murder", "sickness", "accident", "death", "grief", "poison", "stink", "assault", "disaster", "hatred", "pollute",
	"tragedy", "divorce", "jail", "poverty", "ugly", "cancer", "kill", "rotten", "vomit", "agony", "prison"]

	bugs = [i for i in bugs if i in wv.vocab]
	flowers = [i for i in flowers if i in wv.vocab]
	pos = [i for i in pos if i in wv.vocab]
	neg = [i for i in neg if i in wv.vocab]

	print "insect/flower effect size: " + str(round(abs(effect_size(bugs,flowers,pos,neg)),4))

	music = ["bagpipe", "cello", "guitar", "lute", "trombone", "banjo", "clarinet", "harmonica", "mandolin", "trumpet", "bassoon",
	"drum", "harp", "oboe", "tuba", "bell", "fiddle", "harpsichord", "piano", "viola", "bongo", "flute", "horn", "saxophone", "violin"]
	weapons = ["arrow", "club", "gun", "missile", "spear", "axe", "dagger", "harpoon", "pistol", "sword", "blade", "dynamite", "hatchet", "rifle", "tank",
	"bomb", "firearm", "knife", 'shotgun', "teargas", "cannon", "grenade", "mace", "slingshot", "whip"]

	music = [i for i in music if i in wv.vocab]
	weapons = [i for i in weapons if i in wv.vocab]

	print "music/weapon effect size: " + str(round(abs(effect_size(music,weapons,pos,neg)),4))

	woman = ["she","woman","female","her","hers","girl","daughter","mother","sister","aunt"]
	man = ["he","man","male","his","him","boy","son","brother","father","uncle"]
	career = ["executive", 'management', 'professional', 'corporation', 'salary', 'office', 'business', 'career']
	family = ['home', 'parents', 'children', 'family', 'cousins', 'marriage', 'wedding', 'relatives']

	woman = [i for i in woman if i in wv.vocab]
	man = [i for i in man if i in wv.vocab]
	career = [i for i in career if i in wv.vocab]
	family = [i for i in family if i in wv.vocab]

	print "man/woman career/family effect size: " + str(round(abs(effect_size(woman,man,career,family)),4))


	math = ['math', 'algebra', 'geometry', 'calculus', 'equations', 'computation', 'numbers', 'addition']
	art = ['poetry', 'art', 'dance', 'literature', 'novel', 'symphony', 'drama', 'sculpture', 'paint','painting']

	math = [i for i in math if i in wv.vocab]
	art = [i for i in art if i in wv.vocab]
	print "art/math: " + str(round(abs(effect_size(woman,man,art,math)),4))


print bugs
print flowers
print pos
print neg
print man
print woman
print career
print family









