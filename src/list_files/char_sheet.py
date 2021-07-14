import time
import sys
from list_files import InventoryList as InventList


################################################################
# Character Sheet
#
# Specialized type of Inventory List. Guides users through
# building a character and defining aspects about them. This
# can be used for world building when writing or to develop a
# character for roleplay or game.
#
# Provides the user with a pre-populated dict and asks them to
# fill in the values for each pre-determined key.
################################################################

######################################
# CharSheet Driver
######################################
def charsheet_driver(char_sheet):
    return


######################################
# CharSheet Constructor
######################################
def create_charlist():
    print("\nLet's create a character sheet for a new character.\n")
    char_sheet = InventList.InventoryList()
    init_attributes(char_sheet)
    add_values(char_sheet)


######################################
# CharSheet Attribute Setter
######################################
def init_attributes(char_sheet):
    attr_list = ["Name: ", "Age (Date of Birth): ", "Species: ", "Pronouns: ",
                 "Nicknames/Aliases:", "Height: ", "Weight: ", "Hair Color/Style: ",
                 "Eye Color: ", "Personality Traits: ", "Skills/Talents: ",
                 "Strengths: ", "Weaknesses: ", "Fears: ", "Likes: ", "Dislikes: ",
                 "Favorite Food: ", "Religion/Beliefs: ", "Occupation: ", "Clothing Style: ",
                 "Accessories: ", "Family: ", "Friends: ", "Pets: ", ]
    char_sheet.init_keys(attr_list)
    return


######################################
# CharSheet Value Setter
######################################
def add_values(char_sheet):
    print("\nType each value you want in the given attribute and hit Enter when you want "
          "to fill in the next attribute." + "\nIf you want to finish early, type 'done'.")

    attr_list = char_sheet.keys()
    value_list = []
    value = input("Ready? (yes/no)")

    while value != "done":
        if value == "q" or value == "quit":
            sys.exit()
        else:
            for attr in attr_list:
                print(attr)
                value_list.append(value)
                value = input()

    # return the updated sheet to the driver
    charsheet_driver(char_sheet)

