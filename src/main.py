import time
import sys
from list_files import checklist_driver as checklist
from list_files import inventory_driver as inventory
from list_files import movie_driver as movie
from list_files import book_driver as book


################################################################
# Main List File 
# List application driver.
#
# Imports:
#   time    allows the app to wait before printing messages
################################################################

################################################################
# List Maker
# Help the program get to the right List Driver
################################################################
def list_maker(list_num):
    # Checklist
    if list_num == "1":
        # noinspection PyUnresolvedReferences
        checklist.create_checklist()
    # Inventory List
    elif list_num == "2":
        invent_type = input("\nWhat type of Inventory List would you like to create?\n" +
                            "1 - General\n" +
                            "2 - Movie List\n" +
                            "3 - Book List\n")
        # General Inventory List
        if invent_type == "1":
            inventory.create_inventory()
        # Movie Inventory List
        if invent_type == "2":
            movie.create_movielist()
        # Book Inventory List
        if invent_type == "3":
            book.create_booklist()
    # Character Sheet
    elif list_num == "3":
        return
    elif list_num == "q" or list_num == "quit":
        sys.exit()


################################################################
# Main User Interface
#  Communicates with the user via command line and directs their
#  info to the appropriate list creation functions. 
################################################################
print("\n~~~Welcome to List Maker!~~~")
print("(type quit at any time to quit the app)\n")
time.sleep(0.5)

# take initial list info from the user
list_type = input("\nType the number of the type of list you'd like to create: \n" +
                  "1 - Checklist\n" +
                  "2 - Inventory (General, Movies, Books)\n" +
                  "3 - Character Sheet\n" +
                  "\n More Coming Soon!\n")

# creating the user's chosen list
list_maker(list_type)

# for test
print("\nAll finished.")
