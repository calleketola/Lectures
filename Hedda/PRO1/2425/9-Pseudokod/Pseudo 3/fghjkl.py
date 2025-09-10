import random

###############
## ÖVNING 01 ##
###############

"""
Implementera följande pseudokod:

lista := []
repeat x 10:
    lista append []
    repeat x 10:
        lista[-1] append random number
"""

lista = []
for i in range(10):
    lista.append([])
    for j in range(10):
        lista[-1].append(random.randint(0,9))
print(lista)

###############
## ÖVNING 02 ##
###############

"""
Implementera följande pseudokod:

data := ["1000\n","2000\n","3000\n","\n", "4000\n", "\n", "5000\n",
        "6000\n", "\n", "7000\n", "8000\n", "9000\n", "\n", "10000\n"]

elves := [[]]
FOR x IN data
    IF x = "\n"
        APPEND [] TO elves
    ELSE
        APPEND int(x) TO elves[-1]
PRINT elves
"""

data = ["1000\n","2000\n","3000\n","\n", "4000\n", "\n", "5000\n",
        "6000\n", "\n", "7000\n", "8000\n", "9000\n", "\n", "10000\n"]

elves = [[]]
for x in data:
    if x == "\n":
        elves.append([])
    else:
        elves[-1].append(int(x))
print(elves)


###############
## ÖVNING 03 ##
###############

"""
Implementera följande pseudokod:

sums := []
for i = 0 to length of elves
    sums append 0
    for j = 0 to length of elves[i]
        sums[i] := sums[i] + elves[i][j]

print max(sums)
"""
sums = []
for i in range(len(elves)):
    sums.append(0)
    for j in range(len(elves[i])):
        sums[i] = sums[i] + elves[i][j]
print(max(sums))


###############
## ÖVNING 04 ##
###############

"""
Implementera föjande psuedokod:

function MinSortering(lista):
    for i=1 to length of lista:
        index := 0
        for j=0 to length of lista - i+1:
             if lista[j] > lista[index]:
                  index := j
        t := lista[-i]
        lista[-i] := lista[index]
        lista[index] := t
    return lista
"""
def MinSortering(lista):
    for i in range(1,len(lista)):
        index = 0
        for j in range(len(lista)-i+1):
            if lista[j] > lista[index]:
                index = j
        t = lista[-i]
        lista[-i] = lista[index]
        lista[index] = t
    return lista

a = [7,3,5,1,6,9,4]
print(MinSortering(a))


###############
## ÖVNING 05 ##
###############

"""
Beskriv algoritmen i uppgift 4 med ord
och hitta namnet på algoritmen.
"""
