##############
## Övning 1 ##
##############

with open('sonnet-xviii.txt') as f:
    text = f.read()
print(text)


##############
## Övning 2 ##
##############

lärare = ['Emma', 'Johanna', 'Ebba', 'Calle', 'Ulf',
          'Enrique', 'Johannes', 'Henrik', 'Lone',
          'Joakim', 'Linda']

with open('teknik.txt') as f:
    tek = f.readlines()
for i in range(len(tek)):
    tek[i] = tek[i].strip()
    
saknas = []
for namn in lärare:
    if namn not in tek:
        saknas.append(namn)
with open('teknik.txt', 'a') as f:
    for namn in saknas:
        f.write(f'\n{namn}')
        print("Lade till", namn)

# Kortare lösning, om man vet vem som skanas redan:
#with open('teknik.txt', 'a') as f:
#    f.write('\n')
#    f.write('Emma')
    
##############
## Övning 4 ##
##############

with open('text-1.txt') as f:
    rader = f.readlines()
print("Filen innehåller", len(rader), "rader")

##############
## Övning 5 ##
##############

max_längd = 0
pos = 0
for rad in range(len(rader)):
    if len(rader[rad].strip()) > max_längd:
        pos = rad
print("Ordet", rader[pos], "är längst med", max_längd, "tecken")

##############
## Övning 6 ##
##############

antal_i = 0
for rad in rader:
    for bokstav in rad:
        if bokstav.lower() == 'i':
            antal_i += 1
print("Det finns", antal_i, 'i:n')

##############
## Övning 7 ##
##############

startbokstäver = {}
for rad in rader:
    if rad[0] in startbokstäver:
        startbokstäver[rad[0]] += 1
    else:
        startbokstäver[rad[0]] = 1

vanligast = 'a'
for bokstav in startbokstäver:
    if startbokstäver[bokstav] > startbokstäver[vanligast]:
        vanligast = bokstav
print(vanligast, 'är den vanligaste startbokstaven')

##############
## Övning 8 ##
##############


with open('data-1.csv') as f:
    rader = f.readlines()

summa = 0
produkter = []
for rad in range(len(rader)):
    rader[rad] = rader[rad].split()
    produkter.append(1)
    for kol in range(len(rader[rad])):
        rader[rad][kol] = float(rader[rad][kol])
        produkter[-1] *= rader[rad][kol]
    summa += produkter[-1]
print(summa)
