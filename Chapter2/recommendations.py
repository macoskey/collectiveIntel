from math import sqrt 
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
import matplotlib as mplt

# returns a distance-based similarity score for person1 and person2
def sim_distance(prefs,person1,person2):
	# get the list of s hared items
	si={}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item] = 1
	
	# if they have no ratings in common, return 0
	if len(si) == 0: return 0
	
	# add up the squares of all the differences
	sum_of_squares = sum([pow(prefs[person1][item]-prefs[person2][item],2)
						  for item in si])
	
	return 1/(1+sqrt(sum_of_squares))
	
# returns the Pearson correlation coefficient for p1 and p2
def sim_pearson(prefs,p1,p2):
	# get the list of mutually rated items
	si={}
	for item in prefs[p1]:
		if item in prefs[p2]: si[item] = 1
	
	# find the number of elements
	n = len(si)
	
	if n == 0: return 0
	
	# add up the preferences
	sum1 = sum([prefs[p1][it] for it in si])
	sum2 = sum([prefs[p2][it] for it in si])
	
	# sum of squares
	sum1Sq = sum([pow(prefs[p1][it],2) for it in si])
	sum2Sq = sum([pow(prefs[p2][it],2) for it in si])
	
	# sum the products
	pSum = sum([prefs[p1][it]*prefs[p2][it] for it in si])
	
	# calculate the Pearson score
	num = pSum-(sum1*sum2/n)
	den = sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
	if den == 0: return 0
	
	r = num/den
	
	return r

# gets recommendations for a person by using a weighted average of every other user's rankings
def getRecommendations(prefs,person,similarity=sim_pearson):
	totals = {}
	simSums = {}
	for other in prefs:
		# don't compare to myself
		if other == person: continue
		
		sim = similarity(prefs,person,other)

		# ignore scores of zero or lower
		if sim <=0: continue

		for item in prefs[other]:
			# only score movies I haven't seen yet
			if item not in prefs[person] or prefs[person][item] == 0:
				# similarity * score
				totals.setdefault(item,0)
				totals[item]+=prefs[other][item]*sim
				# sum of similarities
				simSums.setdefault(item,0)
				sumSums[item]+=sim

			# create the normalized list
			rankings = [(total/simSums[item],item) for item, totals in totals.item()]

			# return the sorted list
			rankings.sort()
			rankings.reverse()
			return rankings

# functions I create start here

def plot_pearson(prefs):
	n = len(prefs)
	D = np.zeros((n,n))
	for i1 in range(n):
		for i2 in range(n):
			D[i1,i2] = sim_pearson(critics,critics.keys()[i1],critics.keys()[i2])
	plt.imshow(D,extent=[0,n,0,n], aspect='auto', interpolation='none')
	plt.show()	
	plt.xticks([0, 5, 7],fontsize=20)
	#mplt.colorbar()
	#plt.colorbar()
	return D

def plot_simdist(prefs):
	n = len(prefs)
	P = np.zeros((n,n))
	for i3 in range(n):
		for i4 in range(n):
			P[i3,i4] = sim_distance(critics,critics.keys()[i3],critics.keys()[i4])
	fig, ax = plt.subplots()
	plt.imshow(P,extent=[0,n,0,n], aspect = 'auto', interpolation = 'none')
	cbar = fig.colorbar()
	plt.show()
	return P

# functions I create ended



# A dictionary of movie critics and their ratings of a small set of movies
critics = {'Lisa Rose': {'Lady in the Water': 2.5, 
						 'Snakes on a Plane': 3.5, 
						 'Just My Luck': 3.0, 
						 'Superman Returns': 3.5, 
						 'You, Me and Dupree': 2.5, 
						 'The Night Listener': 3.0},
		   'Gene Seymour': {'Lady in the Water': 3.0, 
						 'Snakes on a Plane': 3.5, 
						 'Just My Luck': 1.5, 
						 'Superman Returns': 5.0,
						 'The Night Listener': 3.0, 
						 'You, Me and Dupree': 3.5},
		   'Michael Phillips': {'Lady in the Water': 2.5, 
						 'Snakes on a Plane': 3.0, 
						 'Superman Returns': 3.5, 
						 'The Night Listener': 4.0},
		   'Claudia Puig': {'Snakes on a Plane': 3.5,
						 'Just My Luck': 3.0,
						 'The Night Listener': 4.5,
						 'Superman Returns': 4.0,
						 'You, Me and Dupree': 2.5},
		   'Mick LaSalle': {'Lady in the Water': 3.0, 
						 'Snakes on a Plane': 4.0, 
						 'Just My Luck': 2.0, 
						 'Superman Returns': 3.0, 
						 'You, Me and Dupree': 2.0, 
						 'The Night Listener': 3.0},
		   'Jack Matthews': {'Lady in the Water': 3.0, 
						 'Snakes on a Plane': 4.0, 
						 'Just My Luck': 1.5, 
						 'Superman Returns': 5.0, 
						 'You, Me and Dupree': 3.5, 
						 'The Night Listener': 3.0},
	                'Toby': {'Snakes on a Plane': 4.5,
						 'You, Me and Dupree': 1.0, 
						 'Superman Returns': 4.0}						 
		  }

#plot_pearson(critics)
#plot_simdist(critics)

