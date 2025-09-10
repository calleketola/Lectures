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

print("Övning 1")

tal = []
tal.append(float(input("Skriv ett tal: ")))
tal.append(float(input("Skriv ett tal: ")))
tal.append(float(input("Skriv ett tal: ")))
tal.sort()
print(tal)

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

print("Övning 2")

tal = int(input("Antal: "))
numbers = []
for i in range(tal):
    numbers.append(float(input("Skriv ett tal: ")))
least = min(numbers)
print(least)

#Lösning på en rad

print(min([float(input("Skriv ett tal: ")) for i in range(int(input("Antal: ")))]))

###############
## ÖVNING 03 ##
###############

"""
Implementera följande pseudokod:

SET name to USER INPUT
SET first to first letter of name
PRINT "The first letter of the name is {first}"
"""

print("Övning 3")

name = input("Skriv namn: ")
first = name[0]
print(f"The first letter of the name is {first}")

###############
## ÖVNING 04 ##
###############

"""
Översätt följande kod till pseudokod
"""
def StalinSort(lista):
    i = 0
    while i < len(lista) -1:
        if lista[i] > lista[i+1]:
            lista[i+1].pop()
        else:
            i := i + 1
    return lista
def StalinSort(lista):
    i = 0
    while i < len(lista)-1:
        if lista[i] > lista[i+1]:
            lista.pop(i+1)
        else:
            i += 1
    return lista

"""
alternativ 1:

function StalinSort(lista : list):
    loop through every item in list
        if current item is larger than next item
            remove next item
        else
            go to next item
    return list

alternativ 2:

FUNCTION StalinSort
GET lista
SET i to 0
WHILE i LESS THAN length of lista minus 1
    IF lista at position i GREATER THAN lista at position i plus 1
        REMOVE item at position i + 1
    END IF
    ELSE
        SET i to i + 1
    END ELSE
END WHILE
RETURN lista


Alternativ 3:
function StalinSort(lista)
    i := 0
    while i < length lista -1
        if lista[i] > lista[i+1]
            remove lista[i+1]
        else
            i := i + 1
    return lista

"""

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
kontinuerlig första derivata.
"""
def f(x):
    return x**2-10*x-20

def derive(f,x):
    h = 2**(-10)
    return (f(x+h)-f(x))/h

def Newton_Raphson(f, start):
    error = 2**(-10)
    x = start
    limit = 2**10
    i = 0
    while abs(f(x)) > error and i < limit:
        y = f(x)
        dy = derive(f,x)
        x = x - y/dy
        i += 1
    return x

x = float(input())
root = Newton_Raphson(f,x)
print(root)


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

"""
IMPORT library random

SET LIST score_table TO ["", "", "", "", "", ""]
SET LIST dice TO [0,0,0,0,0]

SET turn TO 0
WHILE turn LESS THAN length of score_table
    SET rethrow TO "12345"
    SET throw TO 0
    WHILE throw LESS THAN 3
        FOR every number in rethrow
            SET dice position number TO random number between 1 and 6
        END FOR
        PRINT list dice
        IF throw LESS THAN 2
            PRINT "Which dice do you want to rethrow?"
            SET rethrow TO INPUT
            REMOVE "," FROM rethrow
            REMOVE " " FROM rethrow
        END IF
        ADD 1 TO throw
    END WHILE
    SET ask TO True
    WHILE ask IS True
        PRINT "Set to which score?"
        SET answer TO INPUT
        IF score_table position answer-1 IS EMPTY
            SET ask TO False
        END IF
        ELSE
            PRINT "Already taken"
        END ELSE
    SET score_table position answer-1 TO answer TIMES number of answer in dice
    PRINT score_table
    ADD 1 to turn
END WHILE
PRINT sum of score_table
"""
