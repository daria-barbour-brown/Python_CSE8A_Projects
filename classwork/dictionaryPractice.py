# zipcodes = {92122: "San Diego", 53705: "Madison", 600014: "Chennai"}
# if 92123 not in zipcodes:
# 	zipcodes[92123] = "not there"

# print(zipcodes[92123])

# #else
# 	#print("key not found")


def word_freq_count(lst):
	
	result = {} #empty dict
	for item in lst:   #iterate through list
		
		count = 0
		if item in result:  #if current item is in the empty dict already...
			count = result[item]  #then set counter = value associated with key, word
		
		
		result[item] = count + 1 #then increase count
	return result

#print(word_freq_count(["turkey", "gravy", "corn", "cranberry", "turkey", "gravy", "corn", "turkey", "corn", "turkey"]))


def letter_count_of_words(lst):
	result = {} #empty dict

	for item in lst:   #iterate through list
		length = len(item)

		if length not in result:  #if length of current itwm doesnt exist in dict, create list
			result[length] = []

		if item not in result[length]:  #if item is not in dict, add to dict at key length od current item
			result[length].append(item)


	return result

print(letter_count_of_words(["turkey", "gravy", "corn", "cranberry", "turkey", "gravy", "corn", "turkey", "corn", "turkey", "yams"]))



