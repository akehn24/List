import time
import sys
from list_files import InventoryList as InventList

################################################################
# Inventory
#
# Driver that utilizes the Inventory List file to create a
# general inventory list for the user. Typically used to store items
# and their quantities or values.
#
# Item  - key
# Value - value
#
# Imports:
#   time            allows the program to pause for ease of use
#   sys             allows the user to exit the program on command
#   inventory_list  file that contains this list's data functions
################################################################


######################################
# Inventory Driver
######################################
def inventory_driver(user_list, name):
    # find out what the user wants to do with their list
    request = input("\nWhat would you like to do?\n" +
                    "1 - Print your inventory\n" +
                    "2 - Add new items\n" +
                    "3 - Remove an existing item\n" +
                    "4 - Change an item's value\n" +
                    "5 - Delete your inventory\n" +
                    "6 - Make a new inventory list\n" +
                    "q - I'm done!\n")

    ######################################
    # User requests will be directed here:
    ######################################
    # Print list
    if request == "1":
        print_inventory(user_list, name)
    # Add new items
    elif request == "2":
        add_items(user_list, name)
    # Remove an existing item
    elif request == "3":
        remove_item(user_list, name)
    # Change an item's value
    elif request == "4":
        set_value(user_list, name)
    # Delete list
    elif request == "5":
        delete_list(user_list, name)
        name = None
    # Make new list
    elif request == "6":
        confirm = input("\nThis will overwrite your current list. Proceed?\n" +
                        "1 - Go ahead\n" +
                        "2 - No please!\n")
        if confirm == "1":
            create_inventory()
    elif request == "q" or request == "quit":
        sys.exit()
    else:  # user put in a num not on the list
        print("\nSorry, that number isn't on the list. Try again?\n")
        inventory_driver(user_list, name)

    inventory_driver(user_list, name)


######################################
# Inventory Constructor
######################################
def create_inventory():
    name = input("\nLet's create an Inventory List... What would you like to call it? \n")
    user_list = InventList.InventoryList()
    add_items(user_list, name)


######################################
# Inventory Printer
######################################
def print_inventory(user_list, name):
    if name is None:
        print("You don't currently have a list.")
        return

    print("\n" + name + ":")
    user_list.print_list()
    print("\n")
    time.sleep(0.5)


######################################
# Item Deleter
######################################
def remove_item(user_list, name):
    print("\n")
    print_inventory(user_list, name)
    item = input("\nWhich item would you like to remove?\n")
    user_list.remove_item(item)
    time.sleep(0.5)
    print("\nRemoved " + item + " from your " + name + " list.")

    # return the updated list to the Driver
    inventory_driver(user_list, name)


######################################
# Inventory Deleter
######################################
def delete_list(user_list, name):
    confirm = input("\nAre you sure you want to delete your entire list?\n" +
                    "1 - Yes! I'm done with it.\n" +
                    "2 - No! Please take me back.\n")

    if confirm == "1":
        user_list.delete_list()
        print("\nYour list has been deleted.")
        time.sleep(0.5)
    elif confirm == "2":
        print("Ok!")
        time.sleep(0.5)
    else:  # allows the user to try again
        print("That isn't an option, try again?\n")
        time.sleep(0.5)
        delete_list(user_list, name)


######################################
# Inventory Item Adder
######################################
def add_items(user_list, name):
    if name is None:
        print("You don't currently have a list.")
        return

    print("\nType each item you would like to add with its value separated by a comma.\n" +
          "For example: Fish, 20\n" +
          "Hit Enter after each item and its value and type done when you're finished.")
    # take in user's input in format: "key, value"
    key_val = input()

    while key_val != "done":
        if key_val == "q" or key_val == "quit":
            sys.exit()
        else:
            user_list.add_item(key_val)
            key_val = input()

    # return the updated list to the Driver
    inventory_driver(user_list, name)


######################################
# Inventory Value Setter
######################################
def set_value(user_list, name):
    print_inventory(user_list, name)
    print("Which item's value would you like to change?")
    key = input()
    print("What is the new value you'd like it to have?")
    val = input()

    user_list = user_list.set_value(key, val)
    print("\nThe item " + key + " now has the value " + val + ".")

    # return the updated list to the Driver
    inventory_driver(user_list, name)
