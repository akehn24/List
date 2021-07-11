import time
import sys
from list_files import inventory_list as inventlist

################################################################
# Book Inventory List
#
# Driver that utilizes the Inventory List file to create a
# list of books and their authors for the user. Currently only
# supports unique book titles.
#
# Book  - key
# Author  - value
#
# Imports:
#   time            allows the program to pause for ease of use
#   sys             allows the user to exit the program on command
#   inventory_list  file that contains this list's data functions
################################################################


######################################
# Book Driver
######################################
def book_driver(user_list):
    # find out what the user wants to do with their list
    request = input("\nWhat would you like to do?\n" +
                    "1 - Print your book list\n" +
                    "2 - Add new book\n" +
                    "3 - Remove an existing book\n" +
                    "4 - Update a book's author\n" +
                    "5 - Show all books from an author\n" +
                    "6 - Delete your book list\n" +
                    "7 - Make a new book list\n" +
                    "q - I'm done!\n")

    ######################################
    # User requests will be directed here:
    ######################################
    # Print list
    if request == "1":
        print_booklist(user_list)
    # Add new book
    elif request == "2":
        add_books(user_list)
    # Remove an existing book
    elif request == "3":
        remove_book(user_list)
    # Update a book's author
    elif request == "4":
        set_author(user_list)
    # Show all books from an author
    elif request == "5":
        books_by_author(user_list)
    # Delete list
    elif request == "6":
        delete_booklist(user_list)
    # Make new list
    elif request == "7":
        confirm = input("\nThis will overwrite your current book list. Proceed?\n" +
                        "1 - Go ahead\n" +
                        "2 - No please!\n")
        if confirm == "1":
            create_booklist()
    elif request == "q" or request == "quit":
        sys.exit()
    else:  # user put in a num not on the list
        print("\nSorry, that number isn't on the list. Try again?\n")
        book_driver(user_list)

    book_driver(user_list)


######################################
# Book List Constructor
######################################
def create_booklist():
    print("\nLet's create a Book List!\n")
    user_list = inventlist.create_list()
    add_books(user_list)


######################################
# Book List Printer
######################################
def print_booklist(user_list):
    if user_list:
        print("\n")
        inventlist.print_list(user_list)
        print("\n")
        time.sleep(0.5)
    else:
        print("You don't currently have a list.")
        return


######################################
# Book Deleter
######################################
def remove_book(user_list):
    print("\nWhich book would you like to remove?")
    book = input()
    user_list = inventlist.remove_item(user_list, book)
    time.sleep(0.5)
    print("\nRemoved " + book + " from your movie list.")

    # return the updated list to the Driver
    book_driver(user_list)


######################################
# Book List Deleter
######################################
def delete_booklist(user_list):
    confirm = input("\nAre you sure you want to delete your entire list?\n" +
                    "1 - Yes! I'm done with it.\n" +
                    "2 - No! Please take me back.\n")

    if confirm == "1":
        inventlist.delete_list(user_list)
        print("\nYour book list has been deleted.")
        time.sleep(0.5)
    elif confirm == "2":
        print("Ok!")
        time.sleep(0.5)
    else:  # allows the user to try again
        print("That isn't an option, try again?\n")
        time.sleep(0.5)
        delete_booklist(user_list)


######################################
# Book Adder
######################################
def add_books(user_list):
    print("\nType each book you would like to add with its author separated by a comma.\n" +
          "For example: The Hobbit, Tolkien\n" +
          "Hit Enter after each book and its author and type done when you're finished.\n")

    # take in user's input in format: "key, value"
    key_val = input()

    while key_val != "done":
        if key_val == "q" or key_val == "quit":
            sys.exit()
        else:
            user_list = inventlist.add_item(user_list, key_val)
            key_val = input()

    # return the updated list to the Driver
    book_driver(user_list)


######################################
# Genre Setter
######################################
def set_author(user_list):
    print_booklist(user_list)
    print("Which book's author would you like to change?")
    book = input()
    print("Which author would you like to assign to this book?")
    author = input()

    user_list = inventlist.set_value(user_list, book, author)
    print("\n" + author + " is now the author of " + book + ".")

    # return the updated list to the Driver
    book_driver(user_list)


######################################
# Print Movies by Genre
######################################
def books_by_author(user_list):
    print("\nWhich author's books would you like to see?")
    author = input()

    if author == "q" or author == "quit":
        sys.exit()
    if author in user_list.values():
        print("\nBooks by " + author + ":\n")
        inventlist.keys_by_value(user_list, author)
    else:
        print("There are no books by that author in your list.")
