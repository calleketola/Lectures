name = input("Your name: ")
age = int(input("Your age: ")) # Vi castar till en int
print("Hello,", name, "you are", age, "years old")

float("4.4")
bool(1)
str(1)
list("asd")

name = input("May I have your name, please?" )
if len(name) > 6:
    print("Your name is too long, I do not want it.")
elif len(name) < 3:
    print("Your name is too short, not fit for me.")
else:
    print("Thank you, your name is now mine.")

i = 0
while i < 10:
    print(i)
for i in range(10):
    print(i)

def my_function(par1, par2):
    res = par1+par2
    return res
a = 1
b = 2
print(my_function(a, b))

hobbits = ["Sam", "Frodo", "Merry", "Pippin", "Fatty"]
print(hobbits[0])

matrix = [[1,2,3], [4,5,6], [7,8,9]]
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(matrix[row][col])

# Detta är en kommentar
"""
Detta är en lång kommentar
"""
my_long_name = 0

# Detta är okej Python-kod
a = 5
a = 5.5
a = "Hej"

# Python
name = input("Name: ")
age = int(input("Age: "))
print(name, age)
c, d = True, True
if a == True and b == False:
    pass
elif c == True or d == True:
    pass
else:
    pass

# En while-loop i Python
i = 0
while i < 10:
    print(i)
    i += 1

# For-loop i Python
for i in range(0,10,1): # Start, Stop, Steg
    print(i)

# Funktion i Python
def my_function(par1, par2):
    result = par1+par2
    return result

# Lista i Python
min_lista = [3,1,4,1,5]
print(min_lista[0])
