class Person():

    def __init__(self, name, age, length):
        self.name = name
        self.age = age
        self.length = length

    def greet(self, annan):
        print(f"Hello, {annan}, I am {self}")

    #def __repr__(self):
    #    return f"{self.name} who is {self.age} years old"

    def __add__(self, other):
        return self.name+other.name


calle = Person("Calle", 32, 181)
x = Person("Daniel", 18, 185)

calle.greet(x.name)
