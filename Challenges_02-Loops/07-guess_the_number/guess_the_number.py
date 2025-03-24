#-----------------------------------------------------------------------------
# Name:        Guess the Number (guess_the_number.py)
# Purpose:     To provide a program that prompts the user to guess a random pre-determined number
#
# Author:      Smrithi M
# Created:     5-Mar-2025
# Updated:     5-Mar-2025
#-----------------------------------------------------------------------------

# picking a random number
import random
number = random.randint(1, 10)

# create a variable to store the user's guess
userGuess = 0

# use a while loop to make the user guess till they get it correct
while userGuess != number:
    userGuess = int(input("Guess the number between 1 and 10: "))

# conditional to tell the user if the guess was correct or not
    if userGuess != number:
        print("Wrong, try again.")
    else:
        print("Correct!")