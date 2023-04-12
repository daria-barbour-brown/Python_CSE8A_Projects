data = [[77, 77, 76, 74, 73],
        [85, 85, 78, 81, 81],
        [104, 106, 101, 97, 97]]

# def get_a_days_weather(wdata, day):
# 	cities = ["LA", "Portland", "OKC"]
#     #if day < 0 or day  > 4:
#     if day < 0 or day  >= len(wdata[0]): #if we wanted to change code to seven days
#     	return "day " + str(day) + " is invalid!"
    
#     # result = []
#     # for i in range(len(cities)):
#     # 	result += wdata[i][day]

#     #tuple version

#     result = (wdata[0][day], wdata[1][day], wdata[2][day])
#     return result


# def get_hottest_days(wdata):
# 	list_result = []
	
# 	for city in wdata:
#     	largest_index = 0
    	
#     	for day in range(len(city)):
#     		if city[day] > city[largest_index]:
#     			largest_index = day
#     	list_result.append(largest_index)
   	

#    	return (list_result[0], list_result[1], list_result[2])


# print(get_hottest_days(data))

# from CSE8AImage import *
# def redFilter(img):
# 	for row in range(height(img)):
# 		for col in range(width(img)):
# 			g = img[row][col][1]
# 			b = img[row][col][2]
# 			img[row][col] = (0,g,b)
# 	return

data = [[10, 20, 30, 40],
        [50, 60, 70, 80],
        [90, 100, 110, 120],
  [130, 140, 150, 160]]

for i in range(len(data)-2, -1, -2):
    for j in range(len(data[i])-2, -1, -1):

    	print(data[j][i],)
    print("_______\n")
    










