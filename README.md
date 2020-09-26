# List 👩🏻‍💻
## Implementation of an Evolving List

I enjoy making lists. I very much enjoy making lists. Though it seems like a simple project, when told to do something I'm interested in... I chose lists.

In reality, I'm using my love of lists to practice some coding basics to keep myself in the swing of things.

---

## 📋 Goals 📋
* Practice inheritance with a base List class and subclasses
* Use multiple styles of data structure to create lists
* Read/Write to text files to save list data
* Practice taking user input - terminal for now
* Creating a navigatable menu for the user to input data
* Practice using templates and taking any data TYPE the user inputs

### Future Goals
* Attempt to create an actual user interface

---

## 📋 Plans 📋
1. List Class - base class to create a simple list.
   - think of a simple ToDo list - items in a vertical row
   - unsorted
   - simple add/remove/create/delete/print
   - __Examples__:
     - To Do list
     - Ideas list
2. Checklist Subclass - simple list where items can be 'checked off' without being removed
   - unsorted, but can be sorted by incomplete/completed
   - very similar to the base class, with added bool assignments to each item
   - __Options__:
     - Checklist item stays where it's at after being completed
     - Checklist is sorted by incompleted (top) / completed (bottom)
       - when an item is completed, it's moved to the bottom of the list
       - acts like two lists on top of each other
   - __Examples__:
     - Tracking To Do list - you want to see how well you did completing tasks
3. Inventory Subclass - key/value list
   - sorted
   - unique keys, non-unique values
   - __Issues__:
     - Having trouble figuring out why this inherits from the base List if it's overriding all of List's functions?
       - I had initially written out 'types of lists' to create as subclasses, but after design, realized this list (and the categorical list) have to override everything due to being a different data structure style. ?????
       - Is this going to be a 'I created multiple List classes!' project?
4. Categorical Subclass - key/value list
   - like a kanban board - different categories hold tasks
   - unsorted, items are called up by value
   - non-unique keys, non-unique values
   - "moving" an item = changing the value
   - __Issues__:
     - Unsure how hard it would be to implement a list whose keys are unique per value

### As I get through writing this, I'm realizing this needs to be done differently. Yay design phase!
1. List base class
   - Checklist subclass
2. Inventory base class
   - Books To Read 
   - Character Bio 
3. Categorical base class
   - Kanban Board / Project Plan
   - Shopping list by grocery dept.
     
