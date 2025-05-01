#-----------------------------------------------------------------------------
# Name:       Simple Function (simple_function.py)
# Purpose:    To provide a program that uses a simple function
#
# Author:      Smrithi M
# Created:     30-Apr-2025
# Updated:     30-Apr-2025
#-----------------------------------------------------------------------------

# define a function that prints "Hello, world!"
def say_hello():
    print("Hello, world!")

# print what the function does
print("Displays 'Hello, world!': ")

# call the function to print "Hello, world!"
say_hello()

print()

# define a function to display a sentence input by the user
def say_something(sentence):
    print(sentence)

# create a variable to store the user input
userInput = input("Enter a sentence to display: ")

# call the function to print the user input
say_something(userInput)