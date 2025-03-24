#-----------------------------------------------------------------------------
# Name:        Sum of Numbers (sum_of_numbers.py)
# Purpose:     To provide a program that adds the numbers in a range
#
# Author:      Smrithi M
# Created:     6-Mar-2025
# Updated:     17-Mar-2025
#-----------------------------------------------------------------------------

# ask the user for a number and store in the variable as an integer
number = int(input("Enter a number: "))

# sum variable to store the sum
sum = 0

# for loop that adds the range to the variable sum
for i in range(1, number + 1):
    sum += i

# print the final sum
print(sum)