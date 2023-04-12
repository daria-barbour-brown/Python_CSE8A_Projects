#PA 3

def get_checkin_bags(bag_weights, min_weight, max_weight):
	checkin_bags = []
	for el in bag_weights:
		if el >= min_weight and el <= max_weight:
			checkin_bags.append(el)
	return checkin_bags


# #bag_weights = []
# min_weight = 36.9
# max_weight = 40.1

# print(get_checkin_bags(bag_weights, min_weight, max_weight)) 

#Star Points
#Statistics

def print_statistics(floats):
	maxVal = None
	minVal = None
	sumOfNums = 0.0
	zeroCount = 0
	negCount = 0
	posCount = 0
	for num in floats:
		if maxVal is None or num > maxVal:
			maxVal = num
		print ("Maximum: " + str(maxVal))
		
		if minVal is None or num < minVal:
			minVal = num
		print ("Minimum: " + str(minVal))
		
		sumOfNums = sumOfNums + num 
		avg = sumOfNums / float(len(floats))
		print("Mean: " + str(avg))
		
		if num == 0:
			zeroCount = zeroCount + 1
		print("Number of occurrences of Zero: " + str(zeroCount))
		
		if num < 0:
			negCount = negCount + 1
		print("Number of negative numbers: " + str(negCount))

		if num < 0:
			posCount = posCount + 1
		print("Number of positive numbers: " + str(posCount))



# data = [-20.0, 10.5, 0.0, -15.1, 21.0]
# print_statistics(data)

#More Practice w/ Loops

def print_pattern(n):
	for i in range(n):

		print("* " * i)


#print_pattern(3)







































