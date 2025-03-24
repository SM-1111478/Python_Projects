#-----------------------------------------------------------------------------
# Name:        Student Grading System (studentGradingSystem.py)
# Purpose:     To provide a program that states the letter grade based on the number grade
#
# Author:      Smrithi M
# Created:     24-Feb-2025
# Updated:     27-Feb-2025
#-----------------------------------------------------------------------------

# display the name of the program
print("Student Grading System")

# ask for user's number grade
grade = int(input("Enter your grade: "))

# use a conditional to give the user their letter grade based on the score they entered
if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
elif grade >= 60:
    print("Grade: D")
else:
    print("Grade: F")