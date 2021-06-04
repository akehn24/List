# Design Notes
## Checklist Class
   - Simple ToDo list - items sorted vertically
   - Unsorted
   - Functions:
      - Create + Name
      - Add item
      - Remove item
      - View list
      - Delete list
   - Future features:
      - Save list
      - Check items off without removing them (bool)
      - Check/Uncheck all items at once
      - Show checked/unchecked items visually
      - Sort list by checked/unchecked
      - Move items around the list?
   - _Examples_:
     - To Do list / Chores list
     - List of ideas
     - Packing for travel checklist

---
## Inventory Class
   - Key/Value list
   - Sorted
   - Unique keys, non-unique values
   - _Examples_:
      - Character Sheet (for games like D&D)
      - !Things! Owned list / Inventory list
         - Books by author (titles would need to be unique)
         - Movies by genre
         - Items with numbers associated with them

---
## Categorical Class
   - Key/Value list
   - Like a Kanban Board - different categories hold tasks
   - Unsorted, items are called up by value
   - Non-unique keys, non-unique values
   - "Moving" an item = changing the value
   - Issues:
     - Unsure how hard it would be to implement a list whose keys are unique per value
   - _Examples_:
      - Kanban Board / Project Plan
      - Shopping list by grocery department
      - Tasks by day/week/month
