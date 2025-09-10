# Ett program som tar emot data och gör saker beroende på vad det är

"""
Uppgift 1
Det finns en logisk bugg på raderna 12-15,
rätta till den.
"""

variabel1 = input("Skriv något:\n")
variabel2 = input("Skriv något mer:\n")

if len(variabel1) > len(variabel2):
    print(variabel1, "är längre än", variabel2)
else:
    print(variabel2, 'är längre än', variabel1)

"""
Uppgift 2
Skriv ett program som tar emot ett tal
och skriver ut följande baserat på talet:
Hur många år bakåt i tiden vill du resa? 
"Iran fanns för så många år sedan" (<4600)
"Då fanns Indien" (<4500)
"Man kan mena att Kina att skapats då" (<3624)
"Då hade du kunnat besöka landet Etiopien" (<1124)
"Danmark hade formats då" (<1059)
"Då existerade Sverige" (<1054)
"Thailand fanns då" (<257)
"Kuba är ett eget land" (<126)
"Nu är Finland självständigt" (<106)
"Montenegro är självständigt" (<16)
"Inga länder du besöker kommer att finnas 2024" (>4600)

Enbart en utskrift per tal man skriver in
ska skrivas ut
"""



"""
Övning 3
Skriv ett program som kollar om ett ord är
skrivet med bara versaler, gemener eller om
det är blandat.
"""
# textvariabel.lower() => bara små bokstäver
# textvariabel.upper() => bara stora bokstäver

"""
Övning 4
Skriv ett program som tar emot ett årtal
(efter 1753) och returnerar om det var ett
skottår eller ej. Tänk på att år jämnt delbara
med 100 inte är skottår, men att år delbara med
400 är fortfarande skottår. (1800 och 1900 ej
skottår men 2000 och 2400 skottår.)
"""


"""
Saxad övning 1
En operatörför mobiltelefoni erbjuder tre olika
abonnemang: Kontant, Normal och Plus. Om man jämför
villkoren för abonnemangen visar det sig att Kontant
är billigast om man ringer högst 33 minuter per
månad, Normal lönar sig bäst om man ringer mellan
33 och 36 minuter per månad och Plus är mest
förmånligt om man ringer ännu mer.

Skriv ett program som läser in antalet minuter man
uppskattar att man kommer att ringa per månad.
Programmet ska tala om vilket abonnemang man bör
välja.
"""

"""
Saxad övning 2
I en triangel kan man beteckna sidorna med a, b
och c. Om man känner till längderna för sidorna
a och b samt vinkeln v mellan dessa sidor så
kan man räkna ut längden av sidan c med formeln:
	
    c = sqrt(a^2+b^2-2ab*cos(v))

	
Skriv ett program som läser in längderna
på två sidor i en triangel och vinkeln mellan
sidorna. Programmet ska avgöra om triangeln är
liksidig (alla sidor lika), likbent (två sidor
lika) eller oliksidig (inga sidor lika).
	
Python jobbar i radianer:
v grader => v * pi/180 radianer
"""
