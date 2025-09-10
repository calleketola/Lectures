# Ett program som tar emot data och gör saker beroende på vad det är

###############
## UPPGIFT 1 ##
###############

variabel1 = input("Skriv något:\n")
variabel2 = input("Skriv något mer:\n")

if len(variabel1) > len(variabel2):
    print(variabel1, "är längre än", variabel2)
elif len(variabel1) == len(variabel2):
    print(variabel1, "och", variabel2, "är lika långa.")
else:
    print(variabel2, 'är längre än', variabel1)

###############
## UPPGIFT 2 ##
###############

tid = input("Hur många år bakåt i tiden vill du resa?")
tid = int(tid)

if tid < 16:
    print("Montenegro är självständigt")
elif tid < 106:
    print("Nu är Finland självständigt")
elif tid < 126:
    print("Kuba är ett eget land")
elif tid < 257:
    print("Thailand fanns då")
elif tid < 1054:
    print("Då existerade Sverige")
elif tid < 1059:
    print("Danmark hade formats då")
elif tid < 1124:
    print("Då hade du kunnat besöka landet Etiopien")
elif tid < 3624:
    print("Man kan mena att Kina att skapats då")
elif tid < 4500:
    print("Då fanns Indien")
elif tid < 4600:
    print("Iran fanns för så många år sedan")
else:
    print("Inga länder du besöker kommer att finnas 2024")

###############
## UPPGIFT 3 ##
###############

svar = input("Skriv ett ord: ")

if svar == svar.lower():
    print(svar, "innehåller bara små bokstäver.")
elif svar == svar.upper():
    print(svar, "innehåller bara stora bokstäver.")
elif svar == svar.title():
    print(svar, "börjar på en stor bokstav.")
else:
    print(svar, "innehåller blandade stora och små bokstäver.")

###############
## UPPGIFT 4 ##
###############

årtal = input("Skriv ett årtal: ")
årtal = int(årtal) # Gör om det till ett tal.
skottår = False

if årtal%4==0: # året är jämnt delbart med fyra
    skottår = True # Kan vara ett skottår
    if årtal%100==0: # året är jämnt delbart med hundra
        if årtal%400==0: # Året är jämnt delbart med 400
            skottår = True
        else: # Delbart med hundra, men inte fyrahundra
            skottår = False

if skottår == True:
    print("Året", årtal, "är ett skottår.")
else:
    print("Året", årtal, "är ett normalår.")

if årtal%400 == 0:
    print("Året", årtal, "är ett skottår.")
elif årtal%100 == 0:
    print("Året", årtal, "är ett normalår.")
elif årtal%4 == 0:
    print("Året", årtal, "är ett skottår.")
else:
    print("Året", årtal, "är ett normalår.")
    

###############
## UPPGIFT 5 ##
###############

tid = input("Hur många minuter kommer du att prata? ")
tid = int(tid)

if tid < 33:
    print("Ta Kontant")
elif tid < 36:
    print("Ta normal")
else:
    print("Ta Plus")

###############
## UPPGIFT 6 ##
###############

import math

a = input("Längden på a: ")
b = input("Längden på b: ")
v = input("Vinkel mellan a & b: ")

a, b, v = float(a), float(b), float(v)

v = math.pi*v/180 # Konverterar till radianer

c = math.sqrt(a*a+b*b-a*b*math.cos(v))
c = round(c,2)
print("a: {}, b: {}, c: {}".format(a,b,c))
if a == b and b == c:
    print("Det är en liksidig triangel")
elif a == b or a == c or b == c:
    print("Det är en likbent triangel")
else:
    print("Det är en oliksidig triangel")

