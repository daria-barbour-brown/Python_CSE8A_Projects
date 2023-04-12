#PART 0
from CSE8AImage import *

marks = [[91, 82, 83, 45, 34], 
		[72, 84, 80, 43, 29],
		[65, 90, 77, 89, 19]]
students = ["A", "B", "C"]
classes = ["C1", "C2", "C3", "C4", "C5"]


# #avg of each student 
# for i in range(3):
#     total = 0
#     for j in range(len(marks[i])):
#         total += marks[i][j]
#     avg = total / len(marks[i])
#     print("Average for student " + students[i] + " is: "  + str(avg))

# #avg of each class
# for i in range(len(marks[i])):
#     total = 0
#     for j in range(3):
#         total += marks[j][i]
#     avg = total / len(marks)
#     print("Average for class" + classes[j] + " is: "  + str(avg))


#print alphabet 
# for i in range(0,6):
# 	for j in range(0, i+2):
# 		while k in range(65, 92):
# 		print(chr(k))


#print 1-10 5 times

# i = 1
# while (i <= 5):
# 	j = 1
# 	while(j<=10):
# 		print(j)
# 		while 
# 	i += 

#PART 1
#passing and returning image

#grey scale filter
def grey_scale(img):
	for row in range(height(img)): #step through each row
		for col in range(width(img)): #for each row look through all columns
			r, b, g = img[row][col]
			img[row][col] = int((r + g + b) / 3) #now save r, blue and green new into current tuple
	return img

img = load_img("../images/BLM.jpg")
new_img = gray_scale(img)


