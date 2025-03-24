#-----------------------------------------------------------------------------
# Name:       Sorting and Reversing Lists (sorting_and_reversing_lists.py)
# Purpose:    To provide a program that sorts and reverses lists
#
# Author:      Smrithi M
# Created:     20-Mar-2025
# Updated:     20-Mar-2025
#-----------------------------------------------------------------------------

# create a list of fruits
fruits = ['banana', 'apple', 'grape', 'kiwi', 'orange']

# print the list
print("original list =", fruits)

# sort the list in alphabetical order (ascending)
fruits.sort()

# print the sorted list
print("sorted list =", fruits)

# sort the list in alphabetical order (descending)
fruits.sort(reverse=True)

# print the sorted list
print("reverse list =", fruits)