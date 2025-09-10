import timeit

# Skapa en lista med massa tal
numbers = [x for x in range(1,100)]

def sum_while():
    summa = 0
    i = 0
    while i < len(numbers):
        summa += numbers[i]
        i += 1
    return summa

def sum_for():
    summa = 0
    for i in range(len(numbers)):
        summa += numbers[i]
    return summa

def sum_sum():
    summa = 0
    summa = sum(numbers)
    return summa

def sum_math():
    summa = 0
    summa = len(numbers)*(numbers[0]+numbers[-1])/2
    return summa

the_while = timeit.timeit(stmt="sum_while()",
                  setup = """numbers = [x for x in range(1,100)]
def sum_while():
    summa = 0
    i = 0
    while i < len(numbers):
        summa += numbers[i]
        i += 1
    return summa 
""", number=10)
the_for = timeit.timeit(stmt="sum_for()",
                  setup = """numbers = [x for x in range(1,100)]
def sum_for():
    summa = 0
    for i in range(len(numbers)):
        summa += numbers[i]
    return summa 
""", number=10)
the_sum = timeit.timeit(stmt="sum_sum()",
                  setup = """numbers = [x for x in range(1,100)]
def sum_sum():
    summa = 0
    summa = sum(numbers)
    return summa
""", number=10)
the_math = timeit.timeit(stmt="sum_math()",
                  setup = """numbers = [x for x in range(1,100)]
def sum_math():
    summa = 0
    summa = len(numbers)*(numbers[0]+numbers[-1])/2
    return summa
""", number=10)

print("Tid med while:", the_while)
print("Tid med for:", the_for)
print("Tid med sum:", the_sum)
print("Tid med matte:", the_math)
