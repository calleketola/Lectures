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

##############
## ÖVNING 2 ##
##############

"""
Skriv ut hur många tal det är i
varje lista.
"""

##############
## ÖVNING 3 ##
##############

"""
Skriv ut summan av alla jämna
tal i listan.
"""

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

##############
## ÖVNING 5 ##
##############

"""
Hur många minor finns det runt
positionen 0,4?
"""


##############
## ÖVNING 6 ##
##############

"""
Hur många minor finns det runt
positionen 7,9?
"""


##############
## ÖVNING 7 ##
##############

"""
Skapa ett nytt rutnät där det
står hur många minor som finns
runt VARJE position ur det
första rutnätet.
"""












