###############
## UPPGIFT 1 ##
###############

i = 0
while i < 100:
    print(i, end=" ")
    if i%2==0:
        i+=3
    else:
        i = i + 1   # Samma sak som i+=1
print()
###############
## UPPGIFT 2 ##
###############
"""
svar = 0
while svar != '3' and svar != '2':
    svar = input("1. Skriv ett bra tal: ")
svar = 0
while svar != 3 or svar != 2:
    svar = int(input("2. Skriv ett bra tal: "))
"""
###############
## UPPGIFT 3 ##
###############

##ålder = input("Hur gammal är du? ")
##while ålder.isnumeric() == False:
##    print("Man kan bara vara helår gammal.")
##    ålder = input("Hur gammal är du? ")
##print("Du är", ålder, "år gammal.")

###############
## UPPGIFT 4 ##
###############

i = 1
j = 1
print(j, end=", ")
while j <= 100:
    print(j, end = ", ")
    k = j
    j = i+j
    i = k
print()

i = 1
j = 1
print(j, end=", ")
while j <= 100:
    print(j, end = ", ")
    i, j = j,i+j
print()
###############
## UPPGIFT 5 ##
###############
i = 65
while chr(i-1) != 'Z':
    print(chr(i), end="")
    i += 1
print()

###############
## UPPGIFT 6 ##
###############

svar = input("LÖSENORD: ")
lösen = 'admin'
while svar != '':
    if svar == lösen:
        print('Lösenord accepterat')
        break
    else:
        print("Fel lösenord")
    svar = input("LÖSENORD: ")
else:
    print("Inloggning avbruten")
