#-----------------------------------------------------------------------------
# Name:       Set Operations (set_operations.py)
# Purpose:    To provide a program that performs set operations
#
# Author:      Smrithi M
# Created:     02-Apr-2025
# Updated:     02-Apr-2025
#-----------------------------------------------------------------------------

# create 2 sets of numbers
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# combine the sets
union = set1.union(set2)
print("Union:", union)

# find the numbers in both sets
intersection = set1.intersection(set2)
print("Intersection:", intersection)

# find the numbers that are in set 1 but not set 2
difference = set1.difference(set2)
print("Difference:", difference)

# find the numbers that are in set 2 but not set 1
difference = set2.difference(set1)
print("Difference:", difference)