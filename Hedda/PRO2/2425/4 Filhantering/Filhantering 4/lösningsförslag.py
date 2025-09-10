# Fil 1
##
##with open("data1.txt") as f:
##    tal = f.readlines()
##
### Skriv ut antalet tal
##n = len(tal)
##
##print("Antal tal:", n)
##
### Skriv ut summan av alla tal
##for i in range(n):
##    tal[i] = float(tal[i])
##print("Summan av alla tal:", sum(tal))
##m = sum(tal)/n
### Skriv ut medlevärdet av talen
##print("Medelvärdet:", m)
##
### Beräkna standardavvikelsen
##s = 0
##for i in range(n):
##    s += (tal[i]-m)**2
##s = s/n
##s = s**0.5
##print("Standardavvikelsen är:", s)

# Fil 2
##with open("data2.txt") as f:
##    data = f.read()
##
##data = data.split()
##
##for i in range(len(data)):
##    data[i] = data[i].replace("'","")
##    data[i] = data[i].replace(",","")
##
##for word in data:
##    print(word)
##
##for word in data:
##    print(word, end=" ")


# Fil 3
with open("data3.txt") as f:
    data = f.readlines()

for i in range(len(data)):
    rad = data[i].strip()
    
    rad = rad.replace('"', '')
    rad = rad.replace('{', '')
    rad = rad.replace('}', '')

    rad = rad.split(",")

    rad[0] = rad[0].split(':')
    rad[1] = rad[1].split(':')

    rad = {rad[0][0]: int(rad[0][1]),
           rad[1][0]: int(rad[1][1])}

    data[i] = rad
    
print(len(data))

summa = 0
for i in range(len(data)):
    summa += data[i]['height']
print(summa)


















