texten = """Den vintertid nu kommer med snö och vind från nord
Har pulsat genom staden i alltför tunga skor
Här står jag på perrongen och väntar på ditt tåg
I samma gamla mössa jag hade sist vi sågs
"""


##############
## ÖVNING 1 ##
##############

# Dela upp texten i ord
# Kolla upp kommandot .split()

words = texten.split()
#print(words)

##############
## ÖVNING 2 ##
##############

# Hur många ord är det i texten?

print("Det är", len(words), "ord i listan")

##############
## ÖVNING 3 ##
##############

# Räkna hur många ord som har exakt tre bokstäver i sig
antal = 0
for word in range(len(words)):
    if len(words[word]) == 3:
        antal += 1
print("Det är", antal, "ord som är tre tecken långa")

##############
## ÖVNING 4 ##
##############

# Dela istället upp texten i tecken.
# Hur många bokstäver finns det?
# Vilken bokstav är vanligast?

tecken = list(texten)

while " " in tecken:
    tecken.remove(" ")
while "\n" in tecken:
    tecken.remove("\n")
print("Det finns", len(tecken), "bokstäver i texten")
##############
## Sista öv ##
##############

# Kryptera texten med ett caesarchiffer
# https://sv.wikipedia.org/wiki/Caesarchiffer
# "".join(lista) konverterar till sträng igen

# Gör en kod som läser tillbaka den igen
