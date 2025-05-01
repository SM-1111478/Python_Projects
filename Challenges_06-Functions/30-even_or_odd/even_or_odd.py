#-----------------------------------------------------------------------------
# Name:       Even or Odd (even_or_odd.py)
# Purpose:    To provide a program that uses a function to tell if a number is even
#
# Author:      Smrithi M
# Created:     1-May-2025
# Updated:     1-May-2025
#-----------------------------------------------------------------------------

# define a function to check if a number is even
def is_even(number):

# use a conditional to check if the number is divisible by 2
    if number % 2 == 0:

# return True if yes
        return True

# return False if not
    else:
        return False

# create a variable to store the user input of the number to check
num = int(input("Enter a number to check if it is even: "))

# call the function and print the result using the user input variable as the parameter
print("The number is even:", is_even(num))