import matplotlib.pyplot as plt # Importerar grafverktyget
import math

def f(x):
    return math.log(x)
def g(x):
    return math.sqrt(x)
def h(x):
    return 1/x

x = []
y1 = []
y2 = []
y3 = []

n = 7
for i in range(1, 2**n):
    x.append(i)
    y1.append(f(x[-1]))
    y2.append(g(x[-1]))
    y3.append(h(x[-1]))
    




plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Tre stycken funktioner')
plt.legend(['f(x)=ln(x)','g(x)=sqrt(x)', 'h(x)=1/x'])
plt.grid()
plt.show()

