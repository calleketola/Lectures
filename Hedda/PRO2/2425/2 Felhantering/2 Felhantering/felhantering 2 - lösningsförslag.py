def dela1(a,b):
    assert b != 0, "Dela inte med noll"
    return a/b

def dela2(a,b):
    if b == 0:
        raise ZeroDivisionError("b får inte vara noll")
    return a/b
    
while True:
    tal = input("Skriv två heltal ")
    tal = tal.split()
    try:
        svar = dela2(int(tal[0]),int(tal[1]))
    except ZeroDivisionError:
        svar = dela2(int(tal[0]),1)
    except IndexError:
        print("Du skrev för få tal")
        continue
        
    print("Kvoten mellan "+ tal[0] + " och " + tal[1] + " är " + str(svar))

    if tal[0] == '0':
        break

##############
## Övning 4 ##
##############

"""
Se till att funktionen list_delare inte accepterar
listor som har färre än två element 
"""

def list_delare(x):
    assert len(x) >= 2
    return x[:len(x)//2], x[len(x)//2:]

##############
## Övning 5 ##
##############

"""
Funktionen färgväljare har bara 8 inlagda
färger. Se till att programmet lyfter ett
felmeddelande, utan att krascha om man anger
en färg som inte finns.
"""

def färgväljare(x):
    colours = {'red': '#FF0000', 'orange': '#FFA5000',
               'yellow': '#FFFF00', 'green': '#00FF00',
               'blue': '#0000FF', 'purple': '#800080',
               'white': '#FFFFFF', 'black': '#000000'}
    try:
        return colours[x]
    except KeyError:
        print(f"{x} not in colour list")

while True:
    try:
        tal = int(input("Ange ett heltal: "))
        svar = tal**2
        print("Kvadraten på " + str(tal) + " är " + str(svar))
    except(KeyboardInterrupt):
        print("Du försökte döda programmet")
        #quit()
    except(EOFError):
        print("Programmet avbröts i förtid")
        quit()
    except(ValueError):
        print("Du måste skriva in heltal")
    if tal == 0:
        break

