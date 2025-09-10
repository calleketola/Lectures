#####################
## UPPGIFT 1, 2, 3 ##
#####################

lista1 = ['Frodo', 'Sam', 'Aragorn', 'Boromir', 'Legolas', 'Gandalf']

lista1.append('Gimli')
lista1.insert(2, 'Merry')
lista1.insert(3, 'Pippin')
print(lista1)


###############
## UPPGIFT 4 ##
###############

lista4 = ['n','i',' ','t','a','l','a','r',' ','b','r','a',' ','l','a','t','i','n']
lista4r = []
i = 1
while i < len(lista4)+1:
    lista4r.append(lista4[-i])
    i += 1
print(lista4r)

###############
## UPPGIFT 5 ##
###############

lista5 = [3,6,1,1,3,5,4,3,9,10,0,6,8,7,3]

i = 0
while i < len(lista5):
    if lista5[i]%2==1: # Udda
        lista5.pop(i)
    else:
        i += 1
print(lista5)

###############
## UPPGIFT 6 ##
###############

lista6 = ["Hej", 6, 7.6, "alla", 9.1, 1.2, 2, 'barn']
listaf = []
listai = []
listas = []
i = 0
while i < len(lista6):
    if type(lista6[i]) == str:
        listas.append(lista6[i])
    elif type(lista6[i]) == int:
        listai.append(lista6[i])
    elif type(lista6[i]) == float:
        listaf.append(lista6[i])
    i += 1
print(listas)
print(listai)
print(listaf)


###############
## UPPGIFT 7 ##
###############

lista7 = [1,4,9,1,2,1,8,4,1,9]
i = 0
while i < len(lista7):
    lista7[i]*=2
    i += 1
print(lista7)

###############
## UPPGIFT 8 ##
###############

lista8 = ['n','i',' ','t','a','l','a','r',' ','b','r','a',' ','l','a','t','i','n']

i = 0
while i < len(lista8):
    summa = 0
    j = 0
    while j < len(lista8):
        if lista8[i] == lista8[j]:
            summa += 1
        j += 1
    print(f"{lista8[i]} förekommer {summa} gång(er)")
    i += 1

###############
## UPPGIFT 9 ##
###############

# Det finns MÅNGA sorteringsalgoritmer
# Implementera gärna mer än en.

lista9 = [6,3,8,59,9,123,53,345,10,3,7,2,5,1,9,63,267,34]

# Bubble sort
switcharoos = 0
lista9a = lista9.copy()
i = 0
while i < len(lista9a):
    j = 1
    while j < len(lista9a)-i:
        # Jämför
        if lista9a[j] < lista9a[j-1]:
            # Här sker bytet
            #temp = lista9a[j]
            #lista9a[j] = lista9a[j-1]
            #lista9a[j-1] = temp
            lista9a[j], lista9a[j-1] = lista9a[j-1], lista9a[j]
            switcharoos += 1
        j += 1
    i += 1
print("BUBBLESORT:")
print(lista9a)
print(f"Number of switches: {switcharoos}")

# Selection sort
lista9b = lista9.copy()
switcharoos = 0
for i in range(len(lista9b)):
    # Hitta minsta talet av de som är kvar:
    minimum = i
    for j in range(i,len(lista9b)):
        if lista9b[j] < lista9b[minimum]:
            minimum = j
    # Byt plats
    lista9b[i], lista9b[minimum] = lista9b[minimum], lista9b[i]
    switcharoos += 1


print("SELECTION SORT")
print(lista9b)
print(f"Number of switches: {switcharoos}")

# Quicksort
lista9c = lista9.copy()

switcharoos = 0

def quicksort(lista):
    global switcharoos
    # Välj ett pivot-element
    pivot = len(lista)-1
    counter = 0
    if pivot > 0:
        for i in range(len(lista)-1):
            # Om talet är mindre än pivot-talet flytta det
            if lista[i] <= lista[pivot]:
                if i != counter:
                    for j in range(counter, len(lista[:pivot])):
                        lista[i], lista[j] = lista[j], lista[i]
                        switcharoos += 1
                        break
                counter+=1
        # Flytta pivot
        temp = lista[pivot]
        lista[pivot] = lista[counter]
        lista[counter] = temp
        switcharoos += 1
        #Nu är pivot-talet på rätt plats.
        # Nu delar vi upp listan i två, den före pivot och den efter pivot
    if len(lista) > 1:
        lista[:counter] = quicksort(lista[:counter])
        lista[counter:] = quicksort(lista[counter:])
    return lista
    
print("QUICKSORT")
quicksort(lista9c)
print(lista9c)
print(f"Number of switches: {switcharoos}")

def selectionsort(lista):
    global switcharoos
    for i in range(len(lista)):
        # Hitta minsta talet av de som är kvar:
        minimum = i
        for j in range(i,len(lista)):
            if lista[j] < lista[minimum]:
                minimum = j
        # Byt plats
        lista[i], lista[minimum] = lista[minimum], lista[i]
        switcharoos += 1
def bubblesort(lista):
    # Bubble sort
    global switcharoos
    for i in range(len(lista)):
        for j in range(1,len(lista)-i):
            # Jämför
            if lista[j] < lista[j-1]:
                # Här sker bytet
                lista[j], lista[j-1] = lista[j-1], lista[j]
                switcharoos += 1


print("More comparisons:")
# Now we create a large list with random elements
import random
randomized_list = []
n = 10000
print(f"Creating list of {n} random elements")
for i in range(10000):
    randomized_list.append(random.randint(1,100000))
print("List created")
rand_list_1 = randomized_list.copy()
rand_list_2 = randomized_list.copy()
rand_list_3 = randomized_list.copy()

import timeit

print("Bubblesort:")
switcharoos = 0
t = timeit.timeit('[func(rand_list_1) for func in [bubblesort]]',number = 1, globals=globals())
print(f"Switches: {switcharoos}")
print(f"Time: {t}")
print("Selection sort:")
switcharoos = 0
t = timeit.timeit('[func(rand_list_2) for func in [selectionsort]]',number = 1, globals=globals())
print(f"Switches: {switcharoos}")
print(f"Time: {t}")
print("Quicksort:")
switcharoos = 0
t = timeit.timeit('[func(rand_list_3) for func in [quicksort]]',number = 1, globals=globals())
print(f"Switches: {switcharoos}")
print(f"Time: {t}")
