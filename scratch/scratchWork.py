#str = "Compile with favtutor"
# result = str.replace("f", "F")
# print(result)


#def power(num, exp):
# 	return num ** exp

# print(power(2,2))

#def print_greeting(hour):
# 	if (hour >= 0) and (hour <= 11):
# 		print("Good Morning")
# 	elif (hour >= 12) and (hour <= 18):
# 		print("Good Afternoon")
# 	elif (hour >= 19) and (hour <= 23):
# 		print("Good Evening")
# 	else:
# 		print("hour is invalid")


# print_greeting(12)
# print_greeting(20)
# print_greeting(-3)
# print_greeting(25)

#def sum_list(nums):
# 	sum = 0
# 	for num in nums:
# 		sum = sum + num
# 	return sum


# print(sum_list([2,1,2,3]))
# print(sum_list([]))


#pets = ["dog", "cat", "bird", "rat"]
# print(",".join(pets))

# string = "my name is daria"
# print(string.split(" "))


names= ["daria", "auden", "claire"]

def avg_name_lenght(names):
	sum = 0
	for name in names:
		sum = sum + len(names)
	avg = sum / float(len(names))
	return avg

print(avg_name_lenght(names))
print(16 / 3)