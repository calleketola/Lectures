def least_square(x, y):
    assert len(x) == len(y)
    n = len(x)
    xy = 0
    x2 = 0
    for i in range(len(x)):
        xy += x[i]*y[i]
        x2 += x[i]*x[i]
    k = (n*xy-sum(x)*sum(y))/(n*x2-sum(x)**2)

    x_mean = sum(x)/n
    y_mean = sum(y)/n

    m = y_mean-x_mean*k

    return k, m

import random
"""
x = [i for i in range(1,1000,20)]
y = [3*a+random.randint(-15,15) for a in x]

with open('filhantering-3-c.txt', 'w') as f:
    for i in range(len(x)):
        f.write(str(x[i])+';'+str(y[i])+'\n')
"""
"""
with open('filhantering-3-a.txt', 'w') as f:
    for i in range(2**9):
        f.write(str(random.randint(-1000000,1000000))+'\n')
"""
