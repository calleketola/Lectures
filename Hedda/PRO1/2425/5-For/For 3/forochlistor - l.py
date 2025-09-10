###############
## UPPGIFT 1 ##
###############
"""
Skriv ut talen 0.01, 0.02, 0.03 ... 0.99 1.00
med en for-loop, gör samma sak med en while-loop.
"""
"""
print("Uppgift 1")
# FOR:
print("Lösning med for-loop:")
for i in range(1,101):
    print(i/100)

# WHILE:
print("Lösning med while-loop:")
i = 0.00
while i < 1:
    i += 0.01
    print(i)
"""

###############
## Uppgift 2 ##
###############
"""
Skriv ut talen 0.02, 0.04, 0.06 ... 0.98, 1.00
med en for-loop, och sen en while-loop.
"""

print("Uppgift 2")
# FOR:
print("Lösning med for-loop:")

# WHILE:
print("Lösning med while-loop:")


###############
## UPPGIFT 3 ##
###############
"""
En aktie ökar i värde med 3 % varje år. Skriv ut
värdet på aktien för varje år tolv år framåt om
den idag har värdet 100 kr.
"""

print("Uppgift 3")

ökning = 1.03
värde = 100

for i in range(12):
    värde = värde*ökning
    print(värde)


###############
## UPPGIFT 4 ##
###############
"""
Skriv ett program som beräknar summan av 1/1+1/2+1/4+1/8...
fram tills den sista termen är mindre än 0.000001. Lös den
en gång med en for-loop och en gång med en while-loop.
"""

print("Uppgift 4")
# FOR:
print("Lösning med for-loop:")
värde = 0
for i in range(100000000):
    if 1/2**i < 0.000001:
        break
    värde += 1/2**i
print(värde)

# WHILE:
print("Lösning med while-loop:")

i = 0
värde = 0
while 1/2**i > 0.000001:
    värde += 1/2**i
    i += 1
print(värde)

###############
## UPPGIFT 5 ##
###############
"""
Gör samma som i fyra men med alternerande tecken, varannan
positiv och varannan negativ. 1/1-1/2+1/4-1/8...
"""

print("Uppgift 5")
# FOR:
print("Lösning med for-loop:")

# WHILE:
print("Lösning med while-loop:")

i = 0
värde = 0
while 1/2**i > 0.000000000001:
    värde += (1/2**i)*(-1)**i
    i += 1
print(värde)

###############
## UPPGIFT 6 ##
###############

"""
Skriv ut varje element i listan genom att
använda index och genom att använda x in listan
"""

roliga_siffror = [3,1,4,1,5,9,2,6,5,3,5,9]
# index:

for i in range(len(roliga_siffror)):
    print(roliga_siffror[i])

# tal in roliga_siffror:
for x in roliga_siffror:
    print(x)

###############
## UPPGIFT 7 ##
###############

"""
Gör samma sak igen!
"""

roliga_namn = [["Bilbo","Gandalf","Dwalin","Balin", "Kili", "Fili", "Dori", "Nori", "Ori", "Oin", "Gloin", "Bifur", "Bofur", "Bombur", "Thorin"], ["Frodo","Sam","Merry","Pippin","Gandalf","Aragorn","Boromir","Legolas","Gimli"]]

for i in range(len(roliga_namn)):
    for j in range(len(roliga_namn[i])):
        print(roliga_namn[i][j])

for x in roliga_namn:
    for y in x:
        print(y)

###############
## UPPGIFT 8 ##
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

treor = 0
for rad in rutnät:
    for tal in rad:
        if tal == 3:
            treor += 1

print("Antal treor:", treor)

#####################
## UPPGIFT Simhopp ##
#####################

"""
Fråga efter antalet domare = n
loopa n gånger
    Ta emot tal
    Addera till tidigare tal
    Kolla om störst
    Kolla om minst
Ta bort största värdet
Ta bort minsta värdet
Ta medelvärdet
Multiplicera med tre
"""

n = input("Antal domare: ")
n = int(n)

poäng = 0

störst = 0
minst = 0

for i in range(n):
    p = input(f"{i+1}) Poäng: ")
    p = int(p)
    if i == 0:
        störst = p
        minst = p
    else:
        if p > störst:
            störst = p
        elif p < minst:
            minst = p
    poäng += p

poäng -= (störst+minst)
medel = poäng/(n-2)
poäng = medel*3
print("Totalpoäng:", poäng)
