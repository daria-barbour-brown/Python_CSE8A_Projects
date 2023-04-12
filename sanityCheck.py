
def num_positives(lst):
    count = 0
    for thing in lst:
        for el in thing:
            if el > 0:
                count = count +1 
    return count

# print(num_positives([[1, 10, 20], [40, 60, 3]]))

# def negate_checkered(img):
#     newImg = []
#     for row in len(img):
#         newRow = []
#         for col in len(img[row]):
#             if col == (0,0,0):
#                 newRow[col] = (255, 255, 255)
#             else:
#                 newRow[col] = (0,0,0)
#         newImg[row] = newRow
#     return newImg

def negate_checkered(lst):
    newList = [] #list of lists
    for i in range(len(lst)):
        rowList=[]
        for j in range(len(lst[i])):
            if lst[i][j] == (255,255,255):
                rowList.append((0,0,0))                #change to black
            elif lst[i][j] == (0,0,0):
                rowList.append((255,255,255))         #change to white
            else:
                rowList.append(lst[i][j])              # no change
        newList.append(rowList)
    return newList

#print(negate_checkered([[(0, 0, 0), (255, 255, 255), (0, 0, 0), (255, 255, 255)], 
#  						[(255, 255, 255), (0, 0, 0), (255, 255, 255), (0, 0, 0)], 
#  						[(0, 0, 0), (255, 255, 255), (0, 0, 0), (255, 255, 255)]]))
def negate_checkered1(l):
    new_list = []
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] == (255,255,255):
                new_list[i][j] = (0,0,0)                #change to black
            elif l[i][j] == (0,0,0):
                new_list[i][j] = (255,255,255)          #change to white
            else:
                new_list[i][j] = l[i][j]         
    return new_list
    

# print(negate_checkered1([[(1,1,1),(0,0,0),(55,22,42)],
#     [(255,255,255),(43,43,55),(71,71,71)],
#     [(123,222,212),(255,255,0),(0,0,0)]]))

def green_filter(img):
    for row in range(len(img)):
        for col in range(len(img[row])):
            r,g,b = img[row][col]
            img[row][col] = (0,g,0)
    return img

#print(green_filter([[(10, 20, 30), (40, 50, 60)], [(70, 80, 90), (100, 110, 120)]]))


def green_filter2(img):
    for row in range(len(img)):
        for col in range(len(img[row])):
            img[row][col] = (0, img[row][col][1], 0)
    return img

#print(green_filter2([[(10, 20, 30), (40, 50, 60)], [(70, 80, 90), (100, 110, 120)]]))

houses = {'Gryffindor': ('Harry Potter', 'Hermione Granger', 'Ron Weasley'), 
          'Ravenclaw': ('Luna Lovegood', 'Cho Chang', 'Padma Patil'), 
          'Hufflepuff':('Pomona Sprout', 'Cedric Diggory', 'Nymphadora Tonks'), 
          'Slytherin':('Severus Snape', 'Draco Malfoy', 'Tom Riddle')}

courses = { 'bash': {'classes': 20, 'hours': 2, 'fee': 50},
            'PHP': {'classes': 10, 'hours': 2, 'fee': 150},
            'Angular': {'classes': 25, 'hours': 2, 'fee': 100},
            'Python': {'classes': 15, 'hours': 2, 'fee': 100}
          }

sum = 0
for v in courses.values():
    sum += v['classes']

print(sum)
