import random

###############
## UPPGIFT 1 ##
###############

"""
Skriv ut varje element i listan genom att
använda index och genom att använda "x in listan"
"""

# Nu har jag med end=" " för att det ska bli
# en snyggare utskrift och inte lika kladdigt
# i fönstret

roliga_siffror = [3,1,4,1,5,9,2,6,5,3,5,9]
# index:
for i in range(len(roliga_siffror)):
    print(roliga_siffror[i], end=" ")
print()

# tal in roliga_siffror:
for tal in roliga_siffror:
    print(tal, end=" ")
print()

###############
## UPPGIFT 2 ##
###############

"""
Gör samma sak igen!
"""

roliga_namn = [["Bilbo","Gandalf","Dwalin","Balin", "Kili", "Fili", "Dori", "Nori", "Ori", "Oin", "Gloin", "Bifur", "Bofur", "Bombur", "Thorin"], ["Frodo","Sam","Merry","Pippin","Gandalf","Aragorn","Boromir","Legolas","Gimli"]]

# index:
for i in range(len(roliga_namn)):
    for j in range(len(roliga_namn[i])):
        print(roliga_namn[i][j], end=" ")
    print()
# grupp i roliga_namn
for grupp in roliga_namn:
    for namn in grupp:
        print(namn, end=" ")
    print()
###############
## UPPGIFT 3 ##
###############

"""
Skriv en kod som räknar antalet treor i rutnätet
"""

rutnät = [[1,4,2,5,7,2,3,5,1,3],
          [5,2,3,1,5,8,0,5,2,3],
          [3,5,1,8,4,3,9,7,8,9],
          [0,0,1,5,7,9,2,9,0,7],
          [4,1,7,9,4,2,5,7,8,9],
          [1,7,4,2,7,3,9,6,4,0],
          [1,6,2,8,3,1,2,3,1,7],
          [6,3,1,8,5,2,8,2,5,1],
          [1,8,5,0,0,6,2,3,4,1],
          [3,3,3,3,1,1,8,5,2,3]]

# Sätt 1
treor = 0
for y in range(len(rutnät)):
    for x in range(len(rutnät[y])):
        if rutnät[y][x] == 3:
            treor += 1
print(f"Det är {treor} stycken treor i rutnätet")
# Sätt 2
treor = 0
for rad in rutnät:
    for tal in rad:
        if tal == 3:
            treor += 1
print(f"Det är {treor} stycken treor i rutnätet")


###############
## UPPGIFT 4 ##
###############

"""
Skriv en kod som genererar ett liknande rutnät som
i uppgiften ovan. (den är 10x10)

Den här uppgiften ska lösas med bara en rad kod.
"""

matris = [[random.randint(0,9) for i in range(10)] for j in range(10)]

for rad in matris:
    print(rad)

###############
## UPPGIFT 5 ##
###############

"""
Skriv ut summan av varje rad
"""
# Med sum
for rad in matris:
    print(sum(rad),end=" ")
print()
# Manuellt
for rad in matris:
    summa = 0
    for tal in rad:
        summa += tal
    print(summa, end=" ")
print()

###############
## UPPGIFT 6 ##
###############

"""
Skriv ut summan av varje kolumn
"""
# Här havererar sum
# Här är det lättast att ta alla kolumner samtidigt
summor = [0 for i in range(len(matris))]
for y in range(len(matris)):
    for x in range(len(matris[y])):
        summor[x] += matris[y][x]
print(summor)

###############
## UPPGIFT 7 ##
###############

"""
Skriv ut summan av hela matrisen
"""

# Det här är om möjligt lättare än den förra
summa = 0
for rad in matris:
    summa += sum(rad)
print(summa)
# Har vi redan löst den förra så är detta superlätt:
print(sum(summor))

###############
## UPPGIFT 8 ##
###############

"""
Skriv ut summan av diagonalen från
övre vänstra hörnet, och summan av
diagonalen från övre högre hörnet.
"""
diagonaler = [0,0]

for i in range(len(matris)): # Det här funkar eftersom den är kvadratisk
    diagonaler[0] += matris[i][i]
for i in range(len(matris)):
    for j in range(1, len(matris)+1):
        diagonaler[1] += matris[i][-j]

###############
## UPPGIFT 9 ##
###############

"""
Utgå från matrisen:

A = [[2,1],
     [1,2]]

Räkna ut matrisens DETERMINANT.
Du gör detta genom att ta produkten av
diagonalen från övre vänstra hörnet
minus produkten av diagonalen från det
lägre vänstra hörnet. (2*2-(1*1)=3)
"""
A = [[2,1],
     [1,2]]
# Eftersom vi tar produkter börjar vi på 1
diags = [1,1]
det = 0
for y in range(len(A)):
    diags[0] *= A[y][y]
    diags[1] *= A[y][-(y+1)]
det = diags[0]-diags[1]
print(det)

################
## UPPGIFT 10 ##
################

"""
Utgå från matrisen:

A = [[1,2,3],
     [4,2,5],
     [2,1,6]]

Räkna ut matrisens DETERMINANT.
Du tar summan av högerdiagonalernas
produkter och subtraherar med summan
av vänsterdiagonalernas produkter.
Alltså:
(1*2*6+2*5*2+3*4*1)-(2*2*3+1*5*1+6*4*2)=-21
"""
A = [[1,2,3],
     [4,2,5],
     [2,1,6]]

det = 0
# Eftersom vi tar produkter börjar vi från 1
h_diag = [1,1,1]
v_diag = [1,1,1] 
for a in range(len(A)): # Antal diagonaler
    for i in range(len(A)):
        h_diag[a] *= A[i][(i+a)%len(A)]

for a in range(len(A)): # Antal diagonaler
    for i in range(len(A)):
        v_diag[a] *= A[len(A)-(i+1)][(i+a)%len(A)]

det = sum(h_diag)-sum(v_diag)
print(det)

################
## UPPGIFT 11 ##
################

"""
Räkna ut DETERMINANTEN av en 10x10-
matris. (antingen den från uppg 3
eller en som du gjort i uppg 4)

Determinanten av matrisen från uppgift
3 är 3028848.
"""
A = rutnät
# Den här uppgiften kan bli identisk med den tidigare...
det = 0
# Eftersom vi tar produkter börjar vi från 1
h_diag = [1 for i in range(len(A))]
v_diag = [1 for i in range(len(A))]
for a in range(len(A)): # Antal diagonaler
    for i in range(len(A)):
        h_diag[a] *= A[i][(i+a)%len(A)]

for a in range(len(A)): # Antal diagonaler
    for i in range(len(A)):
        v_diag[a] *= A[len(A)-(i+1)][(i+a)%len(A)]

det = sum(h_diag)-sum(v_diag)
print(det)
