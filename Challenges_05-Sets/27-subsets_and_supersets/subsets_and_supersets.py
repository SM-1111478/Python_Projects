#-----------------------------------------------------------------------------
# Name:       Subsets and Supersets (subsets_and_supersets.py)
# Purpose:    To provide a program that checks if one set is fully contained in the other
#
# Author:      Smrithi M
# Created:     02-Apr-2025
# Updated:     02-Apr-2025
#-----------------------------------------------------------------------------

# create 2 sets
setA = {1, 2, 3, 4, 5}
setB = {2, 3, 4}

# check if set A is a superset of set B
if setA.issuperset(setB):

# print "True" if it is a superset
    print("True")

# print "False" if not a superset
else:
    print("False")

# check if set B is a subset of set A
if setB.issubset(setA):

# print "True" if it is a subset
    print("True")

# print "False" if not a subset
else:
    print("False")