###############
## UPPGIFT 1 ##
###############
"""
Skriv en kod som skriver ut alla tal från 0 till 100
"""

i = 0
while i < 101:
    print(i)
    i += 1

input("Uppgift 1 klar...")

###############
## UPPGIFT 2 ##
###############
"""
Skriv en kod som skriver ut talen 0.1, 0.2, 0.3 ... 1.0
"""
i = 0
while i <= 1:
    print(i)
    i+=.1

input("Uppgift 2 klar...")

###############
## UPPGIFT 3 ##
###############
"""
Skriv en kod som skriver ut varannat tal från 10 till -10.
"""
i = 10
while i >= -10:
    print(i)
    i -= 2

input("Uppgift 3 klar...")

###############
## UPPGIFT 4 ##
###############
"""
Skriv ut ettan till tolvans gångertabell.
"""

i = 1
while i < 13:
    j = 1
    while j < 13:
        print(i,j,i*j)
        j += 1
    print("----")
    i += 1

input("Uppgift 4 klar...")
###############
## UPPGIFT 5 ##
###############
"""
Skriv en bit kod som skriver ut Fibonacci-serien upp till det hundrade talet
"""
i = 2
a = 1
b = 1
print(a)
print(b)
while i < 100:
    temp = a
    a = a+b
    b = temp
    print(a)
    i += 1
    
input("Uppgift 5 klar...")

###############
## UPPGIFT 6 ##
###############
"""
Skriv en loop som skriver ut A--Z (tips kolla upp \href{https://docs.python.org/3/library/functions.html\#chr}{chr()})
"""
i = 65
while i < 91:
    print(chr(i))
    i += 1

input("Uppgift 6 klar...")

###############
## UPPGIFT 7 ##
###############
"""
Skriv ett program som frågar efter ett lösenord. Om användaren skriver admin ska det svara Lösenord accepterat annars ska det fråga efter lösenordet på nytt.
"""
svar = ""
while svar != "admin":
    svar = input("Skriv ett lösenord: ")
    if svar == "admin":
        print("Lösenord accepterat")
    else:
        print("Fel lösenord")

input("Uppgift 7 klar...")

###############
## UPPGIFT 8 ##
###############
"""
Skriv ett program som frågar efter:
▶ Lånebelopp
▶ Räntesats
▶ Amortering/år
Och som sen skriver ut:
▶ Tid för att betala tillbaka lånet
▶ Totalt betalad ränta
Ex:
Hur mycket ska du låna? 2500000
Vad är räntesatsen (i %)? 2
Hur mycket ska du amortera ? 60000
Det kommer att ta dig 42 år att betala tillbaka lånet
Du kommer att ha betalat 1066800 kr i ränta
"""
lånebelopp = input("Hur mycket ska du låna? ")
räntesats = input("Vad är räntesatsen (i %) ")
lånebelopp = int(lånebelopp)
räntesats = float(räntesats)

mini_amortering = 0.02*lånebelopp # Detta är lite extra

amortering = input("Hur mycket ska du amortera (minsta lagliga gräns är "
                   + str(mini_amortering)+ ": ")
amortering = int(amortering)
#tid = lånebelopp/amortering

lån_kvar = lånebelopp
betald_ränta = 0
år = 0
while lån_kvar > 0:
    betald_ränta += räntesats/100*lån_kvar
    lån_kvar -= amortering
    år += 1
print("Det kommer att ta dig", år, "att betala tillbaka lånet")
print("Du kommer att ha betalat", betald_ränta, "kr i ränta")
print("Det är", betald_ränta/lånebelopp, "gånger mer än du lånade")
