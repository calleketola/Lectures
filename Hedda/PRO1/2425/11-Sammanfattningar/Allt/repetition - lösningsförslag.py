###############
## ÖVNING 01 ##
###############

"""
Skriv ett program som tar emot
fem ord/meningar och skriver ut
vilken som var längst.
"""

antal = 5
svar = []
for i in range(antal):
    s = input("skriv en mening: ")
    svar.append(s)

längst = svar[0]
for i in range(antal):
    if len(svar[i]) > len(längst):
        längst = svar[i]
print(längst, "var längst")

###############
## ÖVNING 02 ##
###############

"""
Skriv ett program som frågar
hur många tal det ska ta emot.
Sen ska det ta emot så många
tal och räkna ut medelvärdet av dem.
"""

antal = input("Hur många tal? ")
antal = int(antal)
tal = []
for i in range(antal):
    t = input("Skriv ett tal: ")
    t = float(t)
    tal.append(t)
medel = sum(tal)/antal
print(medel)


###############
## ÖVNING 03 ##
###############

"""
Skriv ett program som simulerar en
bilmack. Programmet ska berätta
priset för en liter bensin och
priset för en liter diesel. Sen ska
användaren få välja bensin eller
diesel och hur mycket hen vill tanka.

Programmet ska sen skriva ut ett
kvitto på formen:
 _____________________________
|           Kvitto            |
|                             |
| Valt drivmedel: Bensin      |
| Pris per liter: 19.42 kr    |
| Tankat: 43.12 liter         |
| Pris att betala:  837.39 kr |
|_____________________________|
alternativt:
 _____________________________
|           Kvitto            |
|                             |
| Valt drivmedel: Diesel      |
| Pris per liter: 24.01 kr    |
| Tankat: 43.12 liter         |
| Pris att betala: 1035.31 kr |
|_____________________________|
"""

pris_bensin = 19.42
pris_diesel = 24.01

print("Priser")
print("1. Bensin:", pris_bensin)
print("2. Diesel:", pris_diesel)

fråga = True
bensin = False

while fråga:
    print("Vill du tanka bensin eller diesel?")
    svar = input()

    if svar[0].lower() == 'b' or svar == '1':
        bensin == True
        fråga = False
        print("Du har valt bensin")
    elif svar[0].lower() == 'd' or svar == '2':
        bensin == False
        fråga = False
        print("Du har valt diesel")

tanka = input("Hur mycket vill du tanka?\n")
tanka = float(tanka)

betala = 0
if bensin:
    betala = pris_bensin*tanka
else:
    betala = pris_diesel*tanka

print(" _____________________________")
print("|           Kvitto            |")
print("|                             |")

if bensin:
    print("| Valt drivmedel: Bensin      |")
    print("| Pris per liter:", pris_bensin,"kr    |")
else:
    print("| Valt drivmedel: Diesel      |")
    print("| Pris per liter:", pris_diesel,"kr    |")

print("| Tankat:", round(tanka,2), "liter         |")  
print("| Pris att betala:", round(betala,2), "kr |")
print("|_____________________________|")
###############
## ÖVNING 04 ##
###############

"""
I Åre, en svensk skidort, besöker
ungefär 14 000 personer backarna
varje dag under sportlovet
(https://www.besoksliv.se/nyheter/fler-drar-till-fjalls-for-sportlov/)
och under ett år gipsar vårdcentralen
närmast skidbacken ungefär 700
personer
(https://lakartidningen.se/wp-content/uploads/OldWebArticlePdf/3/3733/1087_1088.pdf).

Antag att 80 % av alla som gipsas
görs det under sportlovsveckorna
(vecka 7-10). Skriv ett program som
tar emot antal besökare i backarna
per dag och som sen skriver ut
hur många av dem som antagligen får
ett benbrott och behöver gipsas.
"""
andel_skidbrott = 0.8
total_gipsningar = 700
normalt_antal_skidare = 14000
andel_som_gipsas = total_gipsningar*andel_skidbrott/normalt_antal_skidare


besökare = input("Besökare per dag: ")
besökare = int(besökare)

benbrott = besökare*andel_som_gipsas
print("Ungefär", round(benbrott), "kommer att behöva gipsas.")
