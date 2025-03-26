#-----------------------------------------------------------------------------
# Name:       Tuple Operations and Count (tuple_operations_and_count.py)
# Purpose:    To provide a program that counts how many times an item repeats in the tuple
#
# Author:      Smrithi M
# Created:     25-Mar-2025
# Updated:     25-Mar-2025
#-----------------------------------------------------------------------------

# create a tuple with repeating values
fruits = ('apple', 'banana', 'apple', 'cherry', 'banana', 'apple')

# ask the user to enter a fruit
fruit = input("Enter a fruit from the list: ")

# count how many times the fruit appears in the list
count = fruits.count(fruit)

# print the number of times it appears
print(fruit, 'appears in the tuple', count, 'times')