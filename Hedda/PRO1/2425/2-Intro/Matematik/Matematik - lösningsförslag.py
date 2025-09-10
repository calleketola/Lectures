# 1

# Justera programmet så att det tar emot två
# decimaltal och räknar ut medelvärdet av dem.

## Medelvärde: summan av alla tal delat på antalet tal

print("Uppgift 1")

tal1 = input("Skriv ett tal: ") 
tal2 = input("Skriv ett till tal: ")
tal1 = float(tal1)
tal2 = float(tal2)
summa = tal1+tal2   # Adderar talen
medel = summa/2
print("Medel av dessa tal är:", medel)

# 2
# Dela tal1 med tal2 och skriv ut svaret
print("Uppgift 2")

kvot = tal1/tal2
print("Kvoten är:", kvot)

# 3
# Ta medelvärdet (resultatet från uppg 1) höj
# upp det med kvoten (resultatet från uppg 2)
# medel**kvot
print("Uppgift 3")
potens = medel**kvot
print(medel,"^",kvot,"=",potens)

# 4
# Var dyker det första avrundningsfelet upp?
# När stämmer det plötsligt igen?
print("Uppgift 4")
tal = 0
a =0
while a < 10:
    tal += 0.1
    a += 1
    print(tal)

# 5
# Skriv ett program som konverterar ett heltal i
# bas 10 till bas 2
print("Uppgift 5")
tal_10 = input("Skriv ett tal: ")
tal_10 = int(tal_10)

tal_2 = ""

while tal_10>0:
    tal_2 = str(tal_10%2)+tal_2
    tal_10 = tal_10//2
tal_2 = int(tal_2)
print(tal_2)


# 6
# Använd funktionen omkrets och skriv kod som 
# tar emot en radie från användaren och skriver
# ut omkretsen
print("Uppgift 6")

import math

def omkrets(r):
    return 2*r*math.pi

radie = input("Radien? ")
radie = int(radie)
om = omkrets(radie)
print("Omkretsen är:", om)

# 7
# Skapa en funktion som tar emot ett heltal och
# returnerar resten när man delar med tre.

def uppg7(x):
    return x%3
print("Uppgift 7")
tal7 = input("Skriv ett tal: ")
svar = uppg7(int(tal7))
print("Resten blev", svar)

# 8
# Skapa en funktion som tar emot två tal och
# skriver ut resten när man delar första talet
# med det andra talet.

def uppg8(a,b):
    return a%b

print("Uppgift 8")

tal8a = input("Skriv ett tal: ")
tal8b = input("Skriv ett tal: ")
svar = uppg8(int(tal8a),int(tal8b))
print("Svar:", svar)
