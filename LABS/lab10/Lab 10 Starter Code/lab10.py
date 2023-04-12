import csv


# Function to get the film data, 
# DO NOT EDIT THIS FUNCTION
def get_film_data(filename): #list of dicts
    data = []
    with open(filename) as f:
        for row in csv.DictReader(f):
            row_dict = {k: v for k, v in row.items() if k != '\ufeffcountry'}
            data.append(row_dict)
    return data


# film_data contains the list of dictionaries now.
film_data = get_film_data('Netflix_movies_data.csv')


# Task 1.1 --------------------------------------------------
#returns number of weeks movie or show in top 10 ranking
def find_number_of_weeks(movie):
    weeks = 0
    for dict in film_data:
        if dict["show_title"] == movie:
            if int(dict["weekly_rank"]) <= 10:
                weeks = weeks + 1
            
            
    return weeks

# print(find_number_of_weeks("Squid Game"))

# Task 1.2 -----------------------------------------------
def get_avg_rank(movie):
    weeks = 0
    total_rank = 0    
    for dict in film_data:
        if dict["show_title"] == movie:
            total_rank = total_rank + int(dict["weekly_rank"])
            weeks = weeks + 1
    avgRank = round(total_rank / weeks)


    return avgRank

# print(get_avg_rank("Red Notice"))


# Task 1.3
import matplotlib.pyplot as plt

movie_list = ["You", "Maid", "Arcane", "Army of Thieves"]

#create list of weeks
weeks =[]
for el in movie_list:
    weeks.append(find_number_of_weeks(el))
#print(weeks)


# plt.pie(weeks, autopct='%1.1f%%', labels = movie_list, frame =True)
# plt.show()

def print_left_half(img):
    for row in range(len(img)):
        for col in range(len(img[row])//2):
            print(img[row][col])

img = [[(255,0,0), (0,255, 255), (255, 255, 255), (0,0,0)],
       [(255,0,0), (0,255, 255), (255, 255, 255), (0,0,0)], 
       [(255,0,0), (0,255, 255), (255, 255, 255), (0,0,0)]]
#print_left_half(img)

def num_positives(lst):
    count = 0
    for thing in lst:
        for el in thing:
            if el > 0:
                count = count +1 
    return count

print(num_positives([[1, 10, 20], [40, 60, 3]]))