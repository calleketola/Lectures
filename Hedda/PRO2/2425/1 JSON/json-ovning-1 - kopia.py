##############
## ÖVNING 1 ##
##############

"""
Skriv ut alla nycklar i variabeln eurovision
"""

eurovision = {"Stockholm": 2, "Göteborg": 1, "Malmö": 2}

for key in eurovision:
    print(key)

##############
## ÖVNING 2 ##
##############
print('---------')
"""
Skriv ut alla nycklar med sina respektive värden
i variabeln eurovision
"""
for key in eurovision:
    print(key, eurovision[key])


##############
## ÖVNING 3 ##
##############

print('---------')
"""
Variabeln antal är en dictionary med alfabetet.
Använd den för att räkna hur många gånger varje
bokstav förekommer i texten som är sparad i
variabeln text.
"""

antal = {chr(x):0 for x in range(97,123)}
antal['å'] = 0
antal['ä'] = 0
antal['ö'] = 0

text = "hej alla glada och pigga elever som vill lära sig så väldigt mycket mer om programmering."

for tecken in text:
    if tecken in antal:
        antal[tecken] += 1
print(antal)
##############
## ÖVNING 4 ##
##############

"""
Vilken bokstav var vanligast i texten?
"""
vanligast = 'a'
for bokstav in antal:
    if antal[bokstav] > antal[vanligast]:
        vanligast = bokstav
print(vanligast)

###############
## ÖVNING 5+ ##
###############

import json
