###############
## ÖVNING 01 ##
###############

"""
Skriv en while-loop som skriver ut
alla tal mellan 0 och 13.
"""
i = 0
while i <= 13:
    print(i)
    i += 1

###############
## ÖVNING 02 ##
###############

"""
Skriv en for-loop som skriver ut
alla tal mellan 0 och 13.
"""

for i in range(14):
    print(i)


###############
## ÖVNING 03 ##
###############

"""
Skriv en while-loop som skriver ut
var tredje tal från 2 till 30.
"""

i = 2
while i < 30:
    print(i)
    i += 3

###############
## ÖVNING 04 ##
###############

"""
Skriv en for-loop som skriver ut
var tredje tal från 2 till 30.
"""
for i in range(2,30,3):
    print(i)

###############
## ÖVNING 05 ##
###############

"""
Skriv en while-loop som skriver ut
talen 10, 9, ... -9, -10.
"""
i = 10
while i > -11:
    print(i)
    i -= 1

###############
## ÖVNING 06 ##
###############

"""
Skriv en for-loop som skriver ut
talen 10, 9, ... -9, -10.
"""

for i in range(10,-11,-1):
    print(i)

###############
## ÖVNING 07 ##
###############

"""
Skriv en for-loop som ritar ut
följande mönster:
*
**
***
****
*****
******
*******
********
*********
"""
for i in range(1,10):
    print('*'*i)

###############
## ÖVNING 08 ##
###############

"""
Skriv en for-loop som ritar ut
följande mönster:
        *
       ***
      *****
     *******
    *********
   ***********
  *************
 ***************
*****************
       ###       
       ###
"""

for i in range(0, 9):
    print(" "*(8-i)+"*"+"*"*i*2)
print("       ###")
print("       ###")

###############
## ÖVNING 09 ##
###############

"""
Skriv ut julgranskulor också
"""
import random

for i in range(0, 9):
    print(" "*(8-i),end="")
    print('*', end="")
    for j in range(i*2-1):
        if random.randint(1,7) == 1:
            print('O', end="")
        else:
            print('*',end="")
    if (i > 0):
        print('*')
    else:
        print()
print("       ###")
print("       ###")

###############
## ÖVNING 10 ##
###############

"""
Lägg till julgransljus
"""
import random

for i in range(0, 9):
    print(" "*(8-i),end="")
    print('*', end="")
    for j in range(i*2-1):
        r = random.randint(1,7)
        if r == 1:
            print('O', end="")
        elif r == 2:
            print('i', end="")
        else:
            print('*',end="")
    if (i > 0):
        print('*')
    else:
        print()
print("       ###")
print("       ###")

###############
## ÖVNING 11 ##
###############

"""
Skriv ett program som frågar efter
hur många tal man vill multiplicera
och sen tar emot så många tal och
multiplicerar ihop dem. (Gör det
med en for-loop)
"""

n = input("Hur många tal vill du multiplicera? ")
n = int(n)
prod = 1
for i in range(n):
    tal = input(f"Tal {i+1}: ")
    prod *= float(tal)
print(prod)

###############
## ÖVNING 10 ##
###############

"""
Skriv ett program som tar emot en
text och som sen skriver ut varje
tecken på en ny rad.
"""
text = input("Skriv något:\n")
for tecken in text:
    print(tecken)
