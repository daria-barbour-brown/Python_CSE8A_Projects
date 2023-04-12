import random
secret_number = random.randint(1, 100)



print("*** Guessing Game ***")
print("I am thinkng of a number between 1 and 100. Can you guess what it is?")

def findNumber(attempts):
	attemptsLeft = attempts
	while attemptsLeft > 0:
		playerGuess = int(input("Guess a number: "))
		attemptsLeft = attemptsLeft - 1
		if attemptsLeft == 0:
			print("Wrong! You are out of guesses. Goodbye.")
		elif playerGuess > secret_number:
			print("Guess lower! You have " + str(attemptsLeft) + " remaining.")
		elif playerGuess < secret_number:
			print("Guess higher. You have " + str(attemptsLeft) + " remaining.")
		elif playerGuess == secret_number:
			print("Correct! You win!")
			break
		
		

attempts = int(input("Enter how many attempts you want: "))
findNumber(attempts)

