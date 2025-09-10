i = 0
j = 0

while i < 10:
    j = 0
    while j < 10:
        print(i,j)
        if i == j:
            break
        j += 1
    i += 1
