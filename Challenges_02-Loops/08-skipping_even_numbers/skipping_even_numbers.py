#-----------------------------------------------------------------------------
# Name:        Skipping Even Numbers (skipping_even_numbers.py)
# Purpose:     To provide a program that prints even numbers from 1 to 10
#
# Author:      Smrithi M
# Created:     5-Mar-2025
# Updated:     6-Mar-2025
#-----------------------------------------------------------------------------

# use a for loop to print the numbers from 1 to 10
for i in range(1, 11):

# use a conditional to check if the number is even and continue statement to skip the current number
    if i % 2 == 0:
        continue
    print(i)