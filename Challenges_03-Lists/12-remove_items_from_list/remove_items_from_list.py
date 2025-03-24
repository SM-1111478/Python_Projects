#-----------------------------------------------------------------------------
# Name:       Remove Items From List (remove_items_from_list.py)
# Purpose:    To provide a program that removes an item from a list
#
# Author:      Smrithi M
# Created:     19-Mar-2025
# Updated:     24-Mar-2025
#-----------------------------------------------------------------------------

# create a to-do list
toDoList = []

done = " "

# use a while loop to allow users to add tasks to the to-do list as long as they do not enter "no"
while done != "no":

    # prompts user to enter task to add to the to-do list
    newTask = input("Enter a task you want to add to your to-do list: ")

    # adds task to the list
    toDoList.append(newTask)

    # prints the updated list
    print("To-Do List:", toDoList)
    print(" ")

    # asks the user if they wish to add more tasks
    done = input("Do you want to add another task? (yes/no): ")

# prints the current to-do list
print("To-Do List:", toDoList)
print(" ")

remove = " "

# use a while loop to allow users to remove tasks from the to-do list as long as they do not enter "no"
while remove != "no":

    # prompts the user to enter task to remove from the to-do list
    taskToRemove = input("Enter a task you want to remove from your to-do list: ")

    # removes task from the list
    toDoList.remove(taskToRemove)

    # prints the updated list
    print("To-Do List:", toDoList)
    print(" ")

    # asks the user if they wish to remove more tasks
    remove = input("Do you want to remove another task? (yes/no): ")

# prints the final list
print("To-Do List:", toDoList)