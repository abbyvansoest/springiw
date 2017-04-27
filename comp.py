from gensim.models.keyedvectors import KeyedVectors

wv = KeyedVectors.load_word2vec_format('vecs/au_vectors.bin', binary=True)

# wv.most_similar(positive=['woman', 'king'], negative=['man'])
# wv.most_similar_cosmul(positive=['woman', 'king'], negative=['man'])
# wv.doesnt_match("breakfast cereal dinner lunch".split())

jobs1 = ["programmer","engineer","doctor","scientist","computer"]
jobs2 = ["nurse","teacher","secretary","librarian","receptionist"]

home = ["home","kitchen","family","bake","flowers","garden","delicate"]
work = ["career","office","computer","vocation","occupation","professional","business"]

# for h in home:
# 	print str(round(wv.similarity(h, 'mary'),4))+"\t"+str(round(wv.similarity(h, 'john'),4))

# print "---------"

# for w in work:
# 	print str(round(wv.similarity(w, 'mary'),4))+"\t"+str(round(wv.similarity(w, 'john'),4))

# print "**********"
#wv2 = KeyedVectors.load_word2vec_format('vecs/gb_blog_vectors.bin', binary=True)

# for h in home:
# 	print h
# 	print str(round(wv2.similarity(h, 'mary'),4))+"\t"+str(round(wv2.similarity(h,'john'),4))

# print "---------"

# for w in work:
# 	print str(round(wv2.similarity(w, 'mary'),4))+"\t"+str(round(wv2.similarity(w, 'john'),4))

# for j1 in jobs1:
# 	print str(round(wv2.similarity(j1, 'woman'),4))+"\t"+str(round(wv2.similarity(j1,'man'),4))

# print "---------"

# for j2 in jobs2:
# 	print str(round(wv2.similarity(j2, 'woman'),4))+"\t"+str(round(wv2.similarity(j2, 'man'),4))

# print "**********"
wv3 = KeyedVectors.load_word2vec_format('vecs/in_vectors.bin', binary=True)

# for j1 in jobs1:
# 	print str(round(wv3.similarity(j1, 'woman'),4))+"\t"+str(round(wv3.similarity(j1,'man'),4))

# print "---------"

# for j2 in jobs2:
# 	print str(round(wv3.similarity(j2, 'woman'),4))+"\t"+str(round(wv3.similarity(j2, 'man'),4))



A = ["caress", "freedom", "health", "love", "peace", "cheer", "friend", "heaven", "loyal", "pleasure", "diamond", "gentle", "honest", "lucky",
"rainbow", "diploma", "gift", "honor", "miracle", "sunrise", "family", "happy", "laughter", "paradise", "vacation"]
B = ["abuse", "crash", "filth", "murder", "sickness", "accident", "death", "grief", "poison", "stink", "assault", "disaster", "hatred", "pollute",
"tragedy", "divorce", "jail", "poverty", "ugly", "cancer", "kill", "rotten", "vomit", "agony", "prison"]

for a in A:
	print str(wv3.similarity("happy",a)) + "\t" + str(wv3.similarity("sad",a))
print "......"
for b in B:
	print str(wv3.similarity("happy",b)) + "\t" +  str(wv3.similarity("sad",b))


