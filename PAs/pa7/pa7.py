#PA7
#PART 1

#BIRD WATCHING --------------------------------------------------

#maps each bird with the number of spotted occurrences
def bird_distribution(bird_list): #takes in list of birds
	result = {}

	for bird in bird_list:
		count = 0
		if bird in result:
			count = result[bird] #setting count = existing val for current bird key (# of sightings)
			
		result[bird] = count +1 #increase count for new sighting

	return result #retuns dictionary of bird keys and # of sightings as vals

bird_list = bird_list = ['California quail', 'Blue Jay', 'Gyrfalcon', 'Blue Jay']
#print(bird_distribution(bird_list))

#BUSY MEETING ROOMS -----------------------------------------------

#returns dictionary that contains rooms with equal or more meetings than the threshold 
def busy_rooms(meetings, threshold):
	result = {}

	for item in meetings:
		if len(meetings[item]) >= threshold:
			result[item] = meetings[item]
	return result


meetings = {'CSE 2154': [14], 'CSE 3217': [9,10,11,14,15], 'CSE 1241': [10,11], 'CSE 2154': [7,8,10,11,14,16], 'CSE 1202': [9,11,12,14,17]}
threshold = 5
# print(busy_rooms(meetings, threshold))

#NBA PLAYER STATS --------------------------------------------------

def update_stats(career_points, recent_game): 
		for name,score in recent_game: #iterate through each tuple in lst, first el in tuple is saved as name and second as score
			career_points[name] = career_points[name]+score #set val in dict at current key name, to that val plus new score
		return career_points

career_points = {'LeBron James': 35516, 'Kawhi Leonard': 11085, 'Joel Embiid': 6649, 'Jayson Tatum': 5923}
recent_game = [('LeBron James', 28), ('Joel Embiid', 14) ]

#print(update_stats(career_points, recent_game))

#STAR POINTS -----------------------------------------------

#this function takes in a dict of training averages and the number of sample used to collect those avgs
#it also take in a list of tuples containing new numbers for a few lifts
#the function updates the running avg and retuns a new dictionary 
def updateRunningAvg(liftRunningAvgs, todaysNumbers):
	for workout,weight in todaysNumbers: 
		avg,numSamples = liftRunningAvgs[workout] #get data from tuple in dict
		newNumSamples = numSamples+1 #update the number of sample we now are using
		newAvg = (avg*numSamples + weight)/(newNumSamples) #preform arithmetic to calc new avg
		liftRunningAvgs[workout] = tuple() #tuple immutible, create new empty tuple as value for wokout key
		liftRunningAvgs[workout] = (newAvg,newNumSamples) #assign new tuple to key
		return liftRunningAvgs

liftRunningAvgs = {"Bench Press": (115, 10), "Squat": (135, 5), "OHP": (90, 10), "Dead Lift": (190, 4), "Hip Thrust": (135, 12)}
todaysLegDay = [("Squat", 185), ("Hip Thrust", 80)]

#print(updateRunningAvg(liftRunningAvgs, todaysLegDay))









