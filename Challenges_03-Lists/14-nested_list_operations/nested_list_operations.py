#-----------------------------------------------------------------------------
# Name:       Nested List Operations (nested_list_operations.py)
# Purpose:    To provide a program that works with a nested list
#
# Author:      Smrithi M
# Created:     19-Mar-2025
# Updated:     20-Mar-2025
#-----------------------------------------------------------------------------

# create a list that contains data about students
students = [['Alice', 25, 'Physics'], ['Bob', 22, 'Chemistry'], ['Charlie', 24, 'Biology']]

# change Bob's age to 23
students[1][1] = 23

# change Bob's major to 'Mathematics'
students[1][2] = 'Mathematics'

# print the updated list
print("students =", students)

# use a for loop and conditional to access and print the name of the student who is studying biology
for student in students:
    if student[2] == 'Biology':
        print("the student studying Biology is", student[0])