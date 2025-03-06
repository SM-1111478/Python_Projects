#-----------------------------------------------------------------------------
# Name:        Countdown Timer (countdown_timer.py)
# Purpose:     To provide a program that counts from 10 to 1 till the user enters stop
#
# Author:      Smrithi Manoj
# Created:     6-Mar-2025
# Updated:     6-Mar-2025
#-----------------------------------------------------------------------------

# stop variable to check if the user entered "stop"
stop = " "

# counter variable to store the countdown number
counter = 10

# while loop that counts down until the user enters "stop" or countdown reaches 1
while stop != "stop":
    print(counter)
    counter -= 1
    stop = input("Enter 'stop' to cancel or press enter to continue: ")
    if stop == "stop":
        break
    elif counter == 0:
        break

# print if the user enters "stop" or if countdown reaches 1
print("Countdown stopped")