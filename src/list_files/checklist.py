# Imports

################################################################
# Checklist
# Checklist Class
#
# Imports:
################################################################

######################################
# Checklist Driver
######################################
def checklist_driver(user_list, name):
    # find out what the user wants to do with their list
    request = input("\nWhat would you like to do with your list?\n" +
                    "1 - Print your list\n" +
                    "2 - Add more items\n" +
                    "3 - Remove items\n" +
                    "4 - Delete your list\n")

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
    else:  # user put in a num not on the list
        print("Sorry, that number isn't on the list. Try again?\n")
        checklist_driver(user_list, name)


######################################
# Checklist Constructor
######################################
def create_checklist(name):
    user_list = []
    print("\nLet's create your " + name + " list.")
    # user_list = add_items(user_list)
    # checklist_driver(user_list, name)
    add_items(user_list, name)


######################################
# Checklist Printer
######################################
def print_checklist(user_list, name):
    print("\n" + name + ":")
    for item in user_list:
        print("- ", item)


######################################
# Checklist Deleter
######################################
# delete the entire list
def delete_list(user_list, name):
    confirm = input("Are you sure you want to delete your entire list?\n" +
                    "1 - Yes! I'm done with it.\n" +
                    "2 - No! Please take me back.\n")

    if confirm == "1":
        # delete
        print("Your list has been deleted. Thanks!")
    elif confirm == "2":
        print("Ok!")
    else:
        print("That isn't an option, try again?\n")
        delete_list(user_list, name)


######################################
# Checklist Item Adder
######################################
# add new items to the list
def add_items(user_list, name):
    # take items and add them to the user's list
    print("\nHit Enter after each new item and type done when you're finished.\n")
    item = input()
    while item != "done":
        user_list.append(item)
        item = input()
    # return user_list
    checklist_driver(user_list, name)


######################################
# Checklist Item Remover
######################################
# remove items from the list
def remove_items(user_list, name):
    return
