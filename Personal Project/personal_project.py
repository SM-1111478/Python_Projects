#-----------------------------------------------------------------------------
# Name:       Personal Project (personal_project.py)
# Purpose:    To provide a text-based escape room game
#
# Author:      Smrithi M
# Created:     20-May-2025
# Updated:     12-Jun-2025
#-----------------------------------------------------------------------------

# list to track inventory
inventory = []

# set to track the rooms already visited
visited_rooms = set()

# function to start the game
def start_game():
    print("The goal is to escape the house. Pick one of the choices in the parentheses. If you die, you will have to "
          "restart from the beginning, so choose wisely.")
    input("Press Enter to start")
    print("")
    print("You stand in front of the old abandoned house your friends dared you to enter. No one has lived in the "
          "house for decades.")
    print("Everyone believes the house is haunted, but you don’t believe in ghosts.")
    print("You take a step forward, unsure.")
    print("")
# loop for the choice that runs as long as the input is invalid
    while True:
        choice = input("Are you sure you wish to enter? (yes / no): ").lower()
# conditional based on user input for next move
        if choice == "no":
            print("You turn around and walk back home. Your friends make fun of you for the rest of your life.")
            play_again()
            break
        elif choice == "yes":
            print("You walk up to the door and step inside.")
            foyer()
            break
        else:
            print("Invalid choice.")
            print("")

# function for when foyer is entered
def foyer():
# conditional that runs if room is visited for the first time
    if "foyer" not in visited_rooms:
        visited_rooms.add("foyer")
        print("")
        print("Suddenly, the door slams shut behind you. You jump, knocking into a picture frame hung on the wall.")
        print("The frame falls to the floor, revealing the numbers \033[95m\033[1m5372\033[0m behind it.")
        print("A code of some kind? This could be useful.")
        print("")
        print("There is a door ahead of you that seems to lead into a long hallway, and behind you is the door you "
            "entered through.")
        choice = " "
# loop for the choice that runs as long as the input is invalid
        while choice != "north":
            print("")
            choice = input("Do you go north into the hallway or south back through the entrance? (north / south): ").lower()
# conditional based on user input for next move
            if choice == "south":
                print("")
                print("You try the entrance door, but it’s locked. Looks like you’ll have to find another way out.")
            elif choice == "north":
                south_hallway()
            else:
                print("Invalid choice.")
                print("")
# runs if room is revisited
    else:
        print("")
        print("You're back in the foyer. You look at the numbers on the wall. \033[95m\033[1m5372\033[0m.")
        south_hallway()

# function for when south hallway is entered
def south_hallway():
# conditional that runs if room is visited for the first time
    if "south hallway" not in visited_rooms:
        visited_rooms.add("south hallway")
        print("")
        print("You walk through the door in front of you, into a long hallway.")
        print("You see a door to your left leading to a library and one to your right leading to a dining room.")
        print("You also see other rooms farther down the hallway.")
        print("")
# runs if room is revisited
    else:
        print("")
        print("You're back at the south end of the hallway.")
        print("")
# loop for the choice that runs as long as the input is invalid
    while True:
        choice = input("Do you go west into the library, east into the dining room, south into the foyer, "
                           "or to the north end of the hallway? (east / west / south / north): ").lower()
# conditional based on user input for next move
        if choice == "west":
            library()
            break
        elif choice == "east":
            dining_room()
            break
        elif choice == "north":
            north_hallway()
            break
        elif choice == "south":
            foyer()
            break
        else:
            print("Invalid choice.")
            print("")

# function for when library is entered
def library():
# conditional that runs if room is visited for the first time
    if "library" not in visited_rooms:
        visited_rooms.add("library")
        print("")
        print("You walk into the library when, suddenly, a book comes flying at your face.")
        print("")
# loop for the choice that runs as long as the input is invalid
        while True:
            choice = input("What do you do? (duck / freeze): ").lower()
            print("")
# conditional based on user input for next move
            if choice == "duck":
                print("You duck just in time to avoid the book, which hits the wall behind you.")
                print("You take a look around the room. You’re in a library with a large bookshelf filled with old "
                      "books.")
                print("You scan the bookshelf and find a small black safe at the very bottom.")
                print("You inspect the safe and notice it requires a passcode with \033[94m\033[1m4 digits\033[0m.")
                print("")
                passcode = " "
# loop for the choice that runs as long as the input is incorrect
                while passcode != 5372:
                    passcode = int(input("Enter the passcode: "))
# conditional based on user input for passcode
                    if passcode == 5372:
                        print("The safe door swings open, revealing a shiny \033[4mgolden key\033[0m laying inside.")
                        print("You pocket the key and go back into the hallway.")
                        inventory.append("gold_key")
                        south_hallway()
                    else:
                        print("The safe beeps and the screen displays the word \033[91m\033[1m'Incorrect'\033[0m.")
                break
            elif choice == "freeze":
                print("The book hits you in the face and you die.")
                play_again()
                break
            else:
                print("Invalid choice.")
                print("")
# runs if room is revisited
    else:
        print("")
        print("You're back in the library. You look around but find nothing.")
        south_hallway()

