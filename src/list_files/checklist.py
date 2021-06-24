import time
import sys
from list_files import LinkedChecklist as Link


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
                    "3 - Check off items\n" +
                    "4 - Remove checked off items\n" +
                    "5 - Delete your list\n" +
                    "6 - Make a new list\n" +
                    "q - I'm done!\n")

    ######################################
    # User requests will be directed here:
    ######################################
    # Print your list
    if request == "1":
        print_checklist(user_list, name)
    # Add more items
    elif request == "2":
        add_items(user_list, name)
    # Check off items
    elif request == "3":
        checkoff_items(user_list, name)
    # Remove checked off items
    elif request == "4":
        remove_checked(user_list, name)
    # Delete your list
    elif request == "5":
        delete_list(user_list, name)
        name = None
    # Make a new list
    elif request == "6":
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
    user_list = Link.LinkedChecklist()
    add_items(user_list, name)


######################################
# Checklist Printer
######################################
def print_checklist(user_list, name):
    if name is None:
        print("You don't have a list. Choose option 5 to make a new one!")
        return

    print("\n" + name + ":")
    user_list.print()
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
        user_list.delete_list()
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
    if name is None:
        print("You don't have a list. Choose option 5 to make a new one!")
        return

    print("\nHit Enter after each new item and type done when you're finished.")
    item = input()
    while item != "done":
        user_list.insert(item)
        item = input()
    # return user_list and name to the driver
    checklist_driver(user_list, name)


######################################
# Checklist Item Checker
######################################
def checkoff_items(user_list, name):
    if name is None:
        print("You don't have a list. Choose option 5 to make a new one!")
        return

    # print the list so the user knows what's on it
    print("\nWhich item would you like to check off?")
    print_checklist(user_list, name)

    item = input()
    user_list.change_status(item)
    print(item + " checked off.\n")

    # ask if they want more checked off or return
    more = input("\nAre you done checking off items?\n" +
                 "1 - Yes\n" +
                 "2 - No\n")
    if more == "1":
        print("Sounds good!\n")
        time.sleep(0.5)
    elif more == "2":
        checkoff_items(user_list, name)


######################################
# Checklist Item Checker
######################################
def remove_checked(user_list, name):
    if name is None:
        print("You don't have a list. Choose option 5 to make a new one!")
        return

    confirm = input("\nRemoving checked off items will delete them from your list. Do you want to continue?\n"
                    "1 - Yes\n" +
                    "2 - No\n")
    if confirm == "1":
        user_list.delete_all_checked()
        print("Your checked off items have been removed!\n")
    elif confirm == "2":
        print("Ok!")
        time.sleep(0.5)
