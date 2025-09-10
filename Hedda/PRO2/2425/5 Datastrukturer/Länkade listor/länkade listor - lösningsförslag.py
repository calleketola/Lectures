class Node():

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():

    def __init__(self):
        self.root = Node("root")
        self.size = 0

    def __repr__(self):
        out_string = "["
        current = self.root.next
        while current:
            out_string += f"{current.value},"
            current = current.next
        if self.size > 0:
            out_string = out_string[:-1]+"]"
        else:
            out_string = "[]"
        return out_string

    def insert(self, i, value):
        # Control that the index is good
        if i > self.size or i < 0:
            raise IndexError("Index out of bounds")
        # Special case when i is 0
        if i == 0:
            # Store the tail
            temp = self.root.next
            # Replace tail with new item
            self.root.next = Node(value)
            # Put tail on the new item
            self.root.next.next = temp
            self.size += 1
        else:
            # Traverse the list i steps
            current = self.root
            for k in range(i):
                current = current.next
            # Store the tail of the list
            temp = current.next
            # Replace the tail with the new item
            current.next = Node(value)
            # Put the tail on the new item
            current.next.next = temp
            self.size += 1

    def peek(self, i):
        # Control that the index is good
        if self.size == 0:
            raise Exception("Peeking at empty queue")
        if i > self.size or i < 0:
            raise IndexError("Index out of bounds")
        # Traverse the list i steps
        current = self.root
        for k in range(i+1):
            current = current.next
            
        return current.value

            
    def pop(self, i):
        # Control that the index is good
        if self.size == 0:
            raise Exception("Popping an empty queue")
        if i > self.size or i < 0:
            raise IndexError("Index out of bounds")
        # Move to correct position
        current = self.root
        for k in range(i-1):
            current = current.next
        # Replace the next item with its next item    
        current.next = current.next.next
        self.size -= 1















    

# Detta är driver koden

import random

linked = LinkedList() # Skapa en tom lista
# Fill the list
x = random.randint(0,9)
linked.insert(0, x) # Lägger till ett slumpat tal
print(linked, f"Inserted {x} to pos 0")
x = random.randint(0,9)
linked.insert(0, x) # Lägger till ett slumpat tal
print(linked, f"Inserted {x} to pos 0")
x = random.randint(0,9)
linked.insert(1, x)
print(linked, f"Inserted {x} to pos 1")
x = random.randint(0,9)
linked.insert(1, x)
print(linked, f"Inserted {x} to pos 1")
x = random.randint(0,9)
linked.insert(3, x)
print(linked, f"Inserted {x} to pos 3")
x = random.randint(0,9)
linked.insert(5, x)
print(linked, f"Inserted {x} to pos 5")
# Peek at items
print(linked.peek(0), "is the item at position", 0)
print(linked.peek(1), "is the item at position", 1)
print(linked.peek(2), "is the item at position", 2)
print(linked.peek(3), "is the item at position", 3)
print(linked.peek(4), "is the item at position", 4)
print(linked.peek(5), "is the item at position", 5)
# Remove items
linked.pop(5)
print(linked, "Removed the item at position", 5)
linked.pop(0)
print(linked, "Removed the item at position", 0)
linked.pop(2)
print(linked, "Removed the item at position", 2)
linked.pop(1)
print(linked, "Removed the item at position", 1)
linked.pop(0)
print(linked, "Removed the item at position", 0)
linked.pop(0)
print(linked, "Removed the item at position", 0)
