#-----------------------------------------------------------------------------
# Name:        Day of the Week Activity Recommender (dayOfTheWeekActivityRecommender.py)
# Purpose:     To provide a program that suggests an activity for the day of the week
#
# Author:      Smrithi Manoj
# Created:     25-Feb-2025
# Updated:     27-Feb-2025
#-----------------------------------------------------------------------------

# ask the user for the current day of the week
day = input("What day of the week is it? ")

# use a conditional to determine the activity based on day
if day == "Monday":
    print("Start your week with a workout!")
elif day == "Tuesday":
    print("It's a great day to read a book!")
elif day == "Wednesday":
    print("Mid-week movie night!")
elif day == "Thursday":
    print("Try a new recipe!")
elif day == "Friday":
    print("Relax and enjoy the weekend!")
elif day == "Saturday":
    print("Go for a hike!")
elif day == "Sunday":
    print("Prepare for the week ahead with some self-care.")
