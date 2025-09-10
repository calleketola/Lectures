def största_slö(lista):
    lista.sort()
    return lista[-1]

def största(lista):
    störst = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > störst:
            störst = lista[i]
    return störst

import random

def mellantal(tal1, tal2):
    return (tal1+tal2)/2

tal = [random.randint(0,100) for i in range(10)]
print(tal)
print(största(tal))
tal += [random.randint(0,100) for i in range(10)]
print(tal)
print(största(tal))
t1 = random.randint(1,10)
t2 = random.randint(1,10)
print(t1,t2)
print(mellantal(t1,t2))

