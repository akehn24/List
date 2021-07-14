################################################################
# Inventory List Class
#
# Data functions for creating and manipulating an inventory
# list. Uses the python dictionary to complete these tasks.
#
# Inventory Lists:
# inventory_driver      stores general items with values
# movie_driver          stores movie titles and their genres
# book_driver           stores book titles and their authors
################################################################
class InventoryList:
    ######################################
    # Constructor
    ######################################
    def __init__(self):
        # empty dict to be added to later
        self.user_list = {}

    ######################################
    # Printer
    ######################################
    def print_list(self):
        for item, value in sorted(self.user_list.items()):
            print(item + ", " + value)

    ######################################
    # Add Key:Value Pairs
    ######################################
    def add_item(self, key_val):
        # create list of the user's response: ['key', 'value']
        key_val_list = key_val.split(", ")
        # extract the key and value from the list
        key = key_val_list[0]
        val = key_val_list[1]
        # add to the list and return it
        self.user_list[key] = val
        # return self.user_list

    ######################################
    # Remove Key:Value Pairs
    ######################################
    def remove_item(self, item):
        self.user_list.pop(item)
        return self.user_list

    ######################################
    # Value Setter
    ######################################
    def set_value(self, key, val):
        self.user_list[key] = val
        return self.user_list

    ######################################
    # Delete List
    ######################################
    def delete_list(self):
        self.user_list.clear()

    ######################################
    # Display Keys by Value
    ######################################
    def keys_by_value(self, val):
        # temp dict to store the keys with this value
        key_list = []
        # loop through, add keys with the value
        for key, value in self.user_list.items():
            if value == val:
                key_list.append(key)
        return key_list

    ######################################
    # Populate Keys without Values
    ######################################
    def init_keys(self, key_list):
        for key in key_list:
            self.user_list[key] = None

    ######################################
    # Populate Values for Existing Keys
    ######################################
    def insert_values(self, val_list):
        itr = 0
        for value in val_list:
            self.user_list[itr] = value
            itr += 1
