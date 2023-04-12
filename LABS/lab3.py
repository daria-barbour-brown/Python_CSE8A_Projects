#LAB 3

# Part 1

'''

nums = [10,-3,5,1,4,8,7]
idx = -1
x = nums[idx]


print(x)

'''

# Part 2

'''

x = int(1.2)
y = int(7.8)
z = int(2.9)

print(x)
print(y)
print(z)



nums = [1,2,3,4,5]
mid = len(nums) / 2
mid_val = nums[int(mid)]

print(mid_val)

'''

# Part 3

'''

numbers = [10, 2, 3, 2, -1, 4]
x = sum(numbers)

y = sum(numbers[0:2])

z = sum(numbers[2:])

print(x)
print(y)
print(z)

'''

# Part 4

'''

def checkForLetter(word):
    if "e" in word:
        return "The letter e exists in your word."

string = input("Please enter a word: ")

checkForLetter(string)



sentence = "Hello,Good,Afternoon."
x = sentence.index(",")
print(sentence[x+1:])



anotherSentence = "Hello, have a good day."
x = anotherSentence.replace("a", "")
print(x)


userInput = input("Enter words: ")
upperCase = userInput.upper()
print(upperCase)


name = "apple"
firstLetter = name[0]
x = firstLetter.upper()
print(x + name[1:])

'''

name = "Daria Brown"
length = ( int[len(name) -1] / 2)
print(length)





