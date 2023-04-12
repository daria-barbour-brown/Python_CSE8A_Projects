#PART 2

#LIBRARY
library = {'Harry Potter': 10, 'Percy Jackson': 5, 'Eragon': 8}

num_e = library['Eragon']
num_p = library.get('Percy Jackson')

#num_e will = 8, num_p will = 5

#print(num_e)
#print(num_p)

# function to return both book and copies
def print_all(library):
		for book in library:
			print(book + " has " + str(library[book]) + " copies.")

# print_all(library)
# library['Eragon'] = library['Eragon'] + 5
# library['Harry Potter'] = library['Harry Potter'] + 3
# print_all(library)

#PART 3
#BUILDING DICTS FROM TUPLES

#takes in list of tuples and returns dictionary
def build_dict_from_tuples(tupleList):
	tupDict = {}
	for el in tupleList:
		tupDict[el[0]] = el[1]
	return tupDict

# print(build_dict_from_tuples([('a', 1), ('b', 2), ('c', 3)])) 
# #returns {'a': 1, 'b':2, 'c':3}

# print(build_dict_from_tuples([('x', 'hello'), ('y', 328)]))
# #returns {'x': 'hello', 'y': 328}


tuples = [('a', 1), ('b', 2), ('c', 3)]
result = build_dict_from_tuples(tuples)

#print(result)


#PART 4
#COUNTING CHARS

def count_char(data):
    d = {}
    
    for char in data:
    	count = 0
    	if char in d:
    		count = d[char]
    	d[char] = count + 1





    return d

result = count_char('Boot')

# count_char('I am Sam')
# print(result) 
# #returns {'I': 1, ' ': 2, 'a': 2, 'm': 2, 'S': 1}

# count_char('hElLo')
# print(result)
# #returns {'h': 1, 'E': 1, 'l': 1, 'L': 1, 'o': 1}

# count_char('Boot')
# print(result)
# #returns {'B': 1, 'o': 2, 't': 1}

#PART 5
#COLORS

#returns list of RGB colors
def convert(colors, c_map):
    res = []
    for color in colors:
    	res.append(c_map[color])
    return res

colors = ['r', 'b']
c_map = {'r':(255,0,0), 'b': (0,0,255)}
#result = convert(colors, c_map)
#print(result)


c_map = {'blue':(0,0,255), 'red':(255,0,0)}

#result = convert(['red'], c_map)
#print(result) 

#returns dictionary of (RBG vals: color)
def invert_dict(color_dict):
    res = {}
    FILL_ME
    return res

color_map ={'red':(255,0,0)}
result = invert_dict(color_map)












































 
