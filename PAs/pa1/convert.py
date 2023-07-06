#PA1: Ounces to Grams

#Function to convert ounces to grams

def ounces_to_grams(weight_in_oz):
    #conversion: 1oz = 28.35g
    result1 = weight_in_oz * 28.35
    return result1

#Function to convert grams to ounces

def grams_to_ounces(weight_in_g):
    #conversion: 1oz = 1 / 28.35g
    result2 = weight_in_g / 28.35
    return result2

# weight_in_oz_str = input("Enter weight in oz: ") #getting user input
# weight_in_oz = float(weight_in_oz_str)           #convert user's string to float
# weight_in_g = ounces_to_grams(weight_in_oz)      #calling function and storing its result
# print("Weight in grams =" , weight_in_g)         #print

# #convert back to ounces

# convert_back = grams_to_ounces(weight_in_g)     
# print("Weight converted back to ounces =" , convert_back)

# conversion is the same up to a certain decimal, always some level of inacuracy
#if we restricted our results to a smaller number of decimals we would get same answer
