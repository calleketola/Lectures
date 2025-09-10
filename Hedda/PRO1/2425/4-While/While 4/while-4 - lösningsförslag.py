lista_med_tal = [6,4,1,9,4,2,7,5,2,3,7,2,1,9,5,10,2,3,9]
i = 0
print(lista_med_tal)
while i < len(lista_med_tal):
    print(lista_med_tal[i])
    i += 1

##############
## ÖVNING 1 ##
##############

"""
Skriv ut summan av alla tal i lista_med_tal
"""

##############
## ÖVNING 2 ##
##############

"""
Skriv ut produkten av alla tal i lista_med_tal
"""

##############
## ÖVNING 3 ##
##############
saga = """Det var en gång för länge sedan en liten liten nyckelpiga. Nyckelpigan hetta Birgitta och hade exakt fyra prickar på sitt skal. Birgitta var väldigt självmedveten om antalet prickar på sitt skal, så varje morgon ritade hon på tre nya prickar så att hon hade sju prickar.

En vacker höstdag, när daggen låg fint och blänkte i solen, så fångades Birgitta av en vindpust och ramlade ner i en daggdroppe. Daggdroppen tvättade bort hennes tre extra prickar, utan att hon märkte det. Så när Birgitta kom loss ur daggdroppen flög hon vidare med bara sina fyra prickar på skalet.

Alla Birgittas kompisar hälsade som vanligt på Birgitta och var snälla och trevliga. Så Birgitta var på gott humör när hon landade vid sitt favoritmatställe och började mumsa på bladlöss. Hon var så nöjd att hon inte märkte att superstygga spindel Sigvard kom upp för stjälken på blomman.

Med varje steg superstygga spindeln Sigvard tog upp för stjälken stannade han och räknade hur många steg han tagit hittils. "Fy, nu har jag tagit fem steg." Sa Sigvard. Sen tog han ett nytt steg och sa: "Oh vad bra. Nu har jag tagit sex steg!" OCh så fortsatte han varannat steg fräste och spottade han om han sa ett udda tal och varannat steg jublade han över att han tagit ett jämnt antal steg.

Snart var superstygga spindeln Sigvard bara några blad från Birgitta. Där hade han stannat och räknat bladlöss. "Femtiotre. Fy, vad hemskt." Och så slet han bort bladet från blomman. När han kom till nästa blad räknade han bladlöss igen. "36. Vad trevligt. Ha det så bra kära löss." Till slut kom han till Birgitta som just ätit upp alla bladlöss. "Noll stycken löss. Det är jämt och fint. Men! Hur många prickar har du?" Nu blev Birgitta jätterädd för hon hade ju målat på tre prickar på sitt skal och blivit udda.

Rädd som en hare och skakandes som ett asplöv svarade Birgitta: "Oj, hur ska jag veta det som inte kan se min egen rygg?" Superstygga spindeln Sigvard vände på Birgitta och räknade hennes prickar.

"En prick, usch! Två prickar, fint. Tre prickar, nej nej nej. Fyra prickar!" Sigvard slog ut med händerna och sa: "Vad bra. Du har ju fyra prickar det är jämt och fint." Sen klättrade han vidare och räknade sina steg och bladlöss på varje blad.

Birgitta flög snabbt därifrån tillbaka till sina kompisar som hon hälsat på tidigare. Då berättade hon för dem vad som hänt och frågade varför ingen av dem sagt att hon sett annorlunda ut. Då svarade hennes kompisar att hon ju varit precis lika fin som vanligt, och att fyra prickar var precis lika bra som sju prickar.

Sen den dagen slutade Birgitta att måla på nya prickar på sitt skal och var nöjd som hon var."""

"""
Hur många bokstäver finns det i variabeln saga? 
"""



##############
## ÖVNING 4 ##
##############

"""
Vilken bokstav är vanligast i variabeln saga?
"""
stäver = {}
for stav in saga.lower():
    if stav == " ":
        continue
    if stav in stäver:
        stäver[stav] += 1
    else:
        stäver[stav] = 1

vanligast = 'a'
for stav in stäver:
    if stäver[stav] > stäver[vanligast]:
        vanligast = stav
print(vanligast, stäver[vanligast])

##############
## ÖVNING 5 ##
##############

"""
Hur många ord finns det i sagan?
"""

words = "Dance while the music still goes on".split()
print(words)

##############
## ÖVNING 6 ##
##############

"""
Vilket ord är vanligast i sagan?
"""



