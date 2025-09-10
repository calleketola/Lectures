###############
## ÖVNING 01 ##
###############

"""
Implementera följande pseudokod:

Skapa en tom lista
Lägg till ett tal i listan
Lägg till ett tal i listan
Lägg till ett tal i listan
Sortera listan # Det finns ett kommando för detta
Skriv ut listan
"""

###############
## ÖVNING 02 ##
###############

"""
Implementera följande pseudokod:

int n <- input
numbers <- []
for i = 0 to n:
    numbers append float input
least <- min(numbers)
print least
"""

###############
## ÖVNING 03 ##
###############

"""
Implementera följande pseudokod:

SET name to USER INPUT
SET first to first letter of name
PRINT "The first letter of the name is {first}"
"""

###############
## ÖVNING 04 ##
###############

"""
Översätt följande kod till pseudokod
"""

def StalinSort(lista):
    i = 0
    while i < len(lista)-1:
        if lista[i] > lista[i+1]:
            lista.pop(i+1)
        else:
            i += 1
    return lista



###############
## ÖVNING 05 ##
###############

"""
Implementera följande pseudokod:

FUNCTION f(x)
    RETURN x^2-10x-20

FUNCTION derive(f, x)
    SET h = 2^(-10)
    RETURN (f(x+h)-f(x))/h

FUNCTION Newton_Raphson(f, start)
    SET error TO 2^(-10)
    SET x TO start
    SET limit TO 2^10
    SET i TO 0
    WHILE |f(x)| GREATER THAN error AND i LESS THAN limit:
        SET y TO f(x)
        SET dy TO derive(f,x)
        x = x - y/dy
        SET i TO i+1
    END WHILE
    RETURN x

SET x TO INPUT

SET root TO Newton_Raphson(f, x)
PRINT root

Detta är en version av Newton-Raphsons metod för att hitta
rötter till en funktion förutsatt att funktionen har en
kontinuerlig förstaderivata.
"""



###############
## ÖVNING 06 ##
###############

"""
Översätt Yatzy-koden nedanför till pseudokod
"""

import random

score_table = ["","","","","",""]
dice = [0,0,0,0,0]

for turn in range(len(score_table)):
    rethrow = "12345"
    for throw in range(3):
        for die in rethrow:
            dice[int(die)-1] = random.randint(1,6)
        print(dice)
        if throw < 2:
            print("Which dice do you want to rethrow?")
            rethrow = input()
            rethrow = rethrow.replace(",", "")
            rethrow = rethrow.replace(" ", "")
    ask = True
    while ask == True:
        print("Set to which score?")
        answer = int(input())
        if score_table[answer-1] == "":
            ask = False
        else:
            print("Already taken")
    score_table[answer-1] = answer*dice.count(answer)
    print(score_table)
print(sum(score_table))
