#PART 1 
#CHANGING FOR LOOP T WHILE LOOP

# SUMS ALL NUMBERS IN LIST
# def sum_for(nums):
#     res = 0
#     for i in range(len(nums)):
#         res = res + nums[i]
#     return res

# x = sum_for([10,2,3,2])

# print(x)

#def sum_while(nums):
#     res = 0
#     i = 0
#     while i < len(nums) :
#         res = res + nums[i]
#         i += 1
#     return res

# x = sum_while([10,2,3,2])

# print(x)

#LIST SPLITTING 
#names = "Jane;Juan;Leilani;Jose;Kayla"
# name_list = names.split(";")

# print(name_list)

#GET GRADE
#r = "jane:234212:A+"

# def grade(record):
#    data = r.split(':')
#    print(data)
#    res = data[-1]
#    return res

# g = grade(r)

# print(g)

#COMBINED LIST
# combined_list = []
# num = 5
# for i in range(1, num+1):
#     combined_list.append(i)

# print(combined_list)

#ADD TWO LISTS ELEMENTS
def add_two_lists(lst1, lst2):
	sum_list = []
	if len(lst1) != len(lst2):
		return "Cannot add lists of different sizes!"
	for i in range(len(lst1)):
		if type(lst1[i]) != type(lst2[i]):
			return "Cannot add elements of different types!"
		sum_list.append(lst1[i] + lst2[i])
	return sum_list



#print(add_two_lists([1, 2, 3], ['a', 'b', 'c','d']))
   #Cannot add lists of different sizes!
#print(add_two_lists([1,2],[4,5]))
   #[5, 7]
#print(add_two_lists([1,2],[3,4,5]))
   #Cannot add lists of different sizes!
#print(add_two_lists([],[]))
   #[]
print(add_two_lists([1, 2, "a"],[3, 4, "b"]))
   #[4, 6, 'ab']
# print(add_two_lists([1, 2, "a", 2],[3, 4, "b"]))

























