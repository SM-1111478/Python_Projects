#-----------------------------------------------------------------------------
# Name:        Even or Odd Number Checker (evenOrOddNUmberChecker.py)
# Purpose:     To provide a program that determines if a number is even or odd
#
# Author:      Smrithi Manoj
# Created:     25-Feb-2025
# Updated:     27-Feb-2025
#-----------------------------------------------------------------------------

# ask the user for a number
number = int(input("Enter a number: "))

# determine if it is even or odd by dividing by 2 and checking if the remainder is 0
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")