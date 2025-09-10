class Node():

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():

    def __init__(self):
        self.root = Node("root")
        self.size = 0

    def insert(self, i, value):
        """
        På plats i stoppa in value
        """
        if i > self.size:
            raise IndexError
        # Skapa vår nod
        new = Node(value)
        # Plocka fram root
        current = self.root
        # Gå fram till noden före den vi vill stoppa in
        for k in range(i):
            current = current.next
        # Plocka loss svansen och sätt på den nya
        new.next = current.next
        # Peka nu på den nya istället
        current.next = new
        # Uppdatera size
        self.size += 1

    def peek(self, i):
        """
        Metod som tittar på elementet på plats i 
        """
        if i > self.size:
            raise IndexError
        # Start
        current = self.root.next
        for k in range(i):
            current = current.next
        return current.value

    def __repr__(self):
        """
        En metod som gör att print(LinkedList) ser 
        ut som en vanlig lista.
        """
        out_string = "["
        current = self.root.next
        while current:
            out_string += f"{current.value},"
            current = current.next
        if self.size > 0:
            # Ta bort det sista kommatecknet och lägg
            # till en slutparantes
            out_string = out_string[:-1]+"]"
        else:
            out_string = "[]"
        return out_string




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
