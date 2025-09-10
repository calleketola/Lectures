"""
Klassdiagram:

____________________________
|         Karaktär         |
|__________________________|
| styrka : int             |
| karisma : int            |
| närkamp : int            |
| manipulera : int         |
| genomskåda : int         |
| svärd : vapen            |
| sköld : sköld            |
|__________________________|
| attackera() : [int, str] |
| försvara(t : str) : int  |
| övertala() : int       |
| förstå() : int       |
|__________________________|

___________________________
|          Vapen          |
|_________________________|
| bonus : int             |
| skada : int             |
| episk : bool            |
|_________________________|
|_________________________|

___________________________
|          Sköld          |
|_________________________|
| bonus : int             |
| episk : bool            |
|_________________________|
|_________________________|
"""
import random

class Vapen():

    def __init__(self, b, s, e):
        self.bonus = b
        self.skada = s
        self.episk = e

class Sköld():

    def __init__(self, b, e):
        self.bonus = b
        self.episk = e

class Karaktär():

    def __init__(self, sty, kar, när, man, gen):
        self.styrka = sty
        self.karisma = kar
        self.närkamp = när
        self.manipulera = man
        self.genomskåda = gen

        self.svärd = None
        self.sköld = None

    def attackera(self):
        tärningar = self.styrka + self.närkamp + self.svärd.bonus
        sexor = 0
        for i in range(tärningar):
            if random.randint(1,6) == 6:
                sexor += 1
        typ = random.choice(["hugg","stick"])
        return [sexor, typ]

    def försvara(self, t):
        if isinstance(self.sköld, Sköld):
            tärningar = self.styrka + self.närkamp + self.sköld.bonus
        else:
            tärningar = self.styrka + self.närkamp
        if t == "stick":
            if isinstance(self.sköld, Sköld):
                tärningar += 2
            else:
                tärningar -= 2
        sexor = 0
        for i in range(tärningar):
            if random.randint(1,6) == 6:
                sexor += 1
        return sexor
        



"""
Beskrivningar av metoderna

Karaktär.attackera(): [int, str]
Programmet ska rulla ett antal tärningar lika med
styrka + närkamp + svärd.bonus. Sen ska det skicka tillbaka
antalet sexor samt om det var ett hugg eller stick.

Karaktär.försvara(t: str): int
Programmet ska rulla ett antal tärningar lika med
styrka + närkamp + sköld.bonus. Sen ska det skicka tillbaka
antalet sexor. Om du vill göra det bättre så ska
programmet rulla olika antal tärningar beroende på
vilken typ av attack motståndaren gör. Om motståndaren
gör ett stick så får man en bonus på två tärningar
om man har en sköld, och minus två tärningar om
man inte har en sköld.

Karaktär.Övertala(): int
Programmet ska rulla ett antal tärningar lika med
karisma + manipulera och skicka tillbaka antalet
sexor.

Karaktär.förstå(): int
Programmet ska rulla ett antal tärningar lika med
karisma + genomskåda och skicka tillbaka antalet
sexor.
"""

