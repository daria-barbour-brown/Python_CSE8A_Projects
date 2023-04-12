
from CSE8AImage import *
import os
os.chdir("testImages")

def filter_colors(img, colors):
	for r in range(height(img)):
		for c in range(width(img)):
			pixel = img[r][c]

			#img[r][c] = colors[pixel] would not work because not all pixel colors are in palette
			#is pixel in pallet?
			if pixel in colors:
				img[r][c] = colors[pixel]


	return img

w = (255, 255, 255)
bk = (0, 0, 0)
img = load_img("../santa_new.png")

#create a palette to swap black and white colors
palette = {}
palette[w] = bk
palette[bk] = w

#bonus: extend palette to also swap red and green colors

#mod_img = filter_colors(img, palette)
#save_img(mod_img, "filter_color_new.jpg")

#-----------------------------------------

#takes a list of words
#returns a dictionary: word length as the key, list of words (of that word length) as the value
def word_length(words):
	result = {}

	for word in words:
		length = len(word)
		if length not in result:
			result[length] = [word]
		else:
			result[length].append(word)


	return result

w = [ "a", "bb", "c", "dd", "eee" ]
dict = word_length(w)
#print(dict)

#---------------------------------------
#takes a list of phrases
#returns a dictionary: phrase as the key, a list of words that makeup that phrase as the value
def phrase_contents(phrases):
	result = {}
	for phrase in phrases:
		words = phrase.split(" ")
		result[phrase] = words

	return result

lst = ["CSE 8A Rocks", "UCSD", "University of California San Diego"]
dict = phrase_contents(lst)
print(dict)





