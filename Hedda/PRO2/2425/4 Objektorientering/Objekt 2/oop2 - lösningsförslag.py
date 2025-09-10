"""
Klassdiagram:

____________________________
|         Karaktär         |
|__________________________|
| namn : str               |
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
hugg eller stöt.

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
"""

import random

class Karaktär():

    def __init__(self, namn, sty, kar, närkamp, manipulera, genomskåda):
        self.namn = namn
        self.styrka = sty
        self.karisma = kar
        self.närkamp = närkamp
        self.manipulera = manipulera
        self.genomskåda = genomskåda

        # Detta ska karaktären få senare? Så får basic prylar nu
        self.svärd = Vapen(0,1)
        self.sköld = Sköld(0)

    def attackera(self):
        typ = " "
        while typ[0] != "h" and typ[0] != "s":
            typ = input("Hugger eller stöter {}?\n".format(self.namn)).lower()

        sexor = 0
        tärningar = self.styrka+self.närkamp+self.svärd.bonus # Räkna ihop antalet tärningar

        # Rulla tärnignar
        for i in range(tärningar):
            if random.randint(1,6) == 6:
                sexor += 1

        if self.svärd.episk: # Om vårt vapen är episkt
            roll = random.randint(1,8)
            if roll >= 6: # Allt över sex ger en success
                sexor += 1
            if roll >= 8: # Åtta ger ytterliggare en success
                sexor += 1
                
        return [sexor,typ[0]]

    def försvara(self, t):
        """
        t: sträng som breskriver attacktyp
        """
        sexor = 0
        tärningar = self.styrka+self.närkamp+self.sköld.bonus # Räkna ihop antalet tärningar
        if t == "s":
            if self.sköld.bonus == 0:
                tärningar -= 2
            else:
                tärningar += 2

        for i in range(tärningar):
            if random.randint(1,6) == 6:
                sexor += 1

        if self.sköld.episk: # Om vår sköld är episkt
            roll = random.randint(1,8)
            if roll >= 6: # Allt över sex ger en success
                sexor += 1
            if roll >= 8: # Åtta ger ytterliggare en success
                sexor += 1
                
        return sexor

    def manipulera(self):
        return 0

    def genomskåda(self):
        return 0

class Vapen():

    def __init__(self, bonus, skada, episk = False):
        self.bonus = bonus
        self.skada = skada
        self.episk = episk

class Sköld():

    def __init__(self, bonus, episk = False):
        self.bonus = bonus
        self.episk = episk


gubbe1 = Karaktär("Calle", 4, 3, 3, 2,2)
gubbe2 = Karaktär("Enrique", 5, 4, 2,1,2)

gubbe1.vapen = Vapen(2,1, True)
gubbe2.vapen = Vapen(2,2)

gubbe2.sköld = Sköld(2)

while gubbe1.styrka > 0 and gubbe2.styrka > 0:

    print("{} styrka: {}, {} styrka: {}".format(gubbe1.namn,gubbe1.styrka,
                                                gubbe2.namn, gubbe2.styrka))
    print(gubbe1.namn, "anfaller", gubbe2.namn)
    attack = gubbe1.attackera()
    försvar = gubbe2.försvara(attack[1]) # Skickar med attacktyp

    resultat = attack[0] - försvar
    if resultat > 0:
        skada = gubbe1.svärd.skada+(resultat-1)
        gubbe2.styrka -= skada
        print("{} tar {} skada!".format(gubbe2.namn, skada))
    else:
        print("{} försvarar sig mot {}s attack!".format(gubbe2.namn, gubbe1.namn))

    if gubbe2.styrka <= 0:
        print("{} faller död till marken.".format(gubbe2.namn))
        break

    print("{} styrka: {}, {} styrka: {}".format(gubbe1.namn,gubbe1.styrka,
                                                gubbe2.namn, gubbe2.styrka))

    print(gubbe2.namn, "anfaller", gubbe1.namn)
    attack = gubbe2.attackera()
    försvar = gubbe1.försvara(attack[1]) # Skickar med attacktyp

    resultat = attack[0] - försvar
    if resultat > 0:
        skada = gubbe2.svärd.skada+(resultat-1)
        gubbe1.styrka -= skada
        print("{} tar {} skada!".format(gubbe1.namn, skada))
    else:
        print("{} försvarar sig mot {}s attack!".format(gubbe1.namn, gubbe2.namn))

    if gubbe1.styrka <= 0:
        print("{} faller död till marken.".format(gubbe1.namn))
        break



input("Nu är striden slut.")
    
    
    
    
