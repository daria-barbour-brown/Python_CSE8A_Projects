from CSE8AImage import *

#to save images to folder
# import os
# os.chdir("testImages")


#PART1 

#*****************************************

#takes in two 2D list reps of image
#sets value of each color component to be avg of corresponding pixel components
#(first_value + second_value) / 2
def blend(img1, img2):
    modified_image = []
    for row in range(height(img1)): #grab each row
        newRow = []
        for col in range(width(img1)): #from each col
            r = (img1[row][col][0] + img2[row][col][0])/2
            g = (img1[row][col][1] + img2[row][col][1])/2
            b = (img1[row][col][2] + img2[row][col][2])/2
            newRow.append((r, g, b))
        modified_image.append(newRow)
    # TODO Return the modified image
    return modified_image

#TESTING
# test_img1 = load_img("../images/cat.jpg")
# test_img2 = load_img("../images/texture.jpg")
# img = blend(test_img1, test_img2)
# save_img(img, "blendedCat.jpg")




#PART 2 
#*****************************************

#takes in 2D list rep of image
#returns 2D list rep of flipped on vertical axis
def mirror(img):
    modified_image = []
    w = width(img)-1 #end of row
    for r in range(height(img)):
        row = []
        for c in range(width(img)):
            row.append(img[r][w-c]) #move throught columns backwards
        modified_image.append(row)
    return modified_image

#TESTING
# img = load_img("../images/cat.jpg")
# mod_img = mirror(img)
# save_img(mod_img, "catMirrored.jpg")

#*****************************************

#takes in two 2D list rep of image 
#returns stap overlayed on background at top left corner
# topLeftRow = 0 ---row idx of background img
# topLeftCol = 0 ---col idx of background img where we want stamp overlaid
def add_stamp(stamp_image, background_image):
    modified_image = []
    for r in range(height(background_image)):
        row = []
        for c in range(width(background_image)):
            if(c < width(stamp_image)  and r < height(stamp_image)):
                row.append(stamp_image[r][c]) 
            else:
                row.append(background_image[r][c])  
        modified_image.append(row)
    
    return modified_image

#TESTING
# test_img1 = load_img("../images/classified.jpg")
# test_img2 = load_img("../images/classified_doc.jpg")
# mod_img = add_stamp(test_img1, test_img2)
# save_img(mod_img, "classifiedStamped.jpg")   

#*****************************************

#takes in 2D list rep, row and col index where we start crop, width and height of cropped img
#returns cropped img
def find_waldo(img, topLeftrow, topLeftcol, w, h):
    modified_image = []   # create an empty list
    for r in range(topLeftrow,topLeftrow+h):  #iterate from given starting row for length of h
        row = []  #create an empty list to compile each row
        for c in range(topLeftcol, topLeftcol+w):  #iterate from given starting col for length of given w
            row.append(img[r][c])  #add each of those pixels to the empty row list
        modified_image.append(row)  #add each new row to the empty 
    
    return modified_image

#TESTING
# test_img = load_img("../images/waldo.jpg")  #we load an image from images folder and save it into var
# mod_img = find_waldo(test_img, 486, 450, 70, 100)  #then send that test_img along with a starting row, col, and a w + h distt to travel
# save_img(mod_img, "croppedWaldo.jpg") #save the modified image

#*****************************************

#STAR POINTS

#takes in 2D list rep of img
#returns highlighted edges 
#computes gradient of each pixel (difference between current and prievious pixel)
#gradient((R1,G1,B1),(R2,G2,B2))= (abs(R2 - R1), abs(G2-G1), abs(B2-B1))
#determine gradient on x axis -> store in list1
#determine gradient on x axis -> store in list2
#add picelvalies of list1 + list2

# def edge_detection(img):



#     return modified_img


# data = [[10, 20, 30],
#         [40, 50, 60]]

# data.append([70, 80, 90])

# print(data)




