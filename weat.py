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

text = open('weat-data.txt','rw+')
line = text.readline().strip()
while (line):

	work.append(float(line))
	arts.append(float(text.readline().strip()))
	depend.append(float(text.readline().strip()))
	preg.append(float(text.readline().strip()))
	line = text.readline().strip()

filenew = open('weat-data2.txt','w')
for item in work:
	filenew.write(str(item) + ',')
filenew.write('\n')
for item in arts:
	filenew.write(str(item) + ',')
filenew.write('\n')
for item in depend:
	filenew.write(str(item) + ',')
filenew.write('\n')
for item in preg:
	filenew.write(str(item) + ',')
filenew.write('\n')


labels = ['AU','BD','CA','GBB','GBG','GH','HK','IE','IN','JM','KE','LK','MY','NG','NZ','PH','PK','SG','TZ','USB','USG','ZA']

africa = ['KE','GH','NG','TZ','ZA','JM']
oceania = ['PH','SG','MY','HK']
seas = ['PK','IN','BD','LK']
west = ['USG','USB','GBG','GBB','CA','IE','AU','NZ']

work_africa = []
arts_africa = []
depend_africa = []
preg_africa = []
for country in africa:
	i = labels.index(country)
	work_africa.append(work[i])
	arts_africa.append(arts[i])
	depend_africa.append(depend[i])
	preg_africa.append(preg[i])

work_oceania = []
arts_oceania = []
depend_oceania = []
preg_oceania = []
for country in oceania:
	i = labels.index(country)
	work_oceania.append(work[i])
	arts_oceania.append(arts[i])
	depend_oceania.append(depend[i])
	preg_oceania.append(preg[i])

work_seas = []
arts_seas = []
depend_seas = []
preg_seas = []
for country in seas:
	i = labels.index(country)
	work_seas.append(work[i])
	arts_seas.append(arts[i])
	depend_seas.append(depend[i])
	preg_seas.append(preg[i])

work_west = []
arts_west = []
depend_west = []
preg_west = []
for country in west:
	i = labels.index(country)
	work_west.append(work[i])
	arts_west.append(arts[i])
	depend_west.append(depend[i])
	preg_west.append(preg[i])


# red = plt.scatter(work_africa,depend_africa,c="red")
# blue = plt.scatter(work_oceania, depend_oceania,c="blue")
# green = plt.scatter(work_seas, depend_seas,c="green")
# yellow = plt.scatter(work_west, depend_west,c="yellow")

# for label, x, y in zip(labels,work,depend):
#     plt.annotate(
#         label,
#         xy=(x, y), xytext=(-5, 3),
#         textcoords='offset points', ha='right', va='bottom')

# plt.title("Correlation of effect sizes:\n Home/Work and Dependence/Independence")
# plt.xlabel("Gender and work")
# plt.ylabel("Gender and dependence")
# plt.legend([red,blue,green,yellow],["Africa","Oceania","SE Asia","West"])
# plt.show()



# red = plt.scatter(arts_africa,work_africa,c="red")
# blue = plt.scatter(arts_oceania, work_oceania,c="blue")
# green = plt.scatter(arts_seas, work_seas,c="green")
# yellow = plt.scatter(arts_west, work_west,c="yellow")
# for label, x, y in zip(labels,arts,work):
# 	if (label == "GBB"):
# 	    plt.annotate(
# 	        label,
# 	        xy=(x, y), xytext=(20, 3),
# 	        textcoords='offset points', ha='right', va='bottom')
# 	elif (label == "AU"):
# 	    plt.annotate(
# 	        label,
# 	        xy=(x, y), xytext=(-5, -10),
# 	        textcoords='offset points', ha='right', va='bottom')
# 	elif (label == "GH"):
# 	    plt.annotate(
# 	        label,
# 	        xy=(x, y), xytext=(0, 4),
# 	        textcoords='offset points', ha='right', va='bottom')
# 	elif (label == "JM"):
# 	    plt.annotate(
# 	        label,
# 	        xy=(x, y), xytext=(0, 3),
# 	        textcoords='offset points', ha='right', va='bottom')
# 	elif (label == "ZA"):
# 	    plt.annotate(
# 	        label,
# 	        xy=(x, y), xytext=(4, 3),
# 	        textcoords='offset points', ha='right', va='bottom')
# 	else:
# 		plt.annotate(
# 	        label,
# 	        xy=(x, y), xytext=(-5, 3),
# 	        textcoords='offset points', ha='right', va='bottom')

