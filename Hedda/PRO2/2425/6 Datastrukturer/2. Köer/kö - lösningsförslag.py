class Node():

    def __init__(self, value):
        self.value = value
        self.next = None

class Queue():

    def __init__(self):
        self.root = Node("root")
        self.size = 0

    def __str__(self):
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

    def __repr__(self):
        return self.__str__()

    def put(self, value):       
        current = self.root
        while current.next:
            current = current.next
        current.next = Node(value)
        self.size += 1

    def front(self):
        if self.size == 0:
            raise Exception("Peeking at empty queue")
        return self.root.next.value

    def rear(self):
        if self.size == 0:
            raise Exception("Peeking at empty queue")

        current = self.root.next
        while current.next:
            current = current.next
        return current.value
            
    def get(self):
        if self.size == 0:
            raise Exception("Popping an empty queue")
        out = self.root.next
        self.root.next = out.next
        self.size -= 1
        return out.value















    

# Detta är driver koden

import random

kö = Queue() # Skapa en tom kö
for i in range(5): 
    kö.put(random.randint(1,9)) # Lägger till ett slumpat tal
    print(kö)
for i in range(5):
    kö.get() # Plockar bort ett tal
    print(kö)
