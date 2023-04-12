#PART 1
#ICECREAM MENUE

# fruits = ['apple', 'banana', 'strawberry']
# toppings = ['almond', 'chocolate', 'coconut', 'sprinkle']
# for i in fruits:
#     for j in toppings:
#         print(i + ' ice cream with ' + j + ' toppings')


#SANDWHICH 

# breads = ['whole wheat', 'sourdough']
# proteins = ['turkey', 'salmon', 'bean']

# for i in breads:
# 	for j in proteins:
# 		print(i + ', ' + j)


#PART 2
#MULT TABLE 1 - 10

# for i in range(1,11):
#     row = ""
#     for j in range(1,11):
#         row += str(i * j) + " "
#     print(row)

#MULT TABLE 11 - 15

# for i in range(11, 16):
#     row = ""
#     for j in range(11, 16):
#         row += str(i * j) + " "
#     print(row)


#PART 3
#AVG OF EACH STUDENT


marks = [[91, 82, 83],
	    [72, 84, 80],
	    [65, 90, 77]]
# for i in range(3):
#     total = 0
#     for j in range(len(marks[i])):
#         total += marks[i][j] 
#     avg = total / len(marks)
#     print("Average for row " + str(i) +  " is: "  + str(avg))

# #CLASS AVG
for i in range(len(marks[i])):
    total = 0
    for j in range(3):
        total += marks[j][i]
    avg = total / len(marks) 
    print("Class average for column " + str(i) + " is: " + str(avg))

#PART 4
#IMAGES

# img = [[(255, 0, 0), (255, 0, 0), (255, 0, 0)],
# 	  [(225, 0, 0),(225, 225, 225),(225, 0, 0)],
# 	  [(255, 0, 0), (255, 0, 0), (255, 0, 0)]]



# black = (0, 0, 0)
# white = (255, 255, 255)
# img = [[black, white, black, white, black],
# 	  [white, black, white, black, white],
# 	  [black, white, black, white, black]]
# count_black = 0
# for i in range(3):
# 	for j in range(5):
# 		if img[i][j] == black:
# 			count_black += 1
# print("Number of black pixels is: " + str(count_black))

#PART 5







