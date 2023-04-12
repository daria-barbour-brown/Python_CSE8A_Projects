''' 

myList = [3,2,5,6]

def first_last6(myList):
    if myList[0] == 6:
        return True
    if myList[len(myList - 1)] == 6:
        return True
    else:
        return False

print(firts_last6(myList)


a = [42,33,3,6,9,284,0]
b = [42,2,1,55]

def common_end(a, b):
    if a[0] == b[0]:
        return True
    return False

print(common_end(a,b))



student_id = 3
idList = [1,2,3,4]
classGrades = [45,67,99,100]

def grade(student_id,idList,classGrades):
    if student_id == idList[0]:
        return classGrades[0]
    if student_id == idList[1]:
        return classGrades[1]
    if student_id == idList[2]:
        return classGrades[2]
    if student_id == idList[3]:
        return classGrades[3]
    if student_id == idList[4]:
        return classGrades[4]
    return None

print(grade)



[4,3,33,1,29,18]

def rotate_left(nums):
    temp = nums[0]
    nums[0] = nums[1]
    nums[1] =nums[2]
    nums[2] = temp
    return nums

print(rotate_left([4,3,33]))
    
'''

def drink_order():
    selection = input("Whar size drink would you like? "

    if selction == "XS":
        return 1.0
    elif selection == "S"
        return 1.5
    elif selection == "M"
        return 2.0
    elif selection == "L"
        return 2.5
    elif selection == "XL"
        return 3






    print("Invalid size")
    return 0


print(drink_order())
    
        