# function for when dining room is entered
def dining_room():
# conditional that runs if room is visited for the first time
    if "dining room" not in visited_rooms:
        visited_rooms.add("dining room")
        print("")
        print("You walk into the dining room and see a long table that could seat about twenty.")
        print("There is a large vase holding wilted roses in the middle of the table.")
        print("Suddenly, an unusually strong gust of wind blows in through the open window, knocking the vase to the "
              "floor.")
        print("")
        print("You see something on the floor glinting in the moonlight.")
        print("You walk over to where the broken vase lies shattered, the roses scattered on the floor.")
        print("In the midst of it all, a small, \033[4mblack key\033[0m. The key is buried under the roses.")
        print("")
# loop for the choice that runs as long as the input is invalid
        while True:
            choice = input("Do you try to pick up the key or look around first? (pick up / look): ").lower()
            print("")
# conditional based on user input for next move
            if choice == "pick up":
                print("You move one of the roses aside, but get pricked by its thorns in the process.")
                print("You pocket the key and try to move forward, but feel really dizzy all of a sudden.")
                print("The rose thorns were poisonous. You die.")
                play_again()
                break
            elif choice == "look":
                print("You look around the room and find a small broom in the corner.")
                print("You use the broom to sweep the shards from the vase and the roses to the side and pocket the "
                      "key.")
                inventory.append("black_key")
                while True:
                    choice2 = input(
                        "Do you go east into the kitchen or west back into the hallway? (east / west): ").lower()
# conditional based on user input for next move
                    if choice2 == "east":
                        kitchen()
                        break
                    elif choice2 == "west":
                        south_hallway()
                        break
                    else:
                        print("Invalid choice.")
                        print("")
                break
            else:
                print("Invalid choice.")
                print("")
# runs if room is revisited
    else:
        print("")
        print("You're back in the dining room. You look around but find nothing.")
# loop for the choice that runs as long as the input is invalid
        while True:
            choice2 = input("Do you go east into the kitchen or west back into the hallway? (east / west): ").lower()
# conditional based on user input for next move
            if choice2 == "east":
                kitchen()
                break
            elif choice2 == "west":
                south_hallway()
                break
            else:
                print("Invalid choice.")
                print("")

# function for when kitchen is entered
def kitchen():
# conditional that runs if room is visited for the first time
    if "kitchen" not in visited_rooms:
        visited_rooms.add("kitchen")
        print("")
        print("You walk into a large kitchen with pots and pans strewn on the floor.")
        print("As you take in the sight, the refrigerator starts \033[93mglowing and shaking violently\033[0m.")
        print("You have a bad feeling, but you carefully step over the pots and pans towards the refrigerator anyway.")
        print("")
# loop for the choice that runs as long as the input is invalid
        while True:
            choice = input("Do you open the refrigerator? (yes / no): ").lower()
            print("")
# conditional based on user input for next move
            if choice == "yes":
                print("You open the refrigerator, and a \033[93mgiant hand\033[0m comes out and pulls you in. You die.")
                play_again()
                break
            elif choice == "no":
                print("You decide against it, and the shaking dies down eventually.")
                print("You look through shelves and drawers. Finally, You find a \033[4mflashlight\033[0m in one of the drawers.")
                print("You leave it off for now so it doesn’t die on you. You go back to the hallway.")
                inventory.append("flashlight")
                south_hallway()
                break
            else:
                print("Invalid choice.")
                print("")
# runs if room is revisited
    else:
        print("")
        print("You're back in the kitchen. You look around but find nothing.")
        south_hallway()

# function for when north hallway is entered
def north_hallway():
# conditional that runs if room is visited for the first time
    if "north hallway" not in visited_rooms:
        visited_rooms.add("north hallway")
        print("")
        print("You walk further down the hallway, which grows dimmer and dimmer.")
        print("You reach a door at the end of the hallway. To your north is the door, which has a golden padlock on it.")
        print("To your west is the living room, which is brightly lit from the glow of the tv static.")
        print("To your east are stairs that lead down, but it’s pitch black.")
        print("And to your south is the other end of the hallway, where you just came from.")
        print("")
# loop for the choice that runs as long as the input is invalid
        while True:
            choice = input("Where do you go? (west / east / north / south): ").lower()
# conditional based on user input for next move
            if choice == "west":
                living_room()
            elif choice == "east":
                basement()
            elif choice == "north":
                staircase()
            elif choice == "south":
                south_hallway()
            else:
                print("Invalid choice.")
                print("")
# runs if room is revisited
    else:
        print("")
        print("You're back at the north end of the hallway.")
        print("")
# loop for the choice that runs as long as the input is invalid
        while True:
            choice = input("Do you go west into the living room, east into the basement, the south end of the "
                           "hallway, or north into the locked room? (east / west / south / north): ").lower()
# conditional based on user input for next move
            if choice == "west":
                living_room()
            elif choice == "east":
                basement()
            elif choice == "north":
                staircase()
            elif choice == "south":
                south_hallway()
            else:
                print("Invalid choice.")
                print("")

