with open('filhantering-3-a.txt') as f:
    rader = f.readlines()

for i in range(len(rader)):
    rader[i] = int(rader[i])

störst = max(rader)
print("Störst:",störst)
# Talet närmast noll
minst = abs(rader[0])
for i in range(len(rader)):
    if abs(rader[i]) <  abs(minst):
        minst = rader[i]
print('Närmast noll:', minst)
# Medel
summa = sum(rader)
medel = summa/len(rader)
print("Medel:", medel)

sorterad = rader.sort()
median = (rader[len(rader)//2]+rader[len(rader)//2+1])/2
print(median)
