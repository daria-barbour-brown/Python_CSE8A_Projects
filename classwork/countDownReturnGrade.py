
'''

def list_front9(nums):
    count = 0

    for val in nums:
        if val == 9:
            return True
        count = count +1
        if count >= 4:
            return False
    return false

print(list_front9([3,2,56,0,9]))

'''

'''

def list_front9(nums):
    for i in range(4):
        if nums[i] ==9:
            return True
    return False

print(list_front9([2,9,34,6]))

'''

'''

def countDown(num):
    s = ""
    for n in range(num, -1, -1):
        s = s + str(n) + " "
    print(s)


usersNum = int(input("Enter a number: "))
countDown(usersNum)

'''

def returnGrade(studentId, ids, grades):
    for i in range(len(ids)):
        if studentIf == ids[i]:
            return grades[i]
    return None



grades = [A,A,B,B,B,C]
idList = [A1, A2, A3, A4, A5, A6]
studentId = A3
returnGrade(studentId, idList, grades)