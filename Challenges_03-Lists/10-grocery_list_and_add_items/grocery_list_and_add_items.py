#-----------------------------------------------------------------------------
# Name:        Grocery List and Add Items (grocery_list_and_add_items.py)
# Purpose:     To provide a program that creates a grocery list and adds items to the end
#
# Author:      Smrithi M
# Created:     18-Mar-2025
# Updated:     20-Mar-2025
#-----------------------------------------------------------------------------

# create a grocery list
groceryList = []

done = " "

# use a while loop to allow users to add items to the grocery list as long as they do not enter "no"
while done != "no":

    # prompts user to enter item to add to the grocery list
    newItem = input("Enter an item you want to add to your grocery list: ")

    # adds item to the list
    groceryList.append(newItem)

    # prints the updated list
    print("Grocery List:", groceryList)
    print(" ")

    # asks the user if they wish to add more items
    done = input("Do you want to add another item? (yes/no): ")

# prints the final grocery list
print("Grocery List:", groceryList)
