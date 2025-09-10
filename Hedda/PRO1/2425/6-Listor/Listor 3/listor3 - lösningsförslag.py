texten = """Den vintertid nu kommer med snö och vind från nord
Har pulsat genom staden i alltför tunga skor
Här står jag på perrongen och väntar på ditt tåg
I samma gamla mössa jag hade sist vi sågs
"""


##############
## ÖVNING 1 ##
##############

# Dela upp texten i ord

words = texten.split()

print(words)


##############
## ÖVNING 2 ##
##############

# Hur många ord är det i texten?

print(f"Det är {len(words)} ord i texten")

##############
## ÖVNING 3 ##
##############

# Räkna hur många ord med längden tre det finns
of_length_three = 0
for word in words:
    if len(word) == 3:
        of_length_three += 1
print(f"Det är {of_length_three} ord med längden tre i texten")

##############
## ÖVNING 4 ##
##############

# Dela istället upp texten i tecken.
# Hur många bokstäver finns det?
# Vilken bokstav är vanligast?

# Detta är ett sneaky sätt att få bort mellanslag
tt = texten.replace(" ", "")
letters = list(tt)
print(f"Det finns totalt {len(letters)} bokstäver i texten")
# Ett annat sätt hade varit att räkna totala antalet
# tecken och subtrahera med antalet ord-1
#(varför minus 1? klura på den du)

ll = [] # Om man använder en dictionary blir det snyggare

for i in range(len(letters)):
    letter = letters[i]
    if not letter in letters[:i]:
        n = texten.count(letter) # Det här är lättaste sättet
        ll.append((letter, n)) # Här finns ett snyggare sätt med dictionary
print(ll)
most_common = 0
for i in range(len(ll)):
    if ll[i][1] > ll[most_common][1]:
        most_common = i
print(ll[most_common][0], "är vanligast i texten")


##############
## Sista öv ##
##############

# Kryptera texten med ett caesarchiffer
# https://sv.wikipedia.org/wiki/Caesarchiffer
# "".join(lista) konverterar till sträng igen

# Gör en kod som läser tillbaka den igen

# Här kommer inget facit
# Men du kan få en start

texten = texten.upper()
alfabet = [chr(i) for i in range(65, 91)]+['Å','Ä','Ö']

print(alfabet)








