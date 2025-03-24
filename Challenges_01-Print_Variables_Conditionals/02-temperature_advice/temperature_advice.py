#-----------------------------------------------------------------------------
# Name:        Temperature Advice (temperatureAdvice.py)
# Purpose:     To provide a program that issues suggestions based on the temperature
#
# Author:      Smrithi M
# Created:     24-Feb-2025
# Updated:     27-Feb-2025
#-----------------------------------------------------------------------------

# ask for the current temperature
temperature = int(input("What is the temperature today? "))

# use a conditional to give suggestion based on the temperature
if temperature < 10:
    print("It's cold outside. Wear a jacket!")
elif temperature <= 25 and temperature >= 10:
    print("It's a nice day. Wear short-sleeves!")
else:
    print("It's hot outside. Stay cool!")