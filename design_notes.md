# Design Notes
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