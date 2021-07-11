# List Maker
## Implementation of an Evolving List

I use lists frequently in my day-to-day life so I programmed an application that could create the types of lists I want.

## Table of Contents
- [Project Status](https://github.com/akehn24/list-maker##project-status)
   - [Goals](https://github.com/akehn24/list-maker###goals)
   - [Task List](https://github.com/akehn24/list-maker###task-list)
   - [Future Tasks](https://github.com/akehn24/list-maker###)
- [Technologies](https://github.com/akehn24/list-maker##technologies)
- [Bugs](https://github.com/akehn24/list-maker##bugs)
- [Demos](https://github.com/akehn24/list-maker##demos)
- [Sources](https://github.com/akehn24/list-maker##sources)

---
## Project Status :green_circle:
### Goals
- Use multiple styles of data structures to create usable lists
- Read/Write to text files to save list data
- Practice taking user input - terminal for now, GUI later
- Create a navigatable menu for a user to input data

### Task List:
:heavy_check_mark: Create a simple list using data structures   
:heavy_check_mark: Fix import files bug  
:heavy_check_mark: Implement a linked list for the Checklist  
:heavy_check_mark: Integrate the linked list into the current Checklist code  
:heavy_check_mark: Basic Inventory List  
:x: Decide whether or not to make Movie / Book lists
:x::warning: Figure out why TOC links aren't working (I'll do this eventually...)

<!--- 
Emojis for the Task List:
DONE =      :heavy_check_mark:
NOT DONE =  :x:
WIP =       :recycle:
BUGGED =    :warning:
 --->

### Future Tasks
:x: Attempt to create an actual user interface  
:x: Write list to text file for saving  
:x: Character Sheet Class (possibly one for DnD and one for gen use)
:x: Categorical List  

### Feature Creep
- Checklist:
   - :x: Check/Uncheck all items at once
   - :x: Sort items by checked/unchecked

---
## Technologies
- Visual Studio Code
- Pycharm
- Python

## Knowledge Used
- Object Oriented programming
- Classes and Objects
- Python List
- Linked List
- Python Dictionaries

---
## Design
### Checklist
- Implemented a Linked List Class to handle the data and functionality of the list.
- A driver file directs the user through list manipulation by using the functionality of the Linked List Class. 
### Inventory
- A general Inventory list file handles the data and functionality of the Inventory drivers.
- I decided to implement each type of Inventory list driver separately since the UI dialogue would be different for each of them.
- Planning on implementing a Character Sheet Class and driver separately to handle this specialized type of list.
### Categorical
-

---
## Bugs
- Importing a file:
   - Pylance has issues with importing local files. [Info here.](https://github.com/microsoft/pylance-release/blob/main/TROUBLESHOOTING.md#unresolved-import-warnings)
   - Tried their fix of adding the directory path to the setting.json file - did not seem to work
   - Found a workaround to tell Pylance to ignore the line, but the import does not work this way.
   - Switching to Pycharm to see if the import will work there (it does).
- Pycharm bug - cannot find reference 'function_name' in '-init-.py'
   - There are apparently a few fixes, but putting '# noinspection PyUnresolvedReferences' on the line above the ref tells Pycharm to not worry about it.
   - Had this issue a second time trying to import the linked list. Adding -init-.py files into source code files worked.

---
## Demos
Coming soon...