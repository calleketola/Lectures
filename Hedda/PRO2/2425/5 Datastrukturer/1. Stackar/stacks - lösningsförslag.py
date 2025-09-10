class Node():

    def __init__(self, value):
        self.value = value
        self.next = None

class Stack():

    def __init__(self):
        self.root = Node('root')
        self.size = 0

    def __str__(self):
        string = ""
        current = self.root.next
        while current:
            string += str(current.value)+ '->'
            current = current.next
        return string[:-2] # Plockar bort sista ->

    def peek(self):
        """
        Kikar på översta elementet
        """
        if self.size == 0:
            raise Exception("Peeking on an empty stack")
        return self.root.next.value

    def push(self, value):
        """
        Lägger till ett element överst i stacken
        """
        node = Node(value)
        node.next = self.root.next
        self.root.next = node
        self.size += 1

    def pop(self):
        """
        Plockar bort översta elementet
        """
        if self.size == 0:
            raise Exception("Popping an empty stack")

        remove = self.root.next # Detta är det första elementet
        self.root.next = remove.next # Flyttar ner oss
        self.size -= 1
        return remove.value

    def __repr__(self):
        return self.__str__()
















        
# Driver code
import random

min_stack = Stack()
for i in range(5):
    min_stack.push(random.randint(0,9))
    print(f"Stacken: {min_stack} (pushed to stack)")
for i in range(min_stack.size):
    min_stack.pop()
    print(f"Stacken: {min_stack} (popped from stack)")


















    
    
