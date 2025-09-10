##############
## Övning 1 ##
##############

"""
Koden här nedanför skriver ut
talen 1 - 5 två gånger. Justera
i koden så att den gör det fyra
gånger istället. 
"""
print("Övning 1+2")
for i in range(2):
    for j in range(1,6):
        print(j)

##############
## Övning 2 ##
##############

"""
Från din lösning till uppgift 1,
justera så att den skriver ut
talen 3 - 9 istället.
"""

##############
## Övning 3 ##
##############

"""
Koden här nedanför skriver ut
tvåans gånger tabell. Justera
i koden så att den skriver ut
2:an till 5:ans gångertabell.
"""
print("Övning 3")
for i in range(1,11):
    print(f"{i}*{2}={i*2};", end=" ")
print()

##############
## Övning 4 ##
##############

"""
Koden här nedanför tar emot
tre tal och multiplicerar
dem. Justera koden så att
den först frågar om hur
många tal man vill ange.
"""

print("Övning 4+5")

produkt = 1

for i in range(3):
    tal = float(input(f"Tal {i+1}: "))
    produkt *= tal
print(f"Produkten av dina tal är: {produkt}")

##############
## Övning 5 ##
##############

"""
I din lösning till uppgiften
ovan, ändra i koden så att
den ÄVEN räknar ut summan av
alla tal.
"""

##############
## Övning 6 ##
##############

"""
Följande uppgift är saxad från
kursboken, Python från början:

En kommun har gjort följande
prognos för befolkningsutvecklingen
de närmaste åren:

* Vid början av 2022 hade
  kommunen 26 000 invånare
* Antalet födda och avlidna
  under ett år uppskattas
  vara 0,7 % respektive
  0,6 % av befolkningen vid
  årets början.
* Antalet inflyttade och
  antalet utflyttade uppskattas
  till 300 respektive 325
  varje år.

Skriv ett program som beräknar
kommunens uppskattade invånarantal
i början av ett visst år. Vilket
år det gäller ska läsas som
indata till programmet.
"""

print("Övning 6")

##############
## Övning 7 ##
##############

import random

"""
Skriv ett program som skriver ut
talen 0 upp till ett slumpat tal
under 25.

Kommandot för att slumpa ett heltal
med biblioteket random är:
tal = random.randint(start, stop)
Notera att värdet stop kommer med
"""
print("Övning 7+8")


##############
## Övning 8 ##
##############

"""
Justera din lösning från övning 7
Så att den skriver ut 0 - stop ett
slumpvis antal gånger, och slumpa om
sluttalet varje gång.
"""



##############
## Övning 9 ##
##############

"""
När du vill spara flera olika
värden samtidigt kan du använda
sig utav listor.

För att skapa en lista med talen
5 till 9 kan du antingen skriva:

flera_tal = [5,6,7,8,9]

eller

flera_tal = [] # Skapar en tom lista
flera_tal.append(5) # Lägger till 5 sist
flera_tal.append(6) # Lägger till 6 sist
flera_tal.append(7) # Lägger till 7 sist
flera_tal.append(8) # Lägger till 8 sist
flera_tal.append(9) # Lägger till 9 sist

Om du vill skriva ut talen
var för sig behöver du skriva:

print(flera_tal[0]) # Skriver ut 5
print(flera_tal[1]) # Skriver ut 6
print(flera_tal[2]) # Skriver ut 7
print(flera_tal[3]) # Skriver ut 8
print(flera_tal[4]) # Skriver ut 9

Skapa listan flera_tal själv,
och lägg till talen på sätt 2.
Men använd en loop istället för
att skriva 5 rader.

Skriv sedan ut alla talen var
för sig, också det med en loop.
"""


###############
## Övning 10 ##
###############

"""
Om du vill ändra på ett tal
i en lista så behöver du titta
på rätt plats i listan.

flera_tal = [5,6,7,8,9]

Observera listan flera_tal.
För att komma åt 5:an skriver
du:

flera_tal[0] # Notera att vi räknar från noll och jämför med range()

Och vill du komma åt 6:an
skriver du:

flera_tal[1] # Tal 1 är alltså den andra platsen

och så vidare. Vill du ändra
på ett tal skriver du då:

flera_tal[1] = 10

Nu ser listan ut så här:

[5,10,7,8,9]

Ändra i listan flera_tal från
förra övningen så att 7:an
istället är en 12:a. Skriv sedan
ut alla talen igen.
"""



###############
## Övning 11 ##
###############

"""
Nu kommer svårighetsgraden
att stegras ganska så snabbt,
mycket snabbare än när vi
faktiskt når till listor i
kursen.

Skapa listan jämna_tal som
innehåller talen:

0 2 4 ... 98

och skriv ut den, tal för tal,
på en och samma rad (det kommer
att ske radbrytningarpå grund av
fönsterstorleken, men det är okej)
"""


###############
## Övning 12 ##
###############

"""
Från din lista jämna_tal
multiplicera och spara om
var tredje tal med -1.

Listan ska alltså se ut typ:

[0 2 4 -6 8 10 -12 14 16 -18 ...]

Skriv sen ut summan av alla
tal i listan.
"""


###############
## Övning 13 ##
###############

"""
Ta emot 5 tal från användaren
och spara dessa i en lista.
Skriv ut det största och minsta
av talen.

Här finns det två sätt att lösa
uppgiften. Det ena med de två
inbyggda kommandona max() och
min(). Det andra är en egen-
skriven kontroll med if-satser
och loopar. Försök att lösa det
på båda sätten.
"""



###############
## Övning 14 ##
###############

"""
Nu hoppar vi abrupt upp till
listor i listor.

Du kan ha listor i en lista.

listor = [[5,6,7],[4,3,2]]

Då kommer du åt en hel
underlista med:

listor[0] # [5,6,7]
listor[1] # [4,3,2]

Och du kan komma åt enskilda
tal med:

listor[0][0] # 5
listor[0][1] # 6
listor[0][2] # 7

listor[1][0] # 4
listor[1][1] # 3
listor[1][2] # 2

Skriv ut varje tal för sig ur
listan listor som skapas här
nedanför. Du kommer att
behöva använda nästade loopar.
"""
listor = [[6,8,2,1],
          [4,2,1,8],
          [6,6,3,2],
          [8,0,3,2]]



###############
## Övning 15 ##
###############

"""
Skapa en lista som
innehåller tre andra
listor som alla
innehåller talen:
[3,4,5,6,7,8]
"""


###############
## Övning 16 ##
###############

"""
Skapa följande lista
med hjälp av loopar:

[
 [0,1,2,3,4],
 [0,2,4,6,8],
 [0,3,6,9,12],
 [0,4,8,12,16],
 [0,5,10,15,20],
 [0,6,12,18,24,30]
]
"""





