import random

###############
## UPPGIFT 1 ##
###############

"""
Skapa en lista som innehåller alla heltal
från 0 till och med 12
"""

uppg_1 = [] # Skapa en tom lista
for i in range(13): # Loopa 0 - 12
    uppg_1.append(i) # Lägg till i


###############
## UPPGIFT 2 ##
###############

"""
Multiplicera alla talen med 2 och spara de
nya värdena istället.

([0,1,2,...] -> [0,2,4,...])
"""

for i in range(len(uppg_1)): # Loopa igenom listan
    uppg_1[i] *= 2 # Multiplicera alla med 2

###############
## UPPGIFT 3 ##
###############

"""
Plocka bort talet 12 ur listan
"""

uppg_1.remove(12) # Här hade vi kunnat använda pop också.


###############
## UPPGIFT 4 ##
###############

"""
Lägg till talen: 3, 5, 7, 11, 13 och 17 i listan
"""

for i in range(3,18,2):
    if i == 9 or i == 15:
        continue
    uppg_1.append(i)

###############
## UPPGIFT 5 ##
###############

"""
Skriv det största och minsta värdena ur listan.
Tips: undersök funktionerna max() och min()
"""

print("Uppgift 5")

uppgift_5 = []

for i in range(15):
    uppgift_5.append(random.randint(1,10))

print(uppgift_5) # Skriv ut så vi ser att det blir rätt
print(max(uppgift_5), min(uppgift_5))

###############
## UPPGIFT 6 ##
###############

"""
Bestäm medelvärdet av talen i listan 
"""

print("Uppgift 6")
summa = 0
for i in range(len(uppgift_5)):
    summa += uppgift_5[i] # Addera alla
medel = summa/len(uppgift_5)
print(medel)
# Det finns fler sätt:
#summa = sum(uppgift_5)
# Eller:
#summa = 0
#for tal in uppgift_5
#    summa += tal


###############
## UPPGIFT 7 ##
###############

"""
Hitta medianen av talen i listan
"""
print("Uppgift 7")
# Nu måste vi först sortera listan
uppgift_5.sort()
print(uppgift_5)
# Medianen är det mittersta talet
print(uppgift_5[len(uppgift_5)//2]) # // Är heltalsdivision

###############
## UPPGIFT 8 ##
###############

"""
Bestäm typvärdet i listan (vanligast förekommande tal)

Tips: undersök funktionen count()
"""

print("Uppgift 8")
# Här finns det ett fett mycket smidigare sätt med
# dictionaries
antal = []
for i in range(len(uppgift_5)):
    tal = uppgift_5[i]
    antal.append(uppgift_5.count(tal))
print(uppgift_5)
print(antal) # Kollar så vi räknat rätt

for i in range(len(uppgift_5)): # Gå igenom
    if antal[i] == max(antal): # Kolla, är detta den vanligaste?
        print(uppgift_5[i])
        break
# Den här lösningen hanterar inte om det finns flera det är mest av

antal_2 = {}
for tal in uppgift_5:
    if tal not in antal_2:
        antal_2[tal] = 1
    else:
        antal_2[tal] += 1
print(max(antal_2, key = antal_2.get))

###############
## UPPGIFT 9 ##
###############

"""
I spel som Dungeons and Dragons så kan man bestämma
karaktärers förmågor med tärningsslag, där högre är
bättre. I gamla utgåvor så rullade man tre tärningar
och summerade dem. I nyare utgåvor så rullar man
fyra tärningar och summerar de tre bästa.

Skriv en kod som slumpar fyra tal mellan 1 och 6 och
stryker det sämsta.
"""

print("Uppgift 9")

tärningar = []
# Här slumpar vi fyra tal
for i in range(4):
    tärningar.append(random.randint(1,6))
# Sortera listan
tärningar.sort()
print(tärningar)
# Ta bort den lägsta som är först
tärningar.pop(0)

res = sum(tärningar)
print(tärningar)
print(res)


################
## UPPGIFT 10 ##
################

"""
Karaktärer får en bonus på handlingar relaterade till
en förmåga enligt följande tabell:

20   : +5
18-19: +4
16-17: +3
14-15: +2
12-13: +1
10-11: +0
 8-9 : -1
 6-7 : -2
 4-5 : -3
 2-3 : -4
 0-1 : -5

Eller enligt följande formel:

f(x)=floor(x/2)-5 , floor betyder avrundat nedåt

Vilket i Python blir:

f(x)=x//2-5

För att avgöra om man lyckas med en handling så
rullar man en 20-sidig tärning, lägger till sin
bonus och jämför det mot ett målvärde. Blir
resultatet lika eller högre än målet har du
lyckats med handlingen.

Rulla en tärning med 20 sidor. Lägg till bonusen.
Klarar din karaktär av en handlingen om måltalet
är 15?
"""

print("Uppgift 10")

# Vi återanvänder res från förra övningen
bonus = res//2-5
tärning = random.randint(1,20)
print("Du rullade:", tärning, end=". ")
if tärning + bonus >= 15:
    print("Du lyckades!")
else:
    print("Du misslyckades!")


################
## UPPGIFT 11 ##
################

"""
Lägg till att programmet frågar efter talet du
behöver nå för att klara en handling.
"""

målvärde = input("Vad är svårighetsgraden? ")
målvärde = int(målvärde)

bonus = res//2-5
tärning = random.randint(1,20)
print("Du rullade:", tärning, end=". ")
if tärning + bonus >= målvärde:
    print("Du lyckades!")
else:
    print("Du misslyckades!")
################
## UPPGIFT 12 ##
################

"""
Varje karaktär har sex stycken grundegenskaper:
1. Styrka
2. Smidighet
3. Uthållighet
4. Intelligens
5. Vishet
6. Karisma
Så försöker man övertala någon använder man
bonusen från karisma, o.s.v.

Slumpa fram värdet till varje egenskap enligt
modellen ovan och räkna ut deras bonusar.
Sen ska programmet fråga vilken egenskap som
ska användas vid en handling och vad målet är.
Sen ska det slumpa ett tal mellan 1 och 20,
lägga på bonusen och avgöra om du klarar det.
"""

# Lösning listor
grund_12 = []


################
## UPPGIFT 13 ##
################

"""
Det finns andra bordsrollspel som använder
andra system. Exempelvis Mutant: år noll.
I Mutant: år noll så rullar man flera sex-
sidiga tärningar och räknar ihop antalet
sexor. Antalet tärningar man rullar är ens
grundegenskap + färdighetsvärde + prylbonus.
Så vill du övertala någon att släppa in dig
i ett rum så tar du ditt värde i karisma plus
ditt värde i manipulera plus din prylbonus
för att du har en cool keps. Sen räknar du
hur många sexor du slog, ju fler desto bättre.

En speciell sak i Mutant: år noll är att det
är viktigt att hålla koll på källan till
varje tärning. Man vill alltså veta om den
kommer från grundegenskapen, färdigheten eller
prylen. Detta är för att man kan välja att
"pressa" sitt slag. Då får man slå om alla
tärningar som inte visar 1 eller 6 (plus ettor
från färdighetvärdets tärningar).

När du slagit om slaget så räknar du ihop
antalet sexor som vanligt, fler är bättre.
Sen räknar du ihop alla ettor från tärningarna
som tillhörde grundattributet och tar lika mycket
i skada. Gör samma sak för din pryl som tar skada
på samma sätt.

Anta att din karaktär har 4 i karisma, 3 i
manipulera och 2 i prylbonus. Rulla 4+3+2 tärningar
och pressa sen slaget. Hur mycket skada tar din
karaktär, och hur mycket skada tar prylen?
"""
