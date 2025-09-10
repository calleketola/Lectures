###############
## UPPGIFT 1 ##
###############

x = input("Tal 1 = ")
y = input("Tal 2 = ")
z = input("Tal 3 = ")

x = float(x)
y = float(y)
z = float(z)

if x>y:	            # Om x större än y
    print("x är större än y")
if y > x:	    # Om y större än x
    print("y är större än x")
if z > y:	    # Om z större än y
    print("z är större än y :O")
    if z == 2*x:    # Om z dubbelt så stor som x
        print("z är dubbelt så stort som x!")
print("Det var kul!")

###############
## UPPGIFT 2 ##
###############

if x==y or x==z or y==z:
    print("Två av talen är lika")

###############
## UPPGIFT 3 ##
###############

if x==y and y==z: # x == y == z 
    print("Alla tre talen är lika")

###############
## UPPGIFT 4 ##
###############

namn = input("Skriv ett namn")

if namn == 'Julius Caesar':
    print("Ave Caesar")

###############
## UPPGIFT 5 ##
###############

namn = input("Skriv ett namn")

if namn.lower() == 'julius caesar':
    print("Ave Caesar")

###############
## UPPGIFT 6 ##
###############

a = input("Skriv 1 eller 0: ")
b = input("Skriv 1 eller 0: ")
a,b = int(a), int(b)

if a == 1 and b == 0:
    print("Sant")
if a == 0 and b == 1:
    print("Sant")
if a == 1 and b == 1:
    print("Falskt")
if a == 0 and b == 0:
    print("Falskt")

###############
## UPPGIFT 7 ##
###############
if a != b:
    print("Sant")
else: # if a == b:
    print("Falskt")










    
