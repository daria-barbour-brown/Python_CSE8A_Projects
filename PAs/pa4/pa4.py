#PA 4

#PATH, FILE FINDING
#PART 1.1
def extract_hwk_from_paths(paths):
	'''
		iterate throught the paths
		split the paths by slash
		we keep only the last element
		append that last element to the final list
	'''
	retList = []
	for path in paths:
		#if you append to new list as you iterate through old it retains the order
		splitPath = path.split('/') #['', 'home', 'CSE8A', 'jeff', 'Hwk2.py']
		retList.append(splitPath[-1])
	return retList

#STAR POINTS
def extract_endingpath_from_paths(paths):
	'''
		iterate through every path
		for each path split it by slash
		remove the unwanted parts of the path
		rejoin it with a slash so that it is still a path
		append it to the list
		return the final list
	'''
	retList = []
	for path in paths:
		joinedPath = ""
		#if you append to new list as you iterate through old it retains the order
		splitPath = path.split('/') #['', 'home', 'CSE8A', 'jeff', 'Hwk2.py']
		del splitPath[0:-2] #['jeff', 'Hwk1.pdf']
		joinedPath = '/'.join(splitPath) #jeff/Hwk1.pdf
		retList.append(joinedPath)
	return retList




#List Mutation
#PART 1.2

def find_and_swap(words, word_one, word_two):
	'''
		iterate through the words
		we need to keep track of the current index
		if we find a word if interest then we swap the word
	'''
	idx = 0 #keep track of the current word index
	for word in words:
		if word == word_one:
			words[idx]=word_two
		elif word == word_two:
			words[idx] = word_one
		idx+=1
	return words




#TEST PART 1.1
#path = ["/home/CSE8A/alex/Hwk1.pdf" , "/home/CSE8A/naomi/Hwk1.mp4", "/home/CSE11/jeff/Hwk1.pdf"]
#print(extract_hwk_from_paths(path))

#TEST PART 1.2 
#print(find_and_swap( ["apple", "orange", "APPLE", "apple"], "apple", "pear" ))


# #TEST STAR POINTS
# path = ["/home/CSE8A/jeff/Hwk1.pdf", "/home/CSE8A/naomi/Hwk1.mp4"]
# print(extract_endingpath_from_paths(path))


