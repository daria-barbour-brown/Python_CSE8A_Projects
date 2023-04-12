from CSE8AImage import *
from pa6 import *
#


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
    
#PART 3


def test_mirror():
    # TEST CASE:
    test_img1 = load_img("images/cat.jpg")
	# test_img1 = load_img("../images/cat.jpg")
	mod_img = mirror(test_img1)
	save_img(mod_img, "catMirrored.jpg")

    


def test_add_stamp():
    # TEST CASE:
    test_img1 = load_img("images/classified.jpg")
    test_img2 = load_img("images/classified_doc.jpg")
# test_img1 = load_img("../images/classified.jpg")
# test_img2 = load_img("../images/classified_doc.jpg")
	mod_img = add_stamp(test_img1, test_img2)
	save_img(mod_img, "classifiedStamped.jpg")


"""
OPTIONAL:
You can similarly create test functions for the other functions in pa6.
"""

def test_blend():
      # TEST CASE:
    test_img1 = load_img("images/cat.jpg")
    test_img2 = load_img("images/texture.jpg")
    blend(test_img1, test_img2)
    save_img(modified_image, "blendedCat")



"""
Calling the Test functions one after the other.
You may want to uncomment one test at a time.
"""

#test_mirror()
#test_add_stamp()
#test_blend()

