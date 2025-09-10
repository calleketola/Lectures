import random

##data = [random.random() for _ in range(1024)]
##
##with open("data1.txt", 'w') as f:
##    for row in data:
##        f.write(str(row))
##        f.write('\n')


##data = []
##
##texten = """Vårvindar friska
##Leka och viska,
##Lunderna kring, likt älskande par,
##Strömmarna ila,
##Finna ej vila
##Förr’n ner i djupet störtvågen far.
##Klaga, mitt hjärta, klaga! – O, hör,
##Vallhornets klang bland klipporna dör!
##Strömkarlen spelar,
##Sorgerna delar
##Vakan kring berg och dal."""
##
##data = texten.split('\n')
##for i in range(len(data)):
##    data[i] = data[i].split()
##
##with open("data2.txt", 'w') as f:
##    for row in data:
##        f.write(str(row))
##        f.write('\n')

data = []

for i in range(16):
    text = '{'
    text += f'"id":{i},'
    text += f'"height":{random.randint(150, 210)}'
    text += '}\n'
    data.append(text)

data[-1]= data[-1].strip()

with open("data3.txt", 'w') as f:
    for row in data:
        f.write(row)
