##############
## ÖVNING 1 ##
##############

"""
En sjö har en area på 1000 m2. I ett hörn av sjön ligger alger med en
utbredning på 13 m2. Varje vecka växer algerna och täcker 27 m^2 mer av sjön.
Efter hur många veckor är sjön täckt med alger?
"""

sjöarea = 1000
algarea = 13

veckor = 0

while algarea < sjöarea:
    algarea += 27
    veckor += 1

print("Det tar", veckor, "veckor att täcka sjön med alger")

##############
## ÖVNING 2 ##
##############

"""
Grannsjön, som är 1337 m^2 stor, är redan täckt med alger. Därför har man
hällt i Algdödarmedel X i sjön. Varje vecka minskar ytan algerna täcker med 3
%. Efter hur många veckor har hälften av algerna försvunnit?
"""

sjöarea = 1337
algarea = sjöarea

veckor = 0

förändring = 0.97

while algarea > sjöarea/2:
    algarea *= förändring
    veckor += 1
print("Det tar", veckor, "veckor att halvera algerna")

##############
## ÖVNING 3 ##
##############

"""
Skriv ett program som tar emot ett tal n och räknar ut följande summa:
1 + 4 + 9 + 16 + ... + n^2
"""

n = input("Hur många termer? ")
n = int(n)
i = 1
summa = 0
while i < n:
    summa += i**2
    i += 1
print(summa)

##############
## ÖVNING 4 ##
##############

"""
Räkna nu ut följande summa istället:
1/1 + 1/2 + 1/4 + 1/8 + ... +  1/2^n
"""

summa = 0
i = 0
while i < n:
    summa += 1/2**i
    i += 1
print(summa)



##############
## ÖVNING 5 ##
##############

"""
I rollspelet Dungeons and Dragons rullar man en 20-sidig tärning för att se om
man lyckas med något. Utöver vad tärningen visar tar man plus sin bonus
(som kan vara negativ) och lägger till det på tärningsresultatet. Skriv ett
program som rullar en 20-sidig tärning och frågar efter din bonus (oftast ett
tal mellan -2 och +20) och sen frågar efter svårigheten att lyckas. Om
tärningen plus bonusen blir högre eller lika med svårigheten har man lyckats.
"""

import random

# Onödigt komplicerad one line:er
print((random.randint(1,20) + int(input("Bonus: "))) >= int(input("Svårighet: ")))

# Längre enklare sätt
die = random.randint(1,20)
bonus = int(input("Bonus: "))
diff = int(input("Difficulty: "))

if die + bonus >= diff:
    print("Success!")
else:
    print("Failure!")

##############
## ÖVNING 6 ##
##############

"""
I rollspelet Eon så kastade man istället era sexsidiga tärningar och räknade
ihop resultatet, men den regeln att om man slog en sexa så slog man om den
tärningen och kastade en till. Testa att kasta skitmånga tärningar. Vad blir
medelvärdet för en tärning? (Räkna med att totalen är lika med antalet
tärningar du kastade från början).
"""

summa = 0
start_antal = 1000000
antal = start_antal
kastade = 0
while kastade < antal:
    kastade += 1
    tärning = random.randint(1,6)
    if tärning == 6:
        antal += 2
        continue
    summa += tärning
print(summa/start_antal)

##############
## ÖVNING 7 ##
##############

"""
I rollspelen Svärdets sång, Mutant år noll m.fl. så rullar man precis som i Eon
flera sexsidiga tärningar (oftast mellan 2 och 15 stycken) för att se om man
lyckas. Tillskillnad från Eon så räknar man bara antalet sexor. Skriv ett
program som rullar n tärningar och skriver ut hur många sexor man får.
"""

n = input("Antal tärningar: ")
n = int(n)

sexor = 0
i = 0
while i < n:
    resultat = random.randint(1,6)
    if resultat == 6:
        sexor += 1
    i += 1
print("Du rullade totalt", sexor, "sexor")

##############
## ÖVNING 8 ##
##############

"""
Skriv ett program som tar a delat med b och försöker hitta en approximation
på π genom att uppdatera a och b så att du kommer närmare och närmare π.
Skriv sen ut dierensen mellan π och ditt bråk.
"""

import math

a = 1
b = 1

E = 2**(-10)

while abs(a/b-math.pi) > E:
    if a/b - math.pi > 0:
        b += 1
    else:
        a += 1
    print(a/b)
print(a,b,a/b)

##############
## ÖVNING 9 ##
##############

"""
I Dungeons and Dragons så får man ibland rulla två 20-sidiga tärningar och
välja den tärning som slog högst. Rulla två 20-sidiga tärningar
1 000 000 gånger. Vad är medelvärdet för den bästa tärningen i varje kast?
"""

n = 1000000
rullade = 0
summa = 0
while rullade < n:
    t1 = random.randint(1,20)
    t2 = random.randint(1,20)
    if t1 > t2:
        summa += t1
    else:
        summa += t2
    rullade += 1
medel = summa/n
print("Medelvärdet är: ", medel)

###############
## ÖVNING 10 ##
###############

"""
Gör samma experiment igen men välj den sämre tärningen.
"""
n = 1000000
rullade = 0
summa = 0
while rullade < n:
    t1 = random.randint(1,20)
    t2 = random.randint(1,20)
    if t1 < t2:
        summa += t1
    else:
        summa += t2
    rullade += 1
medel = summa/n
print("Medelvärdet är: ", medel)
