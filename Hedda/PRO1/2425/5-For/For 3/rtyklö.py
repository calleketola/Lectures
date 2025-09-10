import random

###############
## UPPGIFT 1 ##
###############

"""
Skriv ut varje element i listan genom att
använda index och genom att använda "x in listan"
"""

roliga_siffror = [3,1,4,1,5,9,2,6,5,3,5,9]
# index:
for i in range(len(roliga_siffror)):
    print(roliga_siffror[i])
### tal in roliga_siffror:
for tal in roliga_siffror:
    print(tal)

###############
## UPPGIFT 2 ##
###############

"""
Gör samma sak igen!
"""

roliga_namn = [["Bilbo","Gandalf","Dwalin","Balin",
                "Kili", "Fili", "Dori", "Nori",
                "Ori", "Oin", "Gloin", "Bifur",
                "Bofur", "Bombur", "Thorin"],
               ["Frodo","Sam","Merry","Pippin",
                "Gandalf","Aragorn","Boromir",
                "Legolas","Gimli"]]

# index:
for i in range(len(roliga_namn)): # Gör två gånger
    for j in range(len(roliga_namn[i])):
        print(roliga_namn[i][j])
### grupp i roliga_namn
for grupp in roliga_namn:
    for namn in grupp:
        print(namn)

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



###############
## UPPGIFT 4 ##
###############

"""
Skriv en kod som genererar ett liknande rutnät som
i uppgiften ovan. (den är 10x10)

Den här uppgiften ska lösas med bara en rad kod.
"""

###############
## UPPGIFT 5 ##
###############

"""
Skriv ut summan av varje rad
"""

###############
## UPPGIFT 6 ##
###############

"""
Skriv ut summan av varje kolumn
"""


###############
## UPPGIFT 7 ##
###############

"""
Skriv ut summan av hela matrisen
"""

###############
## UPPGIFT 8 ##
###############

"""
Skriv ut summan av diagonalen från
övre vänstra hörnet, och summan av
diagonalen från övre högre hörnet.
"""


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
lägre vänstra hörnet. (2*2-(1*1))
"""


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
(1*2*6 + 2*5*2 + 3*4*1)-(2*2*3 + 1*5*1 + 6*4*2)
"""

################
## UPPGIFT 11 ##
################

"""
Räkna ut DETERMINANTEN av en 10x10-
matris. (antingen den från uppg 3
eller en som du gjort i uppg 4)

Determinanten från matrisen i uppgift
3 är 3028848.
"""
