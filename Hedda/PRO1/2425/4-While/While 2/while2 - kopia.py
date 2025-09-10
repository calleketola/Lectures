from turtle import *

###############
## UPPGIFT 1 ##
###############

"""
Rita en kvadrat
"""

###############
## UPPGIFT 2 ##
###############

"""
Rita en sexhörning
"""

###############
## UPPGIFT 3 ##
###############

"""
Rita fem sexhörningar på rad
"""

###############
## UPPGIFT 4 ##
###############

"""
Rita ut femuddiga stjärnor i varje
hörn på sexhörningarna.
"""

###############
## UPPGIFT 5 ##
###############

"""
Utgå från Fibbonacci-serien och
rita en spiral.
"""

###############
## UPPGIFT 6 ##
###############

"""
Skriv ut alla primtal upp till 1000.
"""

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

tal = random.randint(1,6)

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

###############
## UPPGIFT 9 ##
###############

"""
Hitta funktionens minsta värde
"""
