# Standard Library Imports
import time

# Third Party Imports (if any...)

# Local App Imports
# import list.list as list

################################################################
# Main List File 
# List application driver.
#
# Imports:
#   time    allows the app to wait before printing messages
################################################################

################################################################
# Helper Functions
################################################################

################################################################
# List Functions
# Calls Lists's functions so they can do all the work.
################################################################
# imports not working rn, going to implement here to move to 
# List.py later

# Checklist Creator
def create_checklist(list_name):
    checklist = []
    print("\nLet's create your " + list_name + " list. Hit Enter after each new item and type done when you're finished.")
    # take items and add them to the user's list
    item = input()
    while (item != "done"):
        checklist.append(item)
        item = input()

    return checklist

# Checklist Printer
def print_checklist(checklist, list_name):
    print("\n" + list_name + ":")
    for item in checklist:
        print("- ", item)

# Checklist Driver
def checklist(list_name):
    # create the user's checklist
    user_list = create_checklist(list_name)

    # find out what the user wants to do with their list
    request = input("\nYour list is made! What would you like to do with it?\n" + 
                "1 - Print your list\n" + 
                "WIP!\n")

    # User requests will be directed here:
    ######################################
    # print the user's list
    if (request == "1"):
        print_checklist(user_list, list_name)
    # do the thing
    #if (request == "#"):
        #the thing

################################################################
# Main User Interface
# Communicates with the user via command line.
################################################################
print("\n~~~Welcome to List Maker!~~~")
print("(type quit at any time to quit the app)\n")
# waits a moment before printing the next line
time.sleep(0.5)

list_name = input("Let's create a list... What would you like to call it? \n")
list_type = input("\nType the number of the type of list you'd like to create: \n" + 
                  "1 - Checklist\n" + 
                  "Coming Soon!\n")

# creating the user's list
if (list_type == "1"):
    checklist(list_name)

print("\nAll finished.")