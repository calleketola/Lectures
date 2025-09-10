##############
## ÖVNING 1 ##
##############

"""
Ta emot en textsträng och kolla om
den bara består av stora eller små
bokstäver.
"""

text = input("Skriv något ")

if text == text.lower():
    print(text, "innehåller bara små bokstäver")
elif text == text.upper():
    print(text, "innehåller bara stora bokstäver")
    


##############
## ÖVNING 2 ##
##############

"""
Skriv ett program som frågar efter
ett tal och fortsätter att fråga tills
användaren bara svarat med siffror.
"""
svar = "qwerty"
while svar.isnumeric() == False:
    svar = input("Skriv ett tal ")
print("Du skrev talet", svar)

##############
## ÖVNING 3 ##
##############

"""
Skriv ett program som frågar efter
hur många kg lösgodis användaren vill
köpa och sen skriver ut ett fint kvitto.

Pris: 89.90 kr/kg
 ____________________________________
|                                    |
|       Tjommens godisaffär          |
|                                    |
|Lösgodis 1.25 kg á 89.90 tot 112.38 |
|____________________________________|
"""

print("Köp godis! Pris 89.90 kr/kg")
kg = input("Hur många kilo vill du köpa? ")
kg = float(kg)
pris = 89.90
betala = round(kg*pris,2)

tal = str(kg)+str(pris)+str(betala)
siffror = len(tal)
tomrum = 15-siffror

print(" ____________________________________")
print("|                                    |")
print("|       Tjommens godisaffär          |")
print("|Lösgodis", kg, "kg á", pris, "tot", betala, " "*tomrum+"|")
print("|____________________________________|")

##############
## ÖVNING 4 ##
##############

"""
Skriv ett program som skriver ut alla
udda tal mellan 151 och 260
"""

for i in range(151,260,2):
    print(i)

##############
## ÖVNING 5 ##
##############

"""
Skriv ett program som tar emot ett tal
och kollar om det är ett av Fibonacci-
talen.
"""

tal = input("Skriv ett heltal: ")
tal = int(tal)
a = 1
b = 1
while tal >= a:
    if tal == a:
        print("Jupps")
        break
    c = a
    a = a+b
    b = c
else:
    print("Nope")


##############
## ÖVNING 6 ##
##############

"""
Skriv ett program som tar emot en text
och skriver ut hur många tecken den
innehåller.
"""

print(len(input("Skriv något ")), "tecken")

##############
## ÖVNING 7 ##
##############

"""
Skriv ett program som tar emot n tal och
skriver ut produkten av de n talen.
"""
n = input("Antal tal: ")
n = int(n)
prod = 1
for i in range(n):
    tal = input(f"Tal {i+1}: ")
    prod *= float(tal)
print(prod)

##############
## ÖVNING 8 ##
##############

"""
Skriv ett program som tar emot n tal och
skriver ut medelvärdet av talen.
"""
n = input("Antal tal: ")
n = int(n)
summa = 0
for i in range(n):
    tal = input(f"Tal {i+1}: ")
    summa += float(tal)
print(summa/n)
##############
## ÖVNING 9 ##
##############

"""
Skriv ett program som tar emot n tal och
skriver ut vilket tal som är störst
"""
störst = 0
n = input("Antal tal: ")
n = int(n)
for i in range(n):
    tal = input(f"Tal {i+1}: ")
    tal = float(tal)
    if i == 0:
        störst = tal
    elif tal > störst:
        störst = tal
print("störst", störst)
###############
## ÖVNING 10 ##
###############

"""
Skriv ett program som tar emot n tal och
skriver ut vilket tal som är minst
"""
minst = 0
n = input("Antal tal: ")
n = int(n)
for i in range(n):
    tal = input(f"Tal {i+1}: ")
    tal = float(tal)
    if i == 0:
        minst = tal
    elif tal < minst:
        minst = tal
print("minst", minst)
