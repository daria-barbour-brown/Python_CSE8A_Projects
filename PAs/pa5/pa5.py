#PART 1.1 
#Nested for loops with lists


#to save images to folder
# import os
# os.chdir("testResults")

def make_board(npFood, fruits, vegs):
	board = []

	for np in npFood:
		for fruit in fruits:
			for veg in vegs:
				print( type(np), type(fruit), veg)
				temp = np + "," + fruit + "," + veg
				board.append(temp)
	return board 

non_perishable_food = ["canned soup", "sausage", "pasta"]
fruits = ["bananas", "apples"] 
vegetables = ["onions"] 

#print(make_board(non_perishable_food, fruits, vegetables))

#PART 1.2
#Legitimate pool

def is_legitimate_pool(pool):
	counter = 0 #discerns between first and last el and middle els of pool 
	for lst in pool:  #look for illegitimate lists in pool
		if (counter == 0) or (counter == len(lst) -1):  #only occurs on first and last element in pool
			for el in lst:
				if el == 1:
					return "Illegitimate"

		else:  #occurs in middle elements of pool
			if (lst[0] == 1) or (lst[-1] == 1):
				return "Illegitimate"
		counter += 1 
	return "Legitimate"

pool1   = [[0, 0, 0, 0, 0],
       [0, 1, 1, 1, 0],
       [1, 1, 1, 0, 0],
       [0, 1, 0, 0, 0],
       [0, 1, 0, 0, 0]]


pool2 = [[0, 0, 0],
       [0, 1, 0],
       [0, 0, 0]]


# print(is_legitimate_pool(pool1))
# print(is_legitimate_pool(pool2))

#PART 1.3
#filters 

from CSE8AImage import *

#complement
def complement(img):
	for row in range(height(img)): #grab each row
		for col in range(width(img)): #from each col
			r,g,b = img[row][col] #set red = first el in current row and column index, green to the second...
			img[row][col] = (b, g, r) #change the current tuple to swap red and blue
	return img



#negative
def negative(img):
	for row in range(height(img)): #step through each row
		for col in range(width(img)): #for each row look through all columns
			r = 255 - img[row][col][0] #red = 255 minus first index of current tuple
			g = 255 - img[row][col][1] #green = 255 - second
			b = 255 - img[row][col][2] #blue = 225 - third index...
			img[row][col] = (r, g, b) #now save r, blue and green new into current tuple
	return img

#STAR POINTS
#saturation
def saturation(img):
	neg = []
	#image = create_img(height(img), width(img), (0,0,0))
	for row in range(height(img)): #grab each row
		for col in range(width(img)): #from each  row grab each tuple
			r,g,b = img[row][col]
			if r < 150 and b < 150 and g < 150:
				img[row][col] = (0, 0, 0)	
			if r > 150 and b > 150 and g > 150:
				img[row][col] = (255, 255, 255)
	return img
#FOR VIDEO
#run complement
# cat = load_img("../images/cat.jpg")
# img = complement(cat)
# save_img(img, "complement_cat.jpg")

# #run negative
# cat = load_img("../images/cat.jpg")
# img = negative(cat)
# save_img(img, "negative_cat.jpg")


