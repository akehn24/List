################################################################
# Linked List for Checklist
################################################################

################################################################
# Node Class:
#   next_node   the node that comes after this one
#   value       the value the node is assigned
#   status      True = checked  /  False = not checked
################################################################
class Node:
    def __init__(self):
        self.next_node = None
        self.value = None
        self.status = False


################################################################
# Linked List Class:
#   insert                  inserts a node at the end of the list
#   remove_head             removes the head node only
#   delete                  deletes the node with the given value
#   delete_all_checked      deletes all checked nodes
#   delete_list             deletes the entire list
#   get_value               returns node with given value
#   change_status           checks/unchecks a node
#   size                    returns the size of the list
#   print                   prints the list
################################################################
class LinkedChecklist:
    ############################################################
    def __init__(self):
        self.head = None

    ############################################################
    # Inserts a new node at the end of the list
    def insert(self, value):
        new_node = Node()
        new_node.value = value
        curr = self.head

        # initial insert
        if self.head is None:
            self.head = new_node
            return

        # post-initial inserts
        # move curr to the end of the list
        while curr.next_node:
            curr = curr.next_node
        # insert at end
        curr.next_node = new_node

    ############################################################
    # Removes the head node
    def remove_head(self):
        curr = self.head
        curr = curr.next_node
        self.head = curr
        return

    ############################################################
    # Deletes the node of the given value
    def delete_node(self, value):
        curr = self.head
        prev = None

        # delete head
        if self.head.value == value:
            self.remove_head()
            return

        while curr:
            if curr.value == value:
                prev.next_node = curr.next_node
                return
            # move forward
            else:
                prev = curr
                curr = curr.next_node

    ############################################################
    # Deletes all nodes that are "checked" off - status = True
    def delete_all_checked(self):
        # delete head
        if self.head.status:
            self.head = self.head.next_node

        curr = self.head
        prev = None
        while curr:
            if curr.status:
                prev.next_node = curr.next_node
                break
            # move forward
            else:
                prev = curr
                curr = curr.next_node

    ############################################################
    # Deletes the entire list
    def delete_list(self):
        while self.head is not None:
            curr = self.head
            self.head = self.head.next_node
            curr = None

    ############################################################
    # Returns the Node with the given value
    def get_value(self, value):
        curr = self.head

        while curr:
            if curr.value == value:
                return curr
            else:
                curr = curr.next_node

        print("This item is not on the list.")
        return None

    ############################################################
    # "Checks" items off the list, or "unchecks" them
    def change_status(self, value):
        curr = self.get_value(value)

        if curr:
            if curr.status:
                curr.status = False
            else:
                curr.status = True

    ############################################################
    # Returns the size of the list
    def size(self):
        curr = self.head
        length = 0

        while curr:
            length += 1
            curr = curr.next_node

        return length

    ############################################################
    # Prints the list
    def print(self):
        curr = self.head

        while curr:
            if curr:
                # True = checked
                if curr.status:
                    print("x " + curr.value)
                    curr = curr.next_node
                # False = not checked
                else:
                    print("- " + curr.value)
                    curr = curr.next_node

'''
################################################################
# Testing !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
################################################################
link = LinkedChecklist()

print("\n")
print("--Insert Test--")
link.insert("1")
link.insert("2")
link.insert("3")
link.insert("4")
link.insert("5")
link.insert("6")
link.print()
print("Size is", link.size())
print("\n")

print("--Delete Test--")
link.delete_node("1")
link.print()
print("Size is", link.size())
print("\n")
link.delete_node("6")
link.print()
print("Size is", link.size())
print("\n")

print("--Check Test--")
link.change_status("1")
link.change_status("5")
link.print()
print("\n")
link.delete_all_checked()
link.print()
print("Size is", link.size())
print("\n")
'''
