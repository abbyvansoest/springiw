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

	sim = []
	for c in A+B:
		sim.append(wv.similarity(w,c))

	return (mean_a - mean_b) / np.std(sim)


global wv

ogcareers = ["technician", 'accountant', 'supervisor', 'engineer', 'worker', 'educator', 'clerk', 'counselor', 'inspector', 'mechanic', 'manager',
'therapist', 'administrator', 'salesperson', 'receptionist', 'librarian', 'advisor', 'pharmacist', 'janitor', 'psychologist', 'physician', 'carpenter',
'nurse', 'investigator', 'bartender', 'specialist', 'electrician', 'officer', 'pathologist', 'teacher', 'lawyer', 'planner', 'practitioner', 'plumber',
'instructor', 'surgeon', 'veterinarian', 'paramedic', 'examiner', 'chemist', 'machinist', 'appraiser', 'nutritionist', 'architect', 'hairdresser',
'baker', 'programmer', 'paralegal', 'hygienist', 'scientist']
woman = ["she","woman","female","her","hers","girl","daughter","mother","sister","aunt"]
man = ["he","man","male","his","him","boy","son","brother","father","uncle"]


for country in glob.glob("vecs/*"):

	wv = KeyedVectors.load_word2vec_format(country, binary=True)

	svals = []
	d = {}

	careers = [i for i in ogcareers if i in wv.vocab]

	for career in careers:
		val = s(career, woman, man)
		svals.append(val)
		d[career] = val

	print "-------------" + country + "-------------"
	print d
	print "variance: " + str(np.var(svals))



