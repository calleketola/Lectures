class Person():

    def __init__(self, year, month,day, n):
        self.birth_year = year
        self.birth_month = month
        self.birth_day = day
        self.name = n

    def get_birthday(self):
        b_day = str(self.birth_year)
        b_day += str(self.birth_month)
        b_day += str(self.birth_day)
        return b_day

    def greet(self, name):
        return "Hej, {}! Jag heter {}".format(name, self.name)

    def __repr__(self):
        return str(self.name)+" "+str(self.birth_year)

p1 = Person(91,10,15, "Calle")
p2 = Person(3,2,20, "Linus")

print(p1.greet(p2.name))

print(p1)
print(p2)
