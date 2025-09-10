def dela(a,b):
    return a/b

    
while True:
    tal = input("Skriv två heltal ")
    tal = tal.split()
    svar = dela(int(tal[0]),int(tal[1]))
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
    return colours[x]



