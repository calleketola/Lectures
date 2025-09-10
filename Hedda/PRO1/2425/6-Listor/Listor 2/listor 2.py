import random

"""
Uppgift 1 t.o.m. 4 utgår alla från samma
lista som du skapar själv.
"""


###############
## UPPGIFT 1 ##
###############

"""
Skapa en lista som innehåller alla heltal
från 0 till och med 12
"""

a = []
for i in range(13):
    a.append(i)
print(a)

###############
## UPPGIFT 2 ##
###############

"""
Multiplicera alla talen med 2 och spara de
nya värdena istället.

([0,1,2,...] -> [0,2,4,...])
"""
for i in range(len(a)):
    a[i] = i*2
print(a)
###############
## UPPGIFT 3 ##
###############

"""
Plocka bort talet 12 ur listan
"""
a.remove(12)
print(a)

###############
## UPPGIFT 4 ##
###############

"""
Lägg till talen: 3, 5, 7, 9, 11, 13, 15 och 17 i listan
"""
for i in range(3,18,2):
    a.append(i)
print(a)

###############
## UPPGIFT 5 ##
###############

"""
Skriv det största och minsta värdena ur listan.
Tips: undersök funktionerna max() och min()
"""

uppgift_5 = []

for i in range(10):
    uppgift_5.append(random.randint(1,100))

###############
## UPPGIFT 6 ##
###############

"""
Bestäm medelvärdet av talen i listan 
"""


###############
## UPPGIFT 7 ##
###############

"""
Hitta medianen av talen i listan
"""

###############
## UPPGIFT 8 ##
###############

"""
Bestäm typvärdet i listan (vanligast förekommande tal)

Tips: undersök funktionen count()
"""


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

################
## UPPGIFT 11 ##
################

"""
Lägg till att programmet frågar efter talet du
behöver nå för att klara en handling.
"""

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
"""
Exempel på utskrifter:
STY: 14
SMI: 8
UTH: 12
INT: 13
VIS: 11
KAR: 10

Egenskap: styrka
Målvärde: 12

Du rullade: 11
Bonus: +2
Resultat: 13

Du lyckades
"""


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

Om skadan på karaktären är lika med värdet i
grundegenskapen så ska programmet skriva ut att
du är BRUTEN.

Om skadan på prylen är ika med bonusen den ger
så ska du skriva att den är sönder.
"""
"""
Exempel på utskrift:

Resultat GRUND: 1 5 6 2
Resultat FÄRD: 4 2 1
Resultat PRYL: 3 1

Pressning GRUND: (1 6) 3 6
Pressning FÄRD:  5 6 6
Pressning PRYL: (1) 1

Totalt: 4 sexor
Du tar 1 skada på karisma
Din pryl tar 2 skada.
Prylen gick sönder
"""



