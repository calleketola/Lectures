import matplotlib.pyplot as plt

def f(x):
    y = x**2+3*x-1/x
    return y

x = []
for i in range(1,2**8):
    x.append(i/2**4)

y = []

#for i in range(len(x)):
#    y.append(f(x[i]))
for a in x:
    y.append(f(a))


plt.xkcd()
plt.plot(x,y,'r')
plt.xlabel('hej')
plt.show()
