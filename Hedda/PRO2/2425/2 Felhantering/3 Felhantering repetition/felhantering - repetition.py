##############
## ÖVNING 1 ##
##############

## Stoppa användaren från att kunna
## krascha programmet genom att skriva
## in nonsens

ålder = int(input("Hur gammal är du? "))
if ålder < 20:
    print("Hur går det i skolan?")
else:
    print("Du är fan gammal!")

##############
## ÖVNING 2 ##
##############

## Stoppa programmet från att krascha
## om användaren råkar skriva ett för
## stort tal

namn = input("Vad heter du? ")
lista = list(namn)
gissning = int(input('På vilken plats finns det ett "l"?'))

if lista[gissning] == "l":
    print("Bra gjort!")
else:
    print("Nope!")

##############
## ÖVNING 3 ##
##############

## Stoppa programmet från att krascha
## tänk på att det kraschar även på 0

a = float(input("Tal 1: "))
b = float(input("Tal 2: "))

c = a/b

print(f"{a}/{b}={c}")

##############
## ÖVNING 4 ##
##############

## Stoppa programmet från att krascha

start = float(input("Tal 1: "))
stop = float(input("Tal 2: "))
step = float(input("Tal 3: "))

summa = 0

x = start
while x < stop:
    tal = 1/x
    summa += tal
    x += step

print(summa)



