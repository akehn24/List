import sys

################################################################
# Inventory List
#
# Data functions for creating and manipulating an inventory
# list. Uses the python dictionary to complete these tasks.
#
# Inventory Lists:
# inventory_driver      stores general items with values
# movie_driver          stores movie titles and their genres
# book_driver           stores book titles and their authors
################################################################


######################################
# Constructor
######################################
def create_list():
    # empty dict to be added to later
    user_list = {}
    return user_list


######################################
# Printer
######################################
def print_list(user_list):
    for item, value in sorted(user_list.items()):
        print(item + ", " + value)


######################################
# Add Key:Value Pairs
######################################
def add_item(user_list, key_val):
    # create list of the user's response: ['key', 'value']
    key_val_list = key_val.split(", ")
    # extract the key and value from the list
    key = key_val_list[0]
    val = key_val_list[1]
    # add to the list and return it
    user_list[key] = val
    return user_list


######################################
# Remove Key:Value Pairs
######################################
def remove_item(user_list, item):
    user_list.pop(item)
    return user_list


######################################
# Value Setter
######################################
def set_value(user_list, key, val):
    user_list[key] = val
    return user_list


######################################
# Delete List
######################################
def delete_list(user_list):
    user_list.clear()


######################################
# Display Keys by Value
######################################
def keys_by_value(user_list, val):
    # take list, make new one? add in those keys, print
    # temp dict to store the movies with this genre
    val_list = {}
    # loop through, add movies with this genre to the temp list
    for key, value in user_list.items():
        curr_value = value
        if curr_value is val:
            val_list[key] = value

    print_list(val_list)
