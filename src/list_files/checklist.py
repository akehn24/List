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
def checklist_driver(name):
    # create the user's checklist
    user_list = create_checklist(name)

    # find out what the user wants to do with their list
    request = input("\nYour list is made! What would you like to do with it?\n" +
                    "1 - Print your list\n" +
                    "WIP!\n")

    ######################################
    # User requests will be directed here:
    ######################################
    # print the user's list
    if request == "1":
        print_checklist(user_list, name)
    # do the thing
    # if (request == "#"):
    # the thing


######################################
# Checklist Creator
######################################
def create_checklist(name):
    user_list = []
    print(
        "\nLet's create your " + name + " list. Hit Enter after each new item and type done when you're finished.")
    # take items and add them to the user's list
    item = input()
    while item != "done":
        user_list.append(item)
        item = input()
    return user_list


######################################
# Checklist Printer
######################################
def print_checklist(user_list, name):
    print("\n" + name + ":")
    for item in user_list:
        print("- ", item)
