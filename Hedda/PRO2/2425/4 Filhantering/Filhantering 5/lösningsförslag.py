##with open("rep-data-1.txt") as f:
##    tal = f.readlines() # Läser in varje rad
##
##for i in range(len(tal)):
##    tal[i] = int(tal[i]) # Konverterar varje rad till tal
##
##summa = sum(tal) # Sparar summan
##medel = summa/len(tal) # Räknar ut medel
##
##with open("rep-data-1.txt", "a") as f: # Öppnar filen igen
##    f.write(str(summa)) # Skriver in summan
##    f.write('\n') # Skriver in en ny rad
##    f.write(str(medel)) # Skriver in medel
##
##print(summa, medel)

with open("rep-data-2.txt") as f:
    rader = f.readlines()

störst = []

for i in range(len(rader)):
    rader[i] = rader[i].split()
    störst.append(max(rader[i]))

print(" ".join(störst))


with open("rep-data-2.txt", 'a') as f:
    f.write('\n')
    for i in range(len(störst)):
        f.write(störst[i])
        f.write(" ")













    
