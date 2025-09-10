class Person():

    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def __str__(self):
        return self.name + " " + str(2024-self.birth_year)

    def __repr__(self):
        return str(self)

class Teacher(Person):

    def __init__(self, name, birth_year, school, subjects):
        super().__init__(name, birth_year)
        self.school = school
        self.subjects = subjects

    def __str__(self):
        out = super().__str__()
        for sub in self.subjects:
            out += " "+sub
        return out


class Student(Person):

    def __init__(self, name, birth_year, school, group):
        super().__init__(name, birth_year)
    
        self.school = school
        self.group = group

        self.grades = {}

    def add_grade(self, course, grade):
        self.grades[course] = grade

    def calculate_merit(self):
        system = {"A": 20, "B": 17.5, "C": 15, "D": 12.5, "E": 10, "F": 0}
        point_sum = 0
        for course in self.grades:
            if "Gymnasiearbete" not in course:
                point_sum += self.grades[course][1]
        merit = 0
        for course in self.grades:
            if "Gymnasiearbete" not in course:
                merit += (system[self.grades[course][0]]*self.grades[course][1])/point_sum
        return merit

    def __str__(self):
        out = super().__str__()
        out += " " + self.school + " " + self.group
        return out


class Course():

    def __init__(self, name, points):
        self.name = name
        self.points = points
    
        self.students = []
        self.teachers = []

    def add_student(self, stud):
        if stud not in self.students:
            self.students.append(stud)

    def add_teacher(self, teacher):
        if teacher not in self.teachers:
            self.teachers.append(teacher)

    def set_student_grade(self, stud, grade):
        for s in self.students:
            if s == stud:
                s.add_grade(self.name, [grade, self.points])

    def __repr__(self):
        out = self.name + " " + str(self.points)
        out += "("
        for t in self.teachers:
            out += " "+t.name
        out += ")"
        return out

import random

students = [Student("Calle", 1991, "Spyken", "Na07b"),
	    Student("Johannes", 1991, "Katedralskolan", "Ek07c"),
	    Student("Carin", 1987, "Polhemskolan", "Na03a")]

courses = [Course("Matematik 1c", 100),
           Course("Matematik 2c", 100),
           Course("Matematik 3c", 100),
           
           Course("Svenska 1", 100),
           Course("Svenska 2", 100),
           Course("Svenska 3", 100),
           
           Course("Engelska 5", 100),
           Course("Engelska 6", 100),

           Course("Teknik 1", 150),
           Course("Fysik 1a", 150),
           Course("Kemi 1", 100),

           Course("Programmering 1", 100),
           Course("Programmering 2", 100),
           Course("Webbutveckling 1", 100),

           Course("Dator- och nätverksteknik 1", 100),
           Course("Digital kommunikationsteknik", 100),

           Course("Historia 1b", 50),
           Course("Religion 1", 50),
           Course("Samhällskunskap 1", 100),

           Course("Entreprenörskap", 100),
           Course("Idrott och hälsa 1", 100),

           Course("Gymnasiearbete - Teknikprogrammet", 100),

           Course("Individuellt val 1", 100),
           Course("Individuellt val 2", 100),

           Course("Programfördjupnng 1", 100)]

for c in courses:
    c.add_student(students[0])
for c in courses:
    c.set_student_grade(c.students[0], random.choice(["A","B","C","D","E","F"]))

print(students[0].calculate_merit())
