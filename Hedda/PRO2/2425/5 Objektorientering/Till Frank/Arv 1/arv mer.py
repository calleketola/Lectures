class Person():

    def __init__(self, name, birth, length):
        self.name = name
        self.birth = birth
        self.length = length

        self.age = 2024-self.birth

    def greet(self):
        return f'My name is {self.name}'

class Student(Person):

    def __init__(self, name, birth, length, school, group):
        super().__init__(name, birth, length)

        self.school = school
        self.group = group

    def greet(self):
        return 'Yo'

class Child(Person):

    def __init__(self, name, birth, length):
        super().__init__(name, birth, length)

    def grow(self, x):
        self.length += x

    def greet(self):
        return f'Jag heter {self.name} och är {self.length} cm'



p1 = Person('Calle', 1991, 181)
p2 = Student('Ludvig', 2005, 170, 'Hedda', 'Te21a')
p3 = Student('Abdul', 2005, 193, 'Hedda', 'Te21b')
p4 = Child('Johannes', 2024, 45)

personer = [p1,p2,p3, p4]

personer[3].grow(5)
for peep in personer:
    print(peep.greet())
