import time
import sys
from list_files import InventoryList as InventList

################################################################
# Movie Inventory List
#
# Driver that utilizes the Inventory List file to create a
# list of movies and their genres for the user. Currently only
# # supports unique movie titles.
#
# Movie  - key
# Genre  - value
#
# Imports:
#   time            allows the program to pause for ease of use
#   sys             allows the user to exit the program on command
#   inventory_list  file that contains this list's data functions
################################################################


######################################
# Movie Driver
######################################
def movie_driver(user_list):
    # find out what the user wants to do with their list
    request = input("\nWhat would you like to do?\n" +
                    "1 - Print your movie list\n" +
                    "2 - Add new movie\n" +
                    "3 - Remove an existing movie\n" +
                    "4 - Change a movie's genre\n" +
                    "5 - Show all movies of a genre\n" +
                    "6 - Delete your movie list\n" +
                    "7 - Make a new movie list\n" +
                    "q - I'm done!\n")

    ######################################
    # User requests will be directed here:
    ######################################
    # Print list
    if request == "1":
        print_movielist(user_list)
    # Add new movie
    elif request == "2":
        add_movies(user_list)
    # Remove an existing movie
    elif request == "3":
        remove_movie(user_list)
    # Change movie's genre
    elif request == "4":
        set_genre(user_list)
    # Show all movies of genre
    elif request == "5":
        movies_by_genre(user_list)
    # Delete list
    elif request == "6":
        delete_movielist(user_list)
    # Make new list
    elif request == "7":
        confirm = input("\nThis will overwrite your current movie list. Proceed?\n" +
                        "1 - Go ahead\n" +
                        "2 - No please!\n")
        if confirm == "1":
            create_movielist()
    elif request == "q" or request == "quit":
        sys.exit()
    else:  # user put in a num not on the list
        print("\nSorry, that number isn't on the list. Try again?\n")
        movie_driver(user_list)

    movie_driver(user_list)


######################################
# Movie List Constructor
######################################
def create_movielist():
    print("\nLet's create a Movie List!\n")
    user_list = InventList.InventoryList()
    add_movies(user_list)


######################################
# Movie List Printer
######################################
def print_movielist(user_list):
    print("\n")
    user_list.print_list()
    print("\n")
    time.sleep(0.5)


######################################
# Movie Deleter
######################################
def remove_movie(user_list):
    print("\n")
    print_movielist(user_list)
    print("\nWhich movie would you like to remove?")
    movie = input()
    user_list.remove_item(movie)
    time.sleep(0.5)
    print("\nRemoved " + movie + " from your movie list.")

    # return the updated list to the Driver
    movie_driver(user_list)


######################################
# Movie List Deleter
######################################
def delete_movielist(user_list):
    confirm = input("\nAre you sure you want to delete your entire list?\n" +
                    "1 - Yes! I'm done with it.\n" +
                    "2 - No! Please take me back.\n")

    if confirm == "1":
        user_list.delete_list()
        print("\nYour movie list has been deleted.")
        time.sleep(0.5)
    elif confirm == "2":
        print("Ok!")
        time.sleep(0.5)
    else:  # allows the user to try again
        print("That isn't an option, try again?\n")
        time.sleep(0.5)
        delete_movielist(user_list)


######################################
# Movie Adder
######################################
def add_movies(user_list):
    print("\nType each movie you would like to add with its genre separated by a comma.\n" +
          "For example: Hereditary, horror\n" +
          "Hit Enter after each movie and its genre and type done when you're finished.")

    # take in user's input in format: "key, value"
    key_val = input()

    while key_val != "done":
        if key_val == "q" or key_val == "quit":
            sys.exit()
        else:
            user_list.add_item(key_val)
            key_val = input()

    # return the updated list to the Driver
    movie_driver(user_list)


######################################
# Genre Setter
######################################
def set_genre(user_list):
    print_movielist(user_list)
    print("Which movie's genre would you like to change?")
    movie = input()
    print("What is the new genre you'd like it to have?")
    genre = input()

    user_list.set_value(movie, genre)
    print("\n" + movie + " is now in the " + genre + " genre.")

    # return the updated list to the Driver
    movie_driver(user_list)


######################################
# Print Movies by Genre
######################################
def movies_by_genre(user_list):
    print("\nWhich genre would you like to see?")
    genre = input()

    if genre == "q" or genre == "quit":
        sys.exit()
    else:
        print("\nMovies in the " + genre + " genre:")
        # list with these movies
        movies_in_genre = user_list.keys_by_value(genre)
        movies_in_genre.sort()
        for movie in movies_in_genre:
            print(movie)
