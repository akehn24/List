import time
import sys


################################################################
# Checklist
# Checklist Class
#
# Imports:
#   time    allows the program to pause for ease of use
#   sys     allows the user to exit the program on command
################################################################

######################################
# Checklist Driver
######################################
def checklist_driver(user_list, name):
    # find out what the user wants to do with their list
    request = input("\nWhat would you like to do?\n" +
                    "1 - Print your list\n" +
                    "2 - Add more items\n" +
                    "3 - Remove items\n" +
                    "4 - Delete your list\n" +
                    "5 - Make a new list\n" +
                    "q - I'm done!\n")

    ######################################
    # User requests will be directed here:
    ######################################
    # print the user's list
    if request == "1":
        print_checklist(user_list, name)
    elif request == "2":
        add_items(user_list, name)
    elif request == "3":
        remove_items(user_list, name)
    elif request == "4":
        delete_list(user_list, name)
    elif request == "5":
        # will hopefully be able to save these at some point
        confirm = input("\nThis will overwrite your current list. Proceed?\n" +
                        "1 - Go ahead\n" +
                        "2 - No please!\n")
        if confirm == "1":
            create_checklist()
    elif request == "q":
        sys.exit()
    elif request == "quit":
        # the option given at the beginning of the program
        sys.exit()
    else:  # user put in a num not on the list
        print("Sorry, that number isn't on the list. Try again?\n")
        checklist_driver(user_list, name)

    checklist_driver(user_list, name)


######################################
# Checklist Constructor
######################################
def create_checklist():
    name = input("Let's create a Checklist... What would you like to call it? \n")
    user_list = []
    add_items(user_list, name)


######################################
# Checklist Printer
######################################
def print_checklist(user_list, name):
    print("\n" + name + ":")
    for item in user_list:
        print("- ", item)
    print("\n")
    time.sleep(0.5)


######################################
# Checklist Deleter
######################################
def delete_list(user_list, name):
    confirm = input("\nAre you sure you want to delete your entire list?\n" +
                    "1 - Yes! I'm done with it.\n" +
                    "2 - No! Please take me back.\n")

    if confirm == "1":
        user_list.clear()
        print("Your list has been deleted.")
        time.sleep(0.5)
    elif confirm == "2":
        print("Ok!")
        time.sleep(0.5)
    else:
        print("That isn't an option, try again?\n")
        time.sleep(0.5)
        delete_list(user_list, name)


######################################
# Checklist Item Adder
######################################
def add_items(user_list, name):
    print("\nHit Enter after each new item and type done when you're finished.")
    item = input()
    while item != "done":
        user_list.append(item)
        item = input()
    # return user_list and name to the driver
    checklist_driver(user_list, name)


######################################
# Checklist Item Remover
######################################
def remove_items(user_list, name):
    # print the list so the user knows what's on it
    print("\nWhich item would you like to remove?")
    print_checklist(user_list, name)

    item = input()
    user_list.remove(item)
    print(item + " removed.\n")

    # ask if they want more removed or return
    more = input("\nAre you done removing items?\n" +
                 "1 - Yes\n" +
                 "2 - No\n")
    if more == "1":
        print("Sounds good!\n")
        time.sleep(0.5)
    elif more == "2":
        remove_items(user_list, name)
