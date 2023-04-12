# Lab 4
# Part 1
#Task 1.1 - 1.2

'''

def sum(nums):
    res = 0
    for x in range(len(nums)):
        res = res + nums[x] #first correction 
    return res

x = sum([10,2,3,2])
print(x)

'''
#Task 1.3

'''


def sum(nums):
    res = 0
    for x in range(0):
        res = res + x
    return res

x = sum([10,2,3,2])
print(x)


'''

# Part 2

'''

def main():
    res = 0
    for x in range(2,10):
        res = res + x
    return res

main()

print(main())

'''

#Part 3

'''

def sum_squares(nums):
    res = 0
    for x in range(len(nums)):
        square = nums[x] ** 2
        res = res + square
    return res

y = sum_squares([5,1,2])
print(y)

'''

# Part 4

'''

def count(nums, i):
    res = 0
    for x in range(len(nums)):
        if x == i:
            res = res + 1
    return res

y = count([5,1,2,1], 1)
print(y)

'''

#Part 5

'''

def f(num):
    i = 1
    s = 0
    while i <= num:
        s = s + i
        i = i + i
    return s

y = f(3)
print(y)

'''

# Part 6

'''

def sum_to_first_neg(nums):
    res = 0
    for i in nums:
        if i < 0:
            break

        res = res + i
    return res

y = sum_to_first_neg([9,-8,-4,13])
print(y)

'''


def prod_in_range(nums):
    s = 1
    for i in nums:
        if i < -10 or i > 10:
            break
        s = s * i
    return s

y = prod_in_range([1,3,-4,5])
print(y)



