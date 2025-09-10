##############
## ÖVNING 1 ##
##############

"""
Skriv ett program som frågar efter ett
lösenord två gånger. Om man skriver in
två olika saker så ska programmet fråga
igen tills de två lösenorden stämmer
överens. Som när man skapar konton på
olika ställen.
"""

ok = False
while not ok:
    password1 = input("Type password:\n")
    if password1 == input("Retype password:\n"):
        ok = True
    else:
        print("Passwords must match")


##############
## ÖVNING 2 ##
##############

"""
Skriv en kod som tar emot två tal och
kollar om båda två talen är udda.
"""

tal1 = input("Number 1: ")
tal2 = input("Number 2: ")
tal1, tal2 = float(tal1), float(tal2) # Sparar plats
if tal1%2 == 1 and tal2%2 == 1:
    print("Both are odd")
else:
    print("Both are not odd")


##############
## ÖVNING 3 ##
##############

"""
Skriv en kod som tar emot ett tal och
kollar hur långt talet är. Om man inte
har skrivit ett tal, med siffror, så
ska programmet fråga tills man svarar
med bara siffror.
"""

asking = True
while asking:
    number = input("Write a number: ")
    if number.isnumeric():
        print("The number", number, "is", len(number), "long")
        asking = False
    else:
        print("Please write a number")

##############
## ÖVNING 4 ##
##############

"""
Skriv en kod som tar emot tio tal och
skriver ut medelvärdet av talen.
"""
s = 0
n = 10
for i in range(n):
    s += float(input(f"Nuber {i+1}: "))
print("The mean of the numbers is", s/n)

##############
## ÖVNING 5 ##
##############

"""
Man kan komma åt enskilda tecken i en
sträng på följande vis:
a = "Hej på dig"
print(a[0], a[1])
Första tecknet ligger på plats 0

Skriv en kod som tar emot en text och
skriver första bokstaven i texten.
"""

text = input("Write something will you? ")
print(text[0])


##############
## ÖVNING 6 ##
##############

"""
Skriv en kod som tar emot en text och
skriver ut varje bokstav på en ny rad.
"""

text = input("Write something beautiful.\n")
for i in range(len(text)):
    print(text[i])
# Alternativ lösning
#for x in text:
#    print(x)


##############
## ÖVNING 7 ##
##############

"""
Skriv en kod som tar emot text och
skriver ut hur många gånger bokstaven
'e' förekommer i texten
"""

text = input("Write again\n")
num_e = 0
for i in range(len(text)):
    if text[i].lower() == 'e':
        num_e += 1
print("e appeared", num_e, "times")


##############
## ÖVNING 8 ##
##############

"""
Skriv en kod som tar emot en text och
räknar hur många ord som förekommer i
texten.
"""

text = input("Write several words\n")
words = 1
for i in range(len(text)):
    if text[i] == ' ':
        words += 1
print("Number of words might be", words)
# Alternativ lösning
#words = text.split()
#print(len(words))

##############
## ÖVNING 9 ##
##############

"""
Skriv en kod som tar emot ett text och
kollar om första bokstaven är stor eller
liten.
"""

text = input("Write a word\n")
if text[0].lower() == text[0]:
    print("Lowercase")
elif text[0].upper() == text[0]:
    print("Uppercase")

###############
## ÖVNING 10 ##
###############

"""
Skriv en kod som tar emot ett tal och
kollar hur många gånger det går att dela
på två.
"""

number = input("Write an integer: ")
num = int(number)
divisions = 0
while num%2 == 0:
    num = num//2 # Håller kvar det som heltal
    divisions += 1
print(number, "can be divided by two", divisions, "times")

###############
## ÖVNING 11 ##
###############

"""
Skriv en kod som tar emot fyra ord och
kollar om alla börjar med en vokal
"""

word1 = input("Write word 1: ")
word2 = input("Write word 2: ")
word3 = input("Write word 3: ")
word4 = input("Write word 4: ")

vowels = 'aeiouyåäö'

if (word1[0].lower() in vowels and
    word2[0].lower() in vowels and
    word3[0].lower() in vowels and
    word4[0].lower() in vowels):
    print("All began with a vowel")

# Alternativ lösning
#words = []
#for i in range(4):
#    if not input(f"Write word {i+1}: ")[0].lower in vowels:
#        break
#else:
#    print("All began with a vowel")
