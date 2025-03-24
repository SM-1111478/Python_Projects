#-----------------------------------------------------------------------------
# Name:       Access and Modify List Items (access_and_modify_list_items.py)
# Purpose:    To provide a program that modifies a list by changing an exising item
#
# Author:      Smrithi M
# Created:     18-Mar-2025
# Updated:     21-Mar-2025
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
print(" ")
print("Grocery List:", groceryList)
print(" ")

# create a variable to store the response to whether the user wishes to replace any items
replace = input("Do you wish to replace an item? (yes/no): ")

# use a while loop to allow users to replace item as long as they do not enter "no"
while replace != "no":

    # create a variable to store the number of the item the user wishes to replace
    itemToReplace = int(input("Enter the number of the item you wish to replace: "))

    # subtract 1 from the number because the index begins at 0
    itemToReplace -= 1

    # prompt the user to enter the new item and replace it with the one they wish to replace
    groceryList[itemToReplace] = input("Enter the new item: ")
    print(" ")

    # print the current grocery list
    print("Grocery List:", groceryList)

    # ask the user if they wish to replace any other items (while loop ends if they enter "no")
    replace = input("Do you wish to replace another item? (yes/no): ")

# print the updated list
print(" ")
print("updated grocery list:", groceryList)

# access the third item in the list and print it
print(" ")
print("item 3 in the grocery list:", groceryList[2])