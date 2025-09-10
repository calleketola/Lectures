class Node():

    def __init__(self, value):
        self.value = value
        self.next = None

class Queue():

    def __init__(self):
        self.root = None
        self.size = 0

    def put(self, value):
        if self.size == 0:
            self.root = Node(value)
        else:
            current = self.root
            while current.next != None:
                current = current.next
            current.next = Node(value)
        self.size += 1

    def get(self):
        if self.size != 0:
            self.root = self.root.next
            self.size -= 1

    def peek(self):
        if self.size != 0:
            return self.root.value
        else:
            return None

    def __repr__(self):
        out = ""
        current = self.root
        while current:
            out += str(current.value)+ '->'
            current = current.next
        return out[:-2] # Plockar bort sista ->
        

class Stack():

    def __init__(self):
        self.root = None
        self.size = 0

    def push(self, value):
        if self.size == 0:
            self.root = Node(value)
        else:
            new = Node(value)
            new.next = self.root
            self.root = new
        self.size += 1

    def pop(self):
        if self.size != 0:
            self.root = self.root.next
            self.size -= 1

    def peek(self):
        return self.root.value

    def __repr__(self):
        out = ""
        current = self.root
        while current:
            out += str(current.value)+ '->'
            current = current.next
        return out[:-2] # Plockar bort sista ->




# Detta är driver koden
import random

kö = Queue() # Skapa en tom kö
for i in range(5): 
    kö.put(random.randint(1,9)) # Lägger till ett slumpat tal
    print(kö)
for i in range(5):
    kö.get() # Plockar bort ett tal
    print(kö)


#min_stack = Stack()
#for i in range(5):
#    min_stack.push(random.randint(0,9))
#    print(f"Stacken: {min_stack} (pushed to stack)")
#for i in range(min_stack.size):
#    min_stack.pop()
#    print(f"Stacken: {min_stack} (popped from stack)")