"""
I spelet Svärdets sång slår man sex-sidiga tärningar för
att se om man lyckas med en handling. I en strid får både
försvararen och anfallaren slå för om de lyckas träffa
eller undvika, och den som lyckas mest lyckas. Allstå om
anfallaren får fler sexor än försvararen tar försvararen
skada och om försvararen får fler sexor än anfallaren så
tar hen ingen skada.

För att avgöra hur många tärningar man ska slå tar man
en karaktärs STYRKA + deras förmåga i NÄRKAMP + bonus
från eventuellt VAPEN. Varje gång en karaktär tar skada
så minskar värdet i STYRKA med lika mycket, och när
värdet når noll (eller mindre) så kan man inte längre
strida. (Systemet fungerar likadant för argumentationer
fast då använder man sig av KARISMA och MANIPULERA för
att "anfalla" och GENOMSKÅDA för att "försvara" sig.
Har man dessutom ett föremål som hjälper ens argumentation
får man en bonus från det med.)

Värdet för en karaktärs STYRKA (KARISMA) kan variera mellan
två och sex. Värdet för en karaktärs NÄRKAMP (MANIPULERA
eller GENOMSKÅDA) kan variera mellan noll och fem. Bonusen
från ett vapen kan variera från ett till tre.

1) Skriv ett program där två karaktärer möts i en strid och
turas om att anfalla och försvara sig (systemet tillåter
fler handlingar, men det tar vi senare). Båda ska slå sina
tärningar för anfall och försvar. Vinner den som anfaller
tar försvararen lika mycket skada motsvarande vapnets skade-
värde på STYRKA plus antalet sexor-1 den har fler än mot-
ståndaren. Om någon av karaktärerna hamnar på noll i STYRKA 
är striden slut.

NOTERA: Varje gång en karaktär tar skada så minskar antalet
tärningar den får rulla.

Ex:
Karaktär 1 rullar [6,6,4,3,6,5,6,6] : 5x6
Karaktär 2 rullar [1,5,2,3,6,3,1,2] : 1x6
Vapnet har skadevärde 2
Karaktär 1 gör 2+3=5 skada på Karaktär 2 (2 skada från vapnet 
+3 för att hen slog 4 fler sexor än försvararen)

2) För att öka spänningen kan karaktärerna välja mellan att
hugga och sticka med sina vapen. Lägg till att man väljer
hugg eller stöt när man gör ett angrepp.

3) Att skydda sig mot ett hugg eller en stöt är olika svårt.
Här spelar det också roll om man har en sköld eller inte.
Lägg till en sköld på den ena spelaren. Att försvara sig mot
en stöt utan sköld är svårt, ge försvararen -2 tärningar på
sitt försvarsslag. Att skydda sig mot en stöt med sköld är
lättare, ge försvararen +2 tärningar på sitt försvarsslag.

4) En del vapen är så episka att man får rulla en extra
åttasidig tärning på sin attack. Ge den ena karaktären ett
sådant vapen. På en åttasidig tärning räknas ett resultat på
sex eller sju som en lyckad sexa, medan ett slag på åtta
räknas som två lyckade sexor. I.e. slår man tre sexsidiga
och en åttasidig tärning och får 1, 6, 5, 8 räknas det som
tre sexor
____________________________
|         Karaktär         |
|__________________________|
| styrka : int             |
| karisma : int            |
| närkamp : int            |
| manipulera : int         |
| genomskåda : int         |
| svärd : vapen            |
| sköld : sköld            |
|__________________________|
| attackera() : [int, str] |
| försvara(t : str) : int  |
| manipulera() : int       |
| genomskåda() : int       |
|__________________________|
"""


# Driverkod
svärd = Vapen(2,1, False)
yxa = Vapen(1,2,False)

liten_sköld = Sköld(1,False)

spelare_1 = Karaktär(5,3,3,2,1)
spelare_1.svärd = svärd

spelare_2 = Karaktär(4,4,2,3,2)
spelare_2.svärd = yxa
spelare_2.sköld = liten_sköld

slåss = True
tur = 0
while slåss == True:
    input("Ny runda. Tryck enter för att slåss...")
    if tur == 0:
        a_lyckade, typ = spelare_1.attackera()
        print("Spelare 1 rullade", a_lyckade, "sexor och gjorde ett", typ)
        f_lyckade = spelare_2.försvara(typ)

        print("Spelare 2 rullade", f_lyckade, "sexor")
        if a_lyckade > f_lyckade:
            print("Spelare 1 träffade! Och gör", a_lyckade-f_lyckade, "skada")
            spelare_2.styrka -= a_lyckade-f_lyckade
        else:
            print("Spelare 1 missade!")
            
        tur = 1
    else:
        a_lyckade, typ = spelare_2.attackera()
        f_lyckade = spelare_1.försvara(typ)

        print("Spelare 2 rullade", a_lyckade, "sexor")
        print("Spelare 1 rullade", f_lyckade, "sexor")
        if a_lyckade > f_lyckade:
            print("Spelare 2 träffade! Och gör", a_lyckade-f_lyckade, "skada")
            spelare_1.styrka -= a_lyckade-f_lyckade
        else:
            print("Spelare 2 missade!")


        tur = 0
    if spelare_1.styrka <= 0:
        print("Spelare 1 är bruten")
        slåss = False
    if spelare_2.styrka <= 0:
        print("Spelare 2 är bruten")
        slåss = False











