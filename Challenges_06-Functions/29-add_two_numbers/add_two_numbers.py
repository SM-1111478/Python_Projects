#-----------------------------------------------------------------------------
# Name:       Add Two Numbers (add_two_numbers.py)
# Purpose:    To provide a program that uses a function to add two numbers
#
# Author:      Smrithi M
# Created:     30-Apr-2025
# Updated:     30-Apr-2025
#-----------------------------------------------------------------------------

# define a function that adds two numbers and returns the sum
def add_numbers(num1, num2):
    sum = num1 + num2
    return sum

# get user input for the first number and store in a variable
firstNum = int(input("Enter the first number to add: "))

# get user input for the second number and store in a variable
secondNum = int(input("Enter the second number to add: "))

# call the function to print the sum using variables storing the user input numbers as parameters
print("The final sum is:", add_numbers(firstNum, secondNum))