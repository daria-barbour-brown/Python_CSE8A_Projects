from CSE8AImage import *
import random
import math

def pattern(img, start_row, start_col, length):
    end_row = start_row + length
    end_col = start_col + length
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if r >= end_row / 2:
                img[r][c] = (255, 0, 0)
            if c >= end_col / 2:
                img[r][c] = (0, 255, 0)
            if c <= end_col / 2:
                img[r][c] = (225, 0, 0)
            if r < end_row / 2:
                img[r][c] = (0, 0, 255)


def checker_pattern(img, start_row, start_col, length):
    end_row = start_row + length
    end_col = start_col + length
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if (r < end_row / 2) and (c < end_col / 2):
                img[r][c] = (255, 0, 0) #red
            elif (r < end_row / 2):
                img[r][c] = (0, 0, 255) #blue
            elif (c < end_col / 2):
                    img[r][c] = (0, 255, 0) #green
            else:
                img[r][c] = (255,255,0) #yellow

def checkerFilter(img, start_row, start_col, length):
    if start_row >= height(img) or start_col >= width(img) or start_row < 0 or start_col < 0:
        print("Start row/col is invalid.")
        return None

    if start_row + length > height(img):
        end_row = height(img)
    else:
        end_row = start_row + length
    if start_col + length > width(img):
        end_col = start_col + length

    end_row = start_row + length
    end_col = start_col + length

    mid_row = start_col + (end_row - start_row) / 2
    mid_col = start_col + (end_col - start_col) / 2


    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            pix = img[r][c]
            if (r < mid_row) and (c < mid_col):
                img[r][c] = (pix[0], 0, 0) #red
            elif (r < mid_row):
                img[r][c] = (0, 0, pix[2]) #blue
            elif (c < mid_col):
                    img[r][c] = (0, pix[1], 0) #green
            else:
                img[r][c] = (pix[0],pix[1],0) #yellow

#*********FIX


# img = load_img("cat.jpg")
# checkerFilter(img, 0, 0, height(img))
# save_img(img, "transformation.png")


#RECTANGLE
def white_Image(width, height):
    result = []

    for row in range(height):
        row_list = []
        white = (255, 255, 255)

        for col in range(width):
            row_list = .append(white)

        result.append(row_list)
        #result += [row_list]
    rerurn result

def draw_rect(img, start_row, start_col, width, height, col):

    return img
    pass
# *********FIX

def distance(p1x, p1y, p2x, p2y):
    sum = (p2x - p1x)**2 + (p2y - p1y)**2
    return math.sqrt(sum)

def draw_circle(img, center_row, center_col, radius, color):
    for row in range(0, height(img)):
        for col in range(start_col, end_col):
            img[row][col] = color
    return None

img = white_image(1000, 1000)
draw_rectangle(img, 2, 2, 6, 6, (255, 0, 0))
#draw_circle(img, 4, 4, 3, (255, 0, 0))
#draw_circle(img, 400, 400, 300, (255, 0, 0))
save_img(img, 'drawing.jpg')


def mystery(img):
    h = height(img)

#flips img left to right
for y in range(len(img)):
    for x in range(len(img[y])//2):
        temp = img[y][x]
        img[y][x] = img[y][len(img[y])-x-1]
        img[y][len(img[y])-x-1] = temp










