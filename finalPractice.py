#both functions return list of non-negative numbers 

def filter_negatives(my_list):
	result = []
	for list in range(len(my_list)):
		for num in range(len(my_list[list])):
			if my_list[list][num] >=  0:
				result.append(my_list[list][num])
	return result

#Sample run:
3print(filter_negatives([[-3, 2, 0], [4, -5, 7]]))
#[2, 0, 4, 7]

def filter_negatives2(my_list):
	result = []
	for list in my_list:
		for num in list:
			if num >=  0:
				result.append(num)
	return result

#print(filter_negatives2([[-3, 2, 0], [4, -5, 7]]))


#returns new dict with reverse mapping
#does not modify input dictionary 
def convert_dict(colors):
	result = {}
	for item in  colors.items(): #loop through each tuple
		result[item[1]] = item[0]
	return result	
#******* FIX
def convert_dict2(colors):
	result = {}
	for item in  colors.items(): #loop through each tuple

		result[item[1]] = item[0]
	return result
	

#Sample run:
print(convert_dict({"red":(255, 0, 0), "blue":(0, 255, 0), "green": (0, 0, 255)})
{(255, 0, 0): 'red', (0, 255, 0): 'blue', (0, 0, 255): 'green'})