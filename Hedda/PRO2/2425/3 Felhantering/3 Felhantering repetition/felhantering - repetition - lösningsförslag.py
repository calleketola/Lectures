##############
## ÖVNING 1 ##
##############

## Stoppa användaren från att kunna
## krascha programmet genom att skriva
## in nonsens

try:
    ålder = int(input("Hur gammal är du? "))
    if ålder < 20:
        print("Hur går det i skolan?")
    else:
        print("Du är fan gammal!")
except (ValueError, NameError):
    print("Du skrev inget heltal")


##############
## ÖVNING 2 ##
##############

## Stoppa programmet från att krascha
## om användaren råkar skriva ett för
## stort tal

namn = input("Vad heter du? ")
lista = list(namn)
try:
    gissning = int(input('På vilken plats finns det ett "l"?'))

    if lista[gissning] == "l":
        print("Bra gjort!")
    else:
        print("Nope!")
except ValueError:
    print("Du skrev inte ett heltal")
except IndexError:
    print("Du skrev ett för stort tal")

##############
## ÖVNING 3 ##
##############

## Stoppa programmet från att krascha
## tänk på att det kraschar även på 0

try:
    a = float(input("Tal 1: "))
    b = float(input("Tal 2: "))

    c = a/b
except ValueError:
    print("Båda talen måste vara heltal")
except ZeroDivisionError:
    print("Det andra talet får inte vara 0")


print(f"{a}/{b}={c}")

##############
## ÖVNING 4 ##
##############

## Stoppa programmet från att krascha
try:
    start = float(input("Tal 1: "))
    stop = float(input("Tal 2: "))
    step = float(input("Tal 3: "))
except ValueError:
    start = 1
    stop = 10
    step = 1

summa = 0

x = start
while x < stop:
    tal = 1/x
    summa += tal
    x += step

print(summa)



