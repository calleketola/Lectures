import random

##############
## ÖVNING 1 ##
##############

"""
Skapa en lista som innehåller ett
slumpmässigt antal listor (1 till
12 stycken).

Varje lista ska innehålla ett
slumpmässigt antal tal (1 till 12
stycken).
"""
print("ÖVNING 1")
lista_1 = []
for i in range(random.randint(1,12)):
    lista_1.append([])
    for j in range(random.randint(1,12)):
        lista_1[i].append(random.randint(1,100))

for rad in lista_1:
    print(rad)

##############
## ÖVNING 2 ##
##############

"""
Skriv ut hur många tal det är i
varje lista.
"""

print("ÖVNING 2")
for lista in lista_1:
    print(len(lista))

##############
## ÖVNING 3 ##
##############

"""
Skriv ut summan av alla jämna
tal i listan.
"""

print("ÖVNING 3")
summa = 0
for i in range(len(lista_1)):
    for j in range(len(lista_1[i])):
        if lista_1[i][j] % 2 == 0:
            summa += lista_1[i][j]
print("Summan av alla jämna tal:", summa)


##############
## ÖVNING 4 ##
##############

"""
I spelet Röj (Minesweeper på
engelska) så ligger ett antal
minor doldad i ett rutnät. När
spelaren klickar på en ruta så
kommer det upp ett tal som visar
hur många minor som ligger
i en av rutorna som ligger
granne med rutan spelaren
klickade på.

Räkna hur många av grannarna
runt rutan i position 3,5 har.
"""

print("ÖVNING 4")
# Den här koden skapar ett rutnät
grid = []

for rad in range(10): # Tio rader
    grid.append([]) # Lägg till tom rad
    for kol in range(10): # Tio kolumner
        if random.randint(1,8) == 1: # 1 på 8 att det är en mina
            grid[rad].append("X")
        else:
            grid[rad].append("O")

# Den här koden skriver ut rutnätet
for rad in grid:
    for kol in rad:
        print(kol, end=" ")
    print()

grannar = 0
rad = 3
kol = 5
for i in range(-1,2):
    for j in range(-1,2):
        if i == 0 and j == 0:
            continue # Hoppa 3,5
        if grid[i][j] == "X":
            grannar += 1

print("rad 3, kolumn 5, har", grannar, "grannar")            
##############
## ÖVNING 5 ##
##############

"""
Hur många minor finns det runt
positionen 0,4?
"""

print("ÖVNING 5")
grannar = 0
rad = 0
kol = 4
for i in range(-1,2):
    for j in range(-1,2):
        if i == 0 and j == 0:
            continue # Hoppa 0,4
        # Kontroller att vi är i nätet
        if rad+i>0 and kol+j>0 and grid[i][j] == "X":
            grannar += 1
print("rad 0, kolumn 4, har", grannar, "grannar")            
    

##############
## ÖVNING 6 ##
##############

"""
Hur många minor finns det runt
positionen 7,9?
"""

print("ÖVNING 6")
grannar = 0
rad = 0
kol = 4
for i in range(-1,2):
    for j in range(-1,2):
        if i == 0 and j == 0:
            continue # Hoppa 7,9
        # Kontroller att vi är i nätet
        if rad+i<10 and kol+j<10 and grid[i][j] == "X":
            grannar += 1
print("rad 7, kolumn 9, har", grannar, "grannar")            
   

##############
## ÖVNING 7 ##
##############

"""
Skapa ett nytt rutnät där det
står hur många minor som finns
runt VARJE position ur det
första rutnätet.
"""

print("ÖVNING 7")
ny = [[0 for i in range(10)] for i in range(10)]

for rad in range(10):
    for kol in range(10):
        if grid[rad][kol] == "X":
            ny[rad][kol] = "X"
            continue
        for i in range(-1,2):
            for j in range(-1,2):
                if rad+i >= 10 or kol+j >= 10:
                    continue
                if rad+i < 0 or kol+j < 0:
                    continue
                if i == 0 and j == 0:
                    continue
                if grid[rad+i][kol+j] == "X":
                    ny[rad][kol] += 1
        

for rad in ny:
    for tal in rad:
        print(tal, end=" ")
    print()







