"""
I Python är det möjligt att spara listor i
andra listor.

Ex:

a = [[1,2,3],[4,5,6],[7,8,9]]

För att komma åt enskilda element behöver man
skriva i stil med:
a[1][2]
Vilket skulle peka på listan på plats ett och
element två, alltså 6 i det här fallet. 
"""

import random

###############
## ÖVNING 01 ##
###############

"""
Utgå från lista01 och skriv ut antalet
listor i listan
"""

lista01 = []
for i in range(5):
    for j in range(10):
        lista01.append(random.randint(1,100))

###############
## ÖVNING 02 ##
###############

"""
Skriv ut det totala antalet element i
lista01.
"""

###############
## ÖVNING 03 ##
###############

"""
Räkna ut summan av alla talen i lista01.
"""

###############
## ÖVNING 04 ##
###############

"""
Skriv ut den listan som har LÄGST summa.
"""

###############
## ÖVNING 05 ##
###############

"""
Skriv ut varje listas medelvärde
"""


###############
## ÖVNING 06 ##
###############

"""
Skapa en lista med 12 listor som innehåller
slumpade tal som följer följande mönster:

[5]
[7,2]
[9,2,6]
[1,7,4,2]
...
"""

###############
## ÖVNING 07 ##
###############

"""
Vilket är det vanligast förekommande talet
i listan?
"""

###############
## ÖVNING 08 ##
###############

"""
En dictionary är som en lista, fast istället
för att indexera med tal så kan man indexera
med vad man vill.

a = {} # En tom dictionary
a['hej'] = 5 # Skapar platsen 'hej' och sparar värdet 5
a['hej'] += 3
print(a['hej']) -> 8

b = {'q': 2, 'w': 'abba'} # Skapar en dictionary med de två platserna 'q' och 'w'

for key in b:
    print(key)
>>> 'q'
>>> 'w'
for key in b:
    print(b[key])
>>> 2
>>> 'abba'
"""

"""
Variabeln iron_maiden är en dictionary med
låtnamnen på skivan som nycklar (index) och
längden på varje låt i minuter.

Skriv ut namnet på alla låtar.
"""

iron_maiden = {'Prowler': 3.87,
               'Remember Tomorrow': 5.42,
               'Running Free': 3.23,
               'Phantom of the Opera': 7.08,
               'Transylvania': 4.1,
               'Strange World': 5.67,
               'Charlotte the Harlot': 4.17,
               'Iron Maiden': 3.52}

###############
## ÖVNING 09 ##
###############

"""
Skriv ut låttitel och längd på alla låtar
"""

###############
## ÖVNING 10 ##
###############

"""
Hur lång är skivan i minuter?
"""

###############
## ÖVNING 11 ##
###############

"""
Hur lång är skivan i sekunder?
"""

###############
## ÖVNING 09 ##
###############

"""
I DOTA 2 styr man en hjälte som har fyra
specialförmågor.

Skriv ett program som tar emot ett
hjältenamn och skriver ut följande:
NAMN
Förmåga 1:
Namn: Förmågans namn
Kostnad: Förmågans pris
Nedvarvning: Förmågans cooldown

Förmåga 2:
Namn: Förmågans namn
Kostnad: Förmågans pris
Nedvarvning: Förmågans cooldown

Förmåga 3:
Namn: Förmågans namn
Kostnad: Förmågans pris
Nedvarvning: Förmågans cooldown

Förmåga 4:
Namn: Förmågans namn
Kostnad: Förmågans pris
Nedvarvning: Förmågans cooldown
"""
## Exempelresultat:
# Vilken hjälte vill du veta mer om?
# >>> Dazzle
# DAZZLE
# Förmåga 1:
# Namn: Poison Touch
# Kostnad: 125 mana
# Nedvarvning: 27.0 sekunder 
#
# Förmåga 2:
# Namn: Shallow Grave
# Kostnad: 90 mana
# Nedvarvning: 36.0 sekunder
#
# Förmåga 3:
# Namn: Shadow Wave
# Kostnad: 75
# Nedvarvning: 12.0 sekunder

# Förmåga 4:
# Namn: Bad Juju
# Kostnad: 0 mana
# Nedvarvning: 3.0 sekunder

heroes = {'Abaddon': [['Mist Coil', 50, 6.6],
                      ['Aphotic Shield', 95, 12.0],
                      ['Curse of Avernus', 0, 0.0],
                      ['Borrowed Time', 0, 70.0]],
          'Alchemist': [['Acid Spray', 120, 22.0],
                      ['Unstable Concoction', 100, 1.0],
                      ['Corrosive Weaponry', 0, 0],
                      ['Chemical Rage', 50, 60.0]],
          'Ancient Appiration': [['Cold Feet', 125, 15.0],
                      ['Ice Vortex', 40, 10.0],
                      ['Chilling Touch', 30, 12.0],
                      ['Ice Blast', 175, 60.0]],
          'Anti-Mage': [['Mana Break', 0, 0.0],
                      ['Blink', 45, 13.5],
                      ['Counterspell', 45, 15.0],
                      ['Mana Void', 100, 70.0]],
          'Arc Warden': [['Flux', 75, 16.0],
                      ['Magnetic Field', 50, 20.0],
                      ['Spark Wraith', 80, 4.0],
                      ['Tempest Double', 0, 70.0]],
          'Axe': [["Berserker's Call", 80, 17.0],
                      ['Battle Hunger', 50, 20.0],
                      ['Counter Helix', 0, 0.3],
                      ['Culling Blade', 100, 100.0],
                      ['Borrowed Time', 0, 70.0]],
          'Bane': [['Enfeeble', 120, 28.0],
                      ['Brain Sap', 100, 17.0],
                      ['Nightmare', 120, 24.0],
                      ["Fiend's Grip", 200, 120.0]],
          'Dazzle': [["Poison Touch", 125, 27.0],
                     ["Shallow Grave", 90, 36.0],
                     ["Shadow Wave", 75, 12.0],
                     ["Bad Juju", 0, 3.0]]
          }
