####################
## ÖVNINGAR 01-05 ##
####################

"""
1. Läs in filen filhantering-3-a.txt
2. Vilket är det största talet i filen?
3. Vilket tal är närmast noll?
4. Vad är medelvärdet av talen?
5. Vad är medianen?
"""

with open('filhantering-3-a.txt') as f:
    rader = f.readlines() # Läser in filen
    
for rad in range(len(rader)): # Gå igenom alla rader
    rader[rad] = int(rader[rad]) # Konvertera till tal

print("2. Det största talet är", max(rader))

närmast = 0
for rad in range(len(rader)):
    if abs(rader[rad]) < abs(rader[närmast]):
        närmast = rad

print("3. Det talet som är närmast noll är", rader[närmast])

medel = sum(rader)/len(rader)

print("4. Medelvärdet är", medel)

rader.sort()

median = (rader[len(rader)//2]+rader[len(rader)//2+1])/2

print("5. Medianen är", median)

####################
## ÖVNINGAR 06-11 ##
####################

"""
6.  Läs in filen filhantering-3-b.txt
7.  Skriv ut innehållet i filen
8.  Verket saknar fem veresr. Lägg till dem i en
    ny fil som heter the-nomad.txt
9.  Vilket ord är vanligast förekommande i hela
    texten?
10. Vilken rad i hela texten är längst?
11. Hur många rader slutar på bosktaven n?
"""

with open('filhantering-3-b.txt') as f:
    text = f.read()

print('7.\n', text)

with open('the-nomad.txt', 'w') as f:
    f.write(text)
    f.write('\n\n')
    f.write("""Nomad, you're the rider so mysterious
Nomad, you're the spirit that men fear in us
Nomad, you're the rider of the desert sands
No man's ever understood your genius

Those who see you in horizon desert sun
Those who fear your reputation hide or run
You send before you a mystique that's all your own
Your silhouette is like a statue carved in stone

Nomad, you're the rider so mysterious
Nomad, you're the spirit that men fear in us
Nomad, you're the rider of the desert sands
No man ever understood your genius

Legend has it that you speak an ancient tongue
But no one's spoke to you and lived to tell the tale
Some may say that you have killed a hundred men
Others say that you have died and live again

Nomad, you're the rider so mysterious
Nomad, you're the spirit that men fear in us
Nomad, you're the rider of the desert sands
No man ever understood your genius""")

with open('the-nomad.txt') as f:
    rader = f.read()

frekvens = {}

rader.replace('\n', ' ')
rader.replace(',', '')

for x in rader.split():
    x = x.lower()
    if x not in frekvens:
        frekvens[x] = 1
    else:
        frekvens[x] += 1

vanligast = x

for x in frekvens:
    if frekvens[x] > frekvens[vanligast]:
        vanligast = x

print("9. Ordet", vanligast, 'är vanligast')

with open('the-nomad.txt') as f:
    rader = f.readlines()
for i in range(len(rader)):
    rader[i] = rader[i].strip() # Plockar bort alla '\n'

längder = [len(rader[i]) for i in range(len(rader))]
print("10. Den längsta raden är:", rader[längder.index(max(längder))])

antal = 0
for rad in rader:
    try:
        if rad[-1] == 'n':
            antal += 1
    except IndexError:
        continue
print("11.", antal,"slutar på ett n")

####################
## ÖVNINGAR 12-16 ##
####################

"""
12. Läs in filen filhantering-3-c.txt
13. Använd funktionen least_square för att hitta
    den linjära funktion som passar bäst till datan
14. Vad är y-värdet då x är 461?
15. Vad borde y-värdet vara då x är 5?
16. Vad borde y-värdet vara då x är 6123?
"""


def least_square(x, y):
    """
    x: lista med tal
    y: list amed tal
    ---
    Genererar en linjär trendlinje och skickar
    tillbaka koefficienterna k & m
    """
    assert len(x) == len(y) # Kontrollerar att de är lika långa
    n = len(x) # Längden på listan
    xy = 0 # Summan av alla x*y
    x2 = 0 # Summan av alla x^2
    for i in range(n): # Gå igenom alla tal
        xy += x[i]*y[i] # Summera produkterna
        x2 += x[i]*x[i] # Summera kvadraterna
    k = (n*xy-sum(x)*sum(y))/(n*x2-sum(x)**2) # Beräkna k

    x_mean = sum(x)/n # Medel x
    y_mean = sum(y)/n # Medel y

    m = y_mean-x_mean*k # m-värdet

    return [k, m]

with open('filhantering-3-c.txt') as f:
    rader = f.readlines()
    
x = []
y = []
for rad in rader:
    aa = rad.split(';')
    x.append(int(aa[0]))
    y.append(int(aa[1]))

k, m = least_square(x,y)
print(f"13. y={k}x+{m}")

for i in range(len(x)):
    if x[i] == 461:
        print("14. f(461) =", y[i])
        break

print('15. f(5) =', 5*k+m)
print('16. f(6123) =', 6123*k+m)
