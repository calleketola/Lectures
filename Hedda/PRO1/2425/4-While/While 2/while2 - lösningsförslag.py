from turtle import *

speed(0)

###############
## UPPGIFT 1 ##
###############

"""
Rita en kvadrat
"""
i = 0
while i < 4:
    fd(100)
    rt(90)
    i += 1

###############
## UPPGIFT 2 ##
###############

"""
Rita en sexhörning
"""

hörn = 0
while hörn < 6:
    fd(100)
    lt(60)
    hörn += 1

###############
## UPPGIFT 3 ##
###############

"""
Rita fem sexhörningar på rad
"""

figurer = 0
while figurer < 5:
    hörn = 0
    while hörn < 6:
        fd(20)
        lt(60)
        hörn += 1
    fd(50)
    figurer += 1
    
###############
## UPPGIFT 4 ##
###############

"""
Rita ut femuddiga stjärnor i varje
hörn på sexhörningarna.
"""

figurer = 0
while figurer < 5:
    hörn = 0
    while hörn < 6:
        fd(50)
        lt(60)
        hörn += 1
        uddar = 0
        while uddar < 5:
            fd(20)
            rt(180-180/5)
            uddar += 1
    fd(50)
    figurer += 1

###############
## UPPGIFT 5 ##
###############

"""
Utgå från Fibbonacci-serien och
rita en spiral.
"""

setpos((0,0))
a = 1
b = 1
i = 0
while i < 25:
    fd(a/100)
    rt(90)
    
    c = a
    a += b
    b = c
    
    i += 1

###############
## UPPGIFT 6 ##
###############

"""
Skriv ut alla primtal upp till 1000.
"""

i = 2 # Första möjliga primtalet
while i < 100: # Tusen va tråkigt att vänta ut ():)
    prim = True # Antag att det är ett primtal
    j = 2 
    while j <= i**.5: # Detta är en optimering, vi behöver inte kolla större tal än så
        if i%j == 0: # Om det gick att dela
            prim = False # Inget primtal
            break # Bryt loopen
        j += 1
    if prim: # Så länge vi inte brutit loopen händer detta
        print(i, "är ett primtal")
    i += 1 # Kolla nästa tal

###############
## UPPGIFT 7 ##
###############

"""
I bordsrollspelet Eon kastar man flera
sexsidiga tärningar för att se om en
handling lyckas. Varje gång man slår en
sexa så plockar man bort den tärningen
och kastar två nya. Skulle någon av de
nya tärningarna visa en sexa så upprepar
man proceduren. Skriv ett program som
frågar efter hur många tärningar
användaren vill kasta och som sen kastar
tärningarna, enligt reglerna ovan, och
räknar ut det totala resultatet.
"""
import random

antal = input("Hur många tärningar vill du kasta? ")
antal = int(antal)

summa = 0
kastade = 0

sexor = 0

while kastade < antal:
    tal = random.randint(1,6) # Slumpar ett tal
    print("Du slog en", tal) # Detta är för att visa att det fungerar
    if tal == 6:
        antal += 1 # Istället för två nya tärningar, lägger jag till en tärning och kastar om den gamla
        sexor += 1 # Den här är bara för att kontrollera att det blir rätt
        continue # Nu hoppar jag direkt till toppen av loopen, så ingen summering, och vi ägger itne heller på antal kastade
    summa += tal # Lägger ihop talen
    kastade += 1 # Ökar antalet vi kastat

print("Du slog totalt", summa, "({} sexor, {} tärningar totalt)".format(sexor, antal)) # Format har vi inte pratat om, men det kommer senare

###############
## UPPGIFT 8 ##
###############

"""
För att hitta nollstället till en funktion
kan man använda sig utav derivatan. Om
funktionens värde i ett \(x\) är positivt
och derivatan i den punkten är negativ så
vet du att du antingen har ett nollställe
eller en extrempunkt till höger. På samma
sätt, om derivatan är positivt så finns
nollstället eller extrempunkten till
vänster. Motsvarande resonemang kan användas
för negativa värden på funktionen.
Implementera Eulers metod för att hitta ett
nollställe till funktionen
y=f(x)=0.125 x^4-0.5 x^3+2 x^2-2 x^1-5
		
Formeln för derivatan är:
lim h->0 (f(x+h)-f(x))/h
"""
def df(f, x, h=2**-10):
    """
    f: en matematisk funktion
    x: float
    h: float
    """
    return (f(x+h)-f(x))/h

def f(x):
    return 0.125*x**4-0.5*x**3+2*x**2-2*x-5

# Beroende på vilket startvärde man väljer får man olika resultat

start = float(input("Startvärde: "))
error = 2**(-5) # Hur nära noll vi ska vara för att känna oss nöjda

x = start
step = 2**-7
y = f(x)
while abs(y) > error:
    dydx = df(f,x)
    y = f(x)
    #print(f"x={x} y={y} f'={dydx}")
    if dydx > 0 and y > 0:
        x -= step
    elif dydx < 0 and y > 0:
        x += step
    elif dydx < 0 and y < 0:
        x -= step
    elif dydx > 0 and y < 0:
        x += step
    elif abs(dydx) < error:
        print("Extrempunkt", x, y)
        break
else:
    print("Nollställe:", x, y)

###############
## UPPGIFT 9 ##
###############

"""
Hitta funktionens minsta värde
"""

# Detta går att lösa med samma metod som
# ovan, men man får göra lite små ändringar.
# Nu vill vi veta när derivatan är noll.
# Så om derivatan är positiv ska vi gå till
# vänster och om derivatan är negativ ska vi
# gå till höger, oavsett y-värdet. Vi kommer
# också behöva ändra vårt villkor i loopen.

start = float(input("Startvärde: "))
error = 2**(-5) # Hur nära noll vi ska vara för att känna oss nöjda

x = start
step = 2**-7
y = f(x)
dydx = df(f,x)
while abs(dydx) > error:
    dydx = df(f,x)
    #print(f"x={x} y={y} f'={dydx}")
    if dydx > 0:
        x -= step
    else:
        x += step
else:
    print("Extrempunkt:", x, f(x))
