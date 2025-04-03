#-----------------------------------------------------------------------------
# Name:       Using Update and Discard (using_update_and_discard.py)
# Purpose:    To provide a program that adds and removes elements using update and discard
#
# Author:      Smrithi M
# Created:     02-Apr-2025
# Updated:     02-Apr-2025
#-----------------------------------------------------------------------------

# create a set of letters
letters = {'a', 'b', 'c'}

# update the set to include more letters
letters.update({'d', 'e', 'f'})

# remove b from the set
letters.discard('b')

# print the updated set
print(letters)