# plt.title("Correlation of effect sizes:\n Arts/STEM and Home/Work")
# plt.xlabel("Gender and arts")
# plt.ylabel("Gender and work")
# plt.legend([red,blue,green,yellow],["Africa","Oceania","SE Asia","West"])
# #plt.show()

# plt.savefig("arts-work.png")





# red = plt.scatter(depend_africa,arts_africa,c="red")
# blue = plt.scatter(depend_oceania, arts_oceania,c="blue")
# green = plt.scatter(depend_seas, arts_seas,c="green")
# yellow = plt.scatter(depend_west, arts_west,c="yellow")
# for label, x, y in zip(labels,depend,arts):
# 	if (label == "GH"):
# 	    plt.annotate(
# 	        label,
# 	        xy=(x, y), xytext=(-5, -10),
# 	        textcoords='offset points', ha='right', va='bottom')
# 	elif (label == "SG"):
# 		plt.annotate(
# 	        label,
# 	        xy=(x, y), xytext=(10, 5),
# 	        textcoords='offset points', ha='right', va='bottom')
# 	else:
# 		plt.annotate(
# 	        label,
# 	        xy=(x, y), xytext=(-5, 3),
# 	        textcoords='offset points', ha='right', va='bottom')
# # z = np.polyfit(work, depend, 1)
# # p = np.poly1d(z)
# # plt.plot(work,p(work),"r--")
# # print "y=%.6fx+(%.6f)"%(z[0],z[1])
# plt.title("Correlation of effect sizes:\n Dependence/Independence and Arts/STEM")
# plt.xlabel("Gender and dependence")
# plt.ylabel("Gender and arts")
# plt.legend([red,blue,green,yellow],["Africa","Oceania","SE Asia","West"])
# plt.show()
#plt.savefig("dep-arts.png")


# red = plt.scatter(preg_africa,depend_africa,c="red")
# blue = plt.scatter(preg_oceania, depend_oceania,c="blue")
# green = plt.scatter(preg_seas, depend_seas,c="green")
# yellow = plt.scatter(preg_west, depend_west,c="yellow")

# for label, x, y in zip(labels,preg,depend):

# 	if (label == "CA"):
# 	    plt.annotate(
# 	        label,
# 	        xy=(x, y), xytext=(20, -10),
# 	        textcoords='offset points', ha='right', va='bottom')
# 	elif (label == "JM"):
# 		plt.annotate(
# 	        label,
# 	        xy=(x, y), xytext=(-5, -10),
# 	        textcoords='offset points', ha='right', va='bottom')
# 	elif (label == "GH"):
# 		plt.annotate(
# 	        label,
# 	        xy=(x, y), xytext=(5, -15),
# 	        textcoords='offset points', ha='right', va='bottom')
# 	elif (label == "NG"):
# 		plt.annotate(
# 	        label,
# 	        xy=(x, y), xytext=(0, 5),
# 	        textcoords='offset points', ha='right', va='bottom')
# 	elif (label == "USG"):
# 		plt.annotate(
# 	        label,
# 	        xy=(x, y), xytext=(15, 10),
# 	        textcoords='offset points', ha='right', va='bottom')
# 	else:
# 		plt.annotate(
# 	        label,
# 	        xy=(x, y), xytext=(-5, 3),
# 	        textcoords='offset points', ha='right', va='bottom')

# plt.title("Correlation of effect sizes:\n Pregnancy/Hero and Dependence/Independence")
# plt.xlabel("Gender and heroics")
# plt.ylabel("Gender and dependence")
# plt.legend([red,blue,green,yellow],["Africa","Oceania","SE Asia","West"], bbox_to_anchor=(.27,1))
# plt.show()

#plt.savefig('god-dep.jpg')

