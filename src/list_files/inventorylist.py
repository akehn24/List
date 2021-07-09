import time
import sys


################################################################
# Inventory Class
#
# Allows the user to create an inventory list that stores
# Key : Value pairs of their choosing. Typically used to store
# items and their quantities.
#
# Item  - key
# Value - value
#
# Imports:
#   time    allows the program to pause for ease of use
#   sys     allows the user to exit the program on command
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
    # Print your list
    if request == "1":
        print_inventory(user_list, name)
    # Add more items
    elif request == "2":
        add_items(user_list, name)
    # Remove an existing item
    elif request == "3":
        remove_item(user_list, name)
    elif request == "4":
        set_value(user_list, name)
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
            create_inventory()
    elif request == "q" or request == "quit":
        sys.exit()
    else:  # user put in a num not on the list
        print("Sorry, that number isn't on the list. Try again?\n")
        inventory_driver(user_list, name)

    inventory_driver(user_list, name)


######################################
# Inventory Constructor
######################################
def create_inventory():
    name = input("\nLet's create an Inventory List... What would you like to call it? \n")
    user_list = {}
    add_items(user_list, name)


######################################
# Inventory Printer
######################################
def print_inventory(user_list, name):
    if name is None:
        print("You don't have a list. Choose option 5 to make a new one!")
        return

    print("\n" + name + ":")
    for item, value in sorted(user_list.items()):
        print(item + ", " + value)
    print("\n")
    time.sleep(0.5)


######################################
# Inventory Printer By Value
# Used to find items by value
######################################
def print_by_val():
    return


######################################
# Item Deleter
######################################
def remove_item(user_list, name):
    print("\nWhich item would you like to remove?")
    item = input()
    user_list.pop(item)
    time.sleep(0.5)
    print("\nRemoved " + item + " from your " + name + " list.")


######################################
# Inventory Deleter
######################################
def delete_list(user_list, name):
    confirm = input("\nAre you sure you want to delete your entire list?\n" +
                    "1 - Yes! I'm done with it.\n" +
                    "2 - No! Please take me back.\n")

    if confirm == "1":
        user_list.clear()
        print("\nYour list has been deleted.")
        time.sleep(0.5)
    elif confirm == "2":
        print("Ok!")
        time.sleep(0.5)
    else:
        print("That isn't an option, try again?\n")
        time.sleep(0.5)
        delete_list(user_list, name)


######################################
# Inventory Add Helper
######################################
def add_helper(key_val):
    if key_val == "done":
        return 0
    elif key_val == "q" or key_val == "quit":
        sys.exit()
    else:
        return key_val.split(", ")


######################################
# Inventory Item Adder
######################################
def add_items(user_list, name):
    if name is None:
        print("You don't have a list. Choose option 5 to make a new one!")
        return

    print("\nType each item you would like to add with its value separated by a comma.\n" +
          "For example: Fish, 20\n" +
          "Hit Enter after each item and its value and type done when you're finished.")
    # take in user's input in format: "key, value"
    key_val = input()
    # create list of the user's response: ['key', 'value'] and extract these values
    key_val = add_helper(key_val)

    while key_val != 0:
        # separate key and value, then add
        key = key_val[0]
        val = key_val[1]
        user_list[key] = val
        # set the key_val input list back up with the next request
        key_val = input()
        key_val = add_helper(key_val)
    else:
        # return user_list and name to the driver
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

    user_list[key] = val
    print("\nThe item " + key + " now has the value " + val + ".")
