from CSE8AImage import *
from pa5 import *
import os
os.chdir("testResults")

"""
RGB codes for common colors. You can add on to this
if you want to experiment with different colors.
"""
black   = (0,0,0)
white   = (255,255,255)
red     = (255,0,0)
green   = (0,255,0)
blue    = (0,0,255)
yellow  = (255,255,0)
magenta = (255,0,255)
gray    = (128,128,128)
purple  = (128,0,128)

#PART 1.4

def test_complement():
    
    # TEST CASE 1:
    
    # Create a 100*100 image of magenta color and visualize it 
    test_img1 = create_img(100, 100, magenta)
    save_img(test_img1, "magenta_test_img1.jpg")
    # View the pixel values of the original image
    img_str_to_file(test_img1, "magenta_test_img1.txt")
    
    # Call complement and visualize the resulting image
    result1 = complement(test_img1);
    save_img(result1, "complement_result1.jpg")
    # View the pixel values of the filtered image
    img_str_to_file(result1, "view_complement_pixels.txt")


    # TEST CASE 2:
    
    # Load the cat image given and call complement on it
    cat = load_img("../images/cat.jpg")
    img = complement(cat)
    save_img(img, "complement_cat.jpg")


    # TEST CASE 3:
    # purple should stay the same 
    purple_img3 = create_img(200, 200, purple)
    img_str_to_file(purple_img3, "complement_purple_test.txt")
    save_img(purple_img3, "complement_test_purple_img3.jpg")
    result = complement(purple_img3);
    save_img(result, "complement_purple_result.jpg")
    img_str_to_file(result, "complement_purple_res.txt")
 
 


    
def test_negative():

    # TEST CASE 1:
    
    # Create a 100*100 image of red color and visualize it 
    test_img1 = create_img(100, 100, red)
    save_img(test_img1, "red_test_img1.jpg")
    # View the pixel values of the original image
    img_str_to_file(test_img1, "red_test_img1.txt")
    
    # Call negative and visualize the resulting image
    result1 = negative(test_img1);
    save_img(result1, "negative_result1.jpg")
    # View the pixel values of the filtered image
    #img_str_to_file(result1, "view_negative_pixels.txt")


    # TEST CASE 2:
    cat = load_img("../images/cat.jpg")
    img = negative(cat)
    save_img(img, "negative_cat.jpg")




    # TEST CASE 3:
    #negative of white should be black
    whiteImg = create_img(200, 200, white)
    save_img(whiteImg, "negWhiteTest.jpg")
    img_str_to_file(whiteImg, "negWhiteTest.txt")
    result = negative(whiteImg);
    save_img(result, "negWhiteRes.jpg")
    img_str_to_file(result, "negWhiteRes.txt")



    
    






"""
Calling the Test functions one after the other.
You may want to uncomment one test at a time.
OPTIONAL: You can add tests for the custom filters you have
created as part of Star points.
"""

#test_complement()
test_negative()
