from bhtsne import tsne
import matplotlib.pyplot as plt
from gensim.models.keyedvectors import KeyedVectors
import numpy as np
import glob


def get_data():

	global wv

	out = open('tsnedata.txt','w')
	for country in glob.glob('vecs/*'):

		print "~~~~~~~~~~~~~~ " + country.split("/")[1] + " ~~~~~~~~~~~~~~"
		wv = KeyedVectors.load_word2vec_format(country, binary=True)

		man = wv.word_vec("man")
		woman = wv.word_vec("woman")
		doctor = wv.word_vec('doctor')
		nurse = wv.word_vec('nurse')

		for m in man:
			out.write(str(m) + "\t")
		out.write('\n')
		for w in woman:
			out.write(str(w) + '\t')
		out.write('\n')
		for d in doctor:
			out.write(str(d) + '\t')
		out.write('\n')
		for n in nurse:
			out.write(str(n) + '\t')
		out.write('\n')


#get_data()
data = np.loadtxt('tsnedata.txt')

labels = ['AU','BD','CA','GBB','GBG','GH','HK','IE','IN','JM','KE','LK','MY','NG','NZ','PH','PK','SG','TZ','USB','USG','ZA']

africa = ['KE','GH','NG','TZ','ZA','JM']
oceania = ['PH','SG','MY','HK']
seas = ['PK','IN','BD','LK']
west = ['USG','USB','GBG','GBB','CA','IE','AU','NZ']

indices = []
for i in west+africa+seas+oceania:
	indices.append(labels.index(i))


colors = []
for label in labels:
	if (label in africa):
		colors.append('red')
		colors.append('red')
		colors.append('blue')
		colors.append('blue')
	if (label in oceania):
		colors.append('blue')
		colors.append('blue')
		colors.append('blue')
		colors.append('blue')
	if (label in seas):
		colors.append('green')
		colors.append('green')
		colors.append('green')
		colors.append('green')
	if (label in west):
		colors.append('yellow')
		colors.append('yellow')
		colors.append('yellow')
		colors.append('yellow')


Y = tsne(data, 3, perplexity=15)

print Y

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# labs = []
# x=[]
# y=[]
# for index in indices:
# 	num = index*4
# 	for i in range(2):
# 		plt.scatter(Y[num+i, 0], Y[num+i, 1],c=colors[num+i])
# 		if ((num+i) % 2 == 0):
# 			x.append(Y[num+i,0])
# 			y.append(Y[num+i,1])
# 			labs.append(labels[index])

# print x
# print y


# labs = []
# for label in labels:
# 	labs.append(label)
# 	labs.append(label)

# for label, x,y in zip(labs,x,y):
# 	ax.annotate(
#         label,
#         xy=(x, y), xytext=(-5, 5),
#         textcoords='offset points', ha='right', va='bottom')
# plt.show()


ax.scatter(Y[:,0],Y[:,1],Y[:,2],c=colors)
plt.show()
