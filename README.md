# List Maker
## Implementation of an Evolving List

I use lists frequently in my day-to-day life so I programmed an application that could create the types of lists I want.

## Table of Contents
- [Project Status](#project-status)
   - [Goals](#goals)
   - [Task List](#task-list)
   - [Future Tasks](#future-tasks)
- [Technologies](#technologies)
- [Bugs](#bugs)
- [Demos](#demos)
- [Sources](#sources)

---
## Project Status :green_circle:
### Goals
- Use multiple styles of data structures to create usable lists
- Read/Write to text files to save list data
- Practice taking user input - terminal for now, GUI later
- Create a navigatable menu for a user to input data
- Keep everything streamlined and easily understandable for the user

### Task List:
:heavy_check_mark: Create a simple list using data structures   
:heavy_check_mark: Fix import files bug  
:heavy_check_mark: Implement a linked list for the Checklist  
:heavy_check_mark: Integrate the linked list into the current Checklist code  
:heavy_check_mark: Basic Inventory List  
:heavy_check_mark: Movie / Book Inventory Lists  
:heavy_check_mark: Fix TOC Links (woohoo!)  
:recycle: Character Sheet Class  
:x: Categorical List Class  
:x: Categorical List driver

<!--- 
Emojis for the Task List:
DONE =      :heavy_check_mark:
NOT DONE =  :x:
WIP =       :recycle:
BUGGED =    :warning:
 --->

### Future Tasks  
:x: Attempt to create an actual user interface  
:x: Write lists to text files for saving  

### Feature Creep
- Checklist:
   - :x: Check/Uncheck all items at once
   - :x: Sort items by checked/unchecked

---
## Technologies
- Visual Studio Code
- Pycharm
- Python
- Git Bash / GitHub

## Knowledge Used
- Object Oriented programming
- Classes and Objects
- Python Lists
- Linked List
- Python Dictionaries
- Drivers to direct the flow of the program

---
## Design
### Checklist
- Implemented a Linked List Class to handle the data and functionality of the list.
- A driver file directs the user through list manipulation by using the functionality of the Linked List Class. 
### Inventory
- A general Inventory List Class handles the data and functionality of the Inventory drivers.
- I decided to implement each type of Inventory List driver separately since the user dialogue would be different for each of them.
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
- Dict has no attribute:
   - Changed Inventory list functions into a Class. Now having issues adding key:value pairs to the dict. Calling the class method 'add_item' throws error:
      - *AttributeError: 'dict' object has no attribute 'add_item'*
   - When I converted my methods over to be contained in a Class, I misunderstood how certain assignments and function calls would work. Took some digging through the code to figure out what was going on! (and every Inventory driver was affected!)

---
## Demos
Coming soon...
