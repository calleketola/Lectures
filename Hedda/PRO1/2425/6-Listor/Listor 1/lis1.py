"""
lista8 = ['n','i',' ','t','a','l','a','r',' ','b','r','a',' ','l','a','t','i','n']

i = 0
while i < len(lista8):
    summa = 0
    j = 0
    while j < len(lista8):
        if lista8[i] == lista8[j]:
            summa += 1
        j += 1
    print(f"{lista8[i]} förekommer {summa} gång(er)")
    i += 1
    
lista5 = [3,6,1,1,3,5,4,3,9,10,0,6,8,7,3]

i = 0
while i < len(lista5):
    if lista5[i]%2==1: # Udda
        lista5.pop(i)
    else:
        i += 1
print(lista5)
"""
import random

a = []


for i in range(5):
    a.append([],)
    for j in range(5):
        a[i].append(random.randint(1, 5))
        


for rad in a :
   
    print(*rad,"=", sum(rad))