# function for when living room is entered
def living_room():
# conditional that runs if room is visited for the first time
    if "living room" not in visited_rooms:
        visited_rooms.add("living room")
        print("")
        print("You enter the living room, which is dark save for the bright glow of the tv static. ")
        print("You look around and find a remote. You try to switch channels when suddenly, the tv goes dark.")
        print("You start to turn away when a tall woman starts climbing out of the tv.")
        print("You start to back away in fear, when she says “If you wish to escape you must solve my riddle.")
        print("")
        print("\033[96m\033[1m“I am the beginning of everything and the end of time and space. I am the beginning of every end and "
              "the end of every place. What am I?”\033[0m")
        print("")
        answer = {"the letter e", "e", "letter e"}
# loop for the choice that runs as long as the input is incorrect
        while True:
            guess = input("Enter your answer: ").lower()
            print("")
# conditional based on user input for answer
            if guess not in answer:
                print("\033[91m\033[1mIncorrect. Try again.\033[0m")
            else:
                break
        print("\033[92m\033[1m“Correct. You may leave.”\033[0m")
        print("You run back to the hallway as the woman disappears in a cloud of dust.")
        north_hallway()
# runs if room is revisited
    else:
        print("")
        print("You're back in the living room. You look around but find nothing.")
        north_hallway()

# function for when basement is entered
def basement():
# conditional based on if item is in inventory
    if "flashlight" in inventory:
        print("")
        print("You turn on your flashlight and slowly make your way downstairs.")
        print("You look around and find a light switch and turn it on.")
        print("It flickers for a moment, glows steadily, illuminating the room.")
        print("You're in the basement, with random junk scattered everywhere.")
        print("To your south is a door with a rusted black padlock and to your west are the stairs.")
        print("")
# conditional that runs if room is visited for the first time
        if basement not in visited_rooms:
            visited_rooms.add("basement")
# loop for the choice that runs as long as the input is invalid
            while True:
                choice = input("Do you go west back upstairs or south into the room? (west / south): ").lower()
# conditional based on user input for next move
                if choice == "west":
                    north_hallway()
                    break
                elif choice == "south":
                    storage_room()
                    break
                else:
                    print("Invalid choice.")
                    print("")
# runs if room is revisited
        else:
            print("")
            print("You're back in the basement. You look around but find nothing.")
# loop for the choice that runs as long as the input is invalid
            while True:
                choice = input("Do you go west back upstairs or south into the room? (west / south): ").lower()
# conditional based on user input for next move
                if choice == "west":
                    north_hallway()
                    break
                elif choice == "south":
                    storage_room()
                    break
                else:
                    print("Invalid choice.")
                    print("")
    else:
        print("")
        print("It's too dark. Try to find a flashlight.")
        north_hallway()

# function for when storage room is entered
def storage_room():
# conditional based on if item is in inventory
    if "black_key" in inventory:
        print("")
        print("You unlock the padlock with your key and enter a small storage room.")
        print("")
# conditional that runs if room is visited for the first time
        if storage_room not in visited_rooms:
            visited_rooms.add("storage_room")
            print("It's completely empty save for a single, \033[4mlong rope\033[0m on the floor. You take the rope and head back "
                  "upstairs.")
            inventory.append("rope")
            north_hallway()
    else:
        print("")
        print("Find the key to unlock the door.")
        north_hallway()

# function for when staircase is entered
def staircase():
# conditional based on if item is in inventory
    if "gold_key" in inventory:
        print("")
        print("You unlock the door and walk inside to find a wide staircase leading upstairs.")
        print("")
# conditional that runs if room is visited for the first time
        if staircase not in visited_rooms:
            visited_rooms.add(staircase)
            print("You go upstairs and find a balcony and step outside. You look down. It’s a steep drop.")
            print("You might not survive falling from here. If only you had something to climb down with.")
            print("")
# conditional based on if item is in inventory
            if "rope" not in inventory:
                print("You should find a \033[4mrope\033[0m to climb down safely.")
                north_hallway()
            else:
                escape()
# runs if room is revisited
        else:
            print("")
            print("You go back upstairs to the balcony.")
            escape()
    else:
        print("")
        print("Find the key to unlock the door.")
        north_hallway()

# function to escape
def escape():
# conditional based on if item is in inventory
        if "rope" in inventory:
            print("")
            print("You take your rope and tie it tightly on the railing, making several knots.")
            print("You throw the other end of the rope over and start climbing down slowly.")
            print("You reach the ground and run away as fast as you possibly can.")
            print("")
            print("\033[93m\033[1mYou escaped!!\033[0m")
            play_again()
        else:
            print("")
            print("You try to climb down slowly, but your foot slips and you fall. You die.")
            play_again()

# function to restart the game
def play_again():
# loop for the choice that runs as long as the input is invalid
    while True:
        print("")
        restart = input("Play again? (yes / no): ").lower()
# conditional based on user input for next move
        if restart == "yes":
            print("")
            inventory.clear()
            visited_rooms.clear()
            start_game()
            break
        elif restart == "no":
            print("")
            print("Thanks for playing.")
            exit()
        else:
            print("Invalid choice.")

# calls the function to start the game
start_game()