#------Volume of Cylinder------

# import math


# def volumeOfCylinder(radius, height):
# 	volume = height * areaOfCircle(radius)
# 	print("Area of cylinder with radius " + str(radius) + " is " + str(volume))

# def areaOfCircle(radius):
# 	area = math.pi * (radius ** 2)
# 	return area

# volumeOfCylinder(10,2)

#-----Comma Deliminated------

# def addCSVNumbers(nums):
# 	#we have a list of strings, need to split
# 	lst = nums.split(',')
	
# 	sum = 0
# 	for s in lst:
# 		sum += int(s)
# 	return sum


# print(addCSVNumbers('85,95,60,75,55'))

#-----LIST TO STRING----

# def getNumbersCSV(lst):
# 	strLst = []
# 	for n in lst:
# 		strLst.append(str(n))
# 	return ','.join(strLst)

# print(getNumbersCSV([1,2,3,4,5]))

def find_element(word, word_list):
    idx_list = []
    for idx in range(len(word_list)):
        if word.lower() in word_list[idx].lower():
            return [idx]
    return idx_list

student_list1 = ['Alice', 'Chris', 'Hannah', 'Jack', 'Christine']
student1 = 'Chris'
print(find_element(student1, student_list1))



