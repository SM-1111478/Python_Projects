#-----------------------------------------------------------------------------
# Name:        Voting Eligibility Checker (votingEligibilityChecker.py)
# Purpose:     To provide a program that determines if the user is eligible to vote
#
# Author:      Smrithi M
# Created:     25-Feb-2025
# Updated:     27-Feb-2025
#-----------------------------------------------------------------------------

# ask the user's age
age = int(input("Enter your age: "))

# use a conditional to determine if the user is eligible to vote
if age >= 18:
    print("You are eligible to vote!")
else:
    print("Sorry, you are not eligible to vote yet.")