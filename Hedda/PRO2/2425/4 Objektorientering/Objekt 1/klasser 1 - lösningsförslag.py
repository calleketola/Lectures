class Person():

    def __init__(self, name, age, length):
        self.name = name
        self.age = age
        self.length = length

    def greet(self):
        print(f"Hello, my name is {self.name}")




calle = Person("Calle", 32, 181)

calle.greet()
