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
- Use multiple styles of data structures to create lists
- Read/Write to text files to save list data
- Practice taking user input - terminal for now, GUI later
- Create a navigatable menu for a user to input data

### Task List:
:heavy_check_mark: Create a simple list using data structures   
:heavy_check_mark: Fix import files bug

:heavy_check_mark: Implement a linked list for the Checklist    
:x: Check/Uncheck all items at once  
:x: Sort items by checked/unchecked  
:x: Integrate the linked list into the current Checklist code  

:x::warning: Figure out why TOC links aren't working

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
:x: Inventory List  
:x: Categorical List  

---
## Technologies
- Visual Studio Code
- Pycharm
- Python

## Data Structs and Algorithms
- Python Lists
- Linked List

---
## Bugs
- Importing a file:
   - Pylance has issues with importing local files. [Info here](https://github.com/microsoft/pylance-release/blob/main/TROUBLESHOOTING.md#unresolved-import-warnings)
   - Tried their fix of adding the directory path to the setting.json file - did not seem to work
   - Found a workaround to tell Pylance to ignore the line, but the import does not work this way.
   - Switching to Pycharm to see if the import will work there (it does).
- Pycharm bug - cannot find reference 'function_name' in '-init-.py'
   - There are apparently a few fixes, but putting '# noinspection PyUnresolvedReferences' on the line above the ref tells Pycharm to not worry about it.

---
## Demos
Coming soon...