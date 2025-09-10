class Person():

    def __init__(self, name, age, length):
        self.name = name
        self.age = age
        self.length = length

    def greet(self, other):
        print(f"Hello, {other.name} my name is {self.name} and I am {self.age} years old")

class Car():

    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color

    def drive(self):
        pass

    def honk(self):
        print(self.brand+": Tut tut!")

    def breaking(self):
        pass

bil = Car("Volvo", 2012, 'red')

bil.honk()
