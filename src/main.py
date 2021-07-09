import time
import sys
from list_files import checklist_driver as checklist
from list_files import inventory_driver as inventory


################################################################
# Main List File 
# List application driver.
#
# Imports:
#   time    allows the app to wait before printing messages
################################################################

################################################################
# List Maker
# Help the program get to the list class chosen by the user.
################################################################
def list_maker(list_num):
    if list_num == "1":
        # noinspection PyUnresolvedReferences
        checklist.create_checklist()
    elif list_num == "2":
        inventory.create_inventory()
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
                  "2 - Inventory\n"
                  "\n More Coming Soon!\n")

# creating the user's chosen list
list_maker(list_type)

# for test
print("\nAll finished.")
