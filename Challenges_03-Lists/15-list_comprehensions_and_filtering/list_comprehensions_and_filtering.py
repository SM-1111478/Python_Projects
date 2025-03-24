#-----------------------------------------------------------------------------
# Name:       List Comprehensions and Filtering (list_comprehensions_and_filtering.py)
# Purpose:    To provide a program that uses list comprehensions to filter data based on a condition
#
# Author:      Smrithi M
# Created:     20-Mar-2025
# Updated:     20-Mar-2025
#-----------------------------------------------------------------------------

# create a list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print original list
print("original list =", numbers)

# create a new list with only even numbers from the original list
evenNumbers = [num for num in numbers if num % 2 == 0]

# print the new list
print("even numbers =", evenNumbers)

# create a new list with squares of all the even numbers
squaredNumbers = [num ** 2 for num in evenNumbers]

# print the new list
print("squared numbers =", squaredNumbers)