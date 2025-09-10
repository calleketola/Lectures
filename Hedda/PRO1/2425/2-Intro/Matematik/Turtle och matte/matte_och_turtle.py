import turtle as t
import math

skala = 10

# Bygg koordinatsystemet

ninja = t.Turtle() # Den här skapar koordinatsystemet
ninja.hideturtle() # Det är en ninja turtle!
ninja.speed(0)
t.hideturtle()

ninja.setpos(-400, 0)
ninja.setpos(400, 0)

# pil
ninja.begin_fill()
ninja.lt(180-45)
ninja.fd(10)
ninja.lt(180-45)
ninja.fd(200**.5)
ninja.lt(180-45)
ninja.fd(10)
ninja.end_fill()

# y-axeln
ninja.pu()
ninja.seth(90)
ninja.setpos(0,-400)
ninja.pd()
ninja.setpos(0,400)

# pil
ninja.begin_fill()
ninja.lt(180-45)
ninja.fd(10)
ninja.lt(180-45)
ninja.fd(200**.5)
ninja.lt(180-45)
ninja.fd(10)
ninja.end_fill()

# siffror
ninja.pu()
# x-axeln
i = -400
while i <= 400:
    ninja.setpos(i, -20)
    ninja.write(round(i/skala,2))
    i += 50

# y-axeln
i = -400
while i <= 400:
    ninja.setpos(-20, i)
    ninja.write(round(i/skala,2))
    i += 50

# Nu är koordinatsystemet utritat!

def f1(x):
    y = 5*x-30
    return y
def f2(x):
    y = 1/2*x**2-20
    return y


# Här skapar jag en hög med sköldpaddor som
# ska rita ut mina grafer
turtles = []
antal_paddor = 4
i = 0
while i < antal_paddor:
    turtles.append(t.Turtle())
    turtles[i].speed(0)
    i += 1
# Vi ger dem färg:
turtles[0].color('blue')    # Leonardo
turtles[1].color('orange')  # Michelangelo
turtles[2].color('purple')  # Donatello
turtles[3].color('red')     # Raphael

# Startpositioner
i = 0
while i < antal_paddor:
    turtles[i].pu()
    turtles[i].shape('turtle')
    i += 1
i = -400
x = i*skala
turtles[0].setpos(i, f1(x/2))
turtles[1].setpos(i, f2(x/2))
turtles[2].setpos(i, -f1(x/2))
turtles[3].setpos(i, -f2(x/2))
# Förbered paddorna för att rita
j = 0
while j < antal_paddor:
    turtles[j].pd()
    j += 1

# Rita graferna
while i < 400:
    x = i/skala
    # Det här flyttar paddorna till sin nya position
    turtles[0].setpos(i, f1(x/2))
    turtles[1].setpos(i, f2(x/2))
    turtles[2].setpos(i, -f1(x/2))
    turtles[3].setpos(i, -f2(x/2))

    i+=1
