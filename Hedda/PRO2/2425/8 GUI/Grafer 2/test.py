from matplotlib import pyplot as plt
import numpy as np

x_data = np.linspace(-np.pi, np.pi, 100)
y_data = [np.sin(x) for x in x_data]

plt.ion()
fig = plt.figure() # Skapar en figur (typ fönstret)
ax = fig.add_subplot(111) # Lägger till ett ritområde
ax.plot(x_data, y_data) # Rita grafen
line = ax.get_lines()[0]
fig.show() # Visa fönstret med grafen
t = np.pi
i = 1
while i < 100:
    t += np.pi/10
    x_data = np.append(x_data, t)
    line.set_xdata(x_data)
    line.set_ydata(np.array([np.sin(x) for x in x_data]))
    ax.set_autoscaley_on(True)
    ax.set_xlim(min(x_data), max(x_data))
    fig.canvas.draw()
    if i <= 20:
        plt.savefig(f'append-{i}.png')
    i += 1
    
