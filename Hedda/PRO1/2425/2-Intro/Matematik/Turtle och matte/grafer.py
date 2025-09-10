import turtle as t
import math
import playsound as ps

skala = 10
EXPLODING = True

# Det här är lite funktioner jag använder längre ner
# så att man inte behöver göra omvandlingen mellan
# grader och radianer.

def sin(x):
    return math.sin(x)
def cos(x):
    return math.cos(x)
def tan(x):
    return math.tan(x)

def derivata(f, x):
    h = 2**(-10)
    return (f(x+h)-f(x))/h

screen = t.Screen()
image = 'explosion.gif'
screen.addshape(image)
e = []

ninja = t.Turtle() # Den här skapar koordinatsystemet
ninja.hideturtle() # Det är en ninja turtle!
ninja.speed(0)

t.hideturtle()

# x-axeln

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

# Nu kommer lite matematiska funktioner

def f1(x):
    return sin(x)*10*skala
def f2(x):
    return cos(x)*10*skala
def f3(x):
    return sin(x)**2*10*skala
def f4(x):
    return cos(x)**2*10*skala

def f5(x):
    return x*(x-250)*(x+200)/(2*10**3)

def f6(x):
    return x**2



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

i = 0
while i < antal_paddor:
    turtles[i].pd()
    i += 1
i = -400

# Rita graferna
while i < 400:
    x = i/skala
    # Det här flyttar paddorna till sin nya position
    turtles[0].setpos(i, f1(x/2))
    turtles[1].setpos(i, f2(x/2))
    turtles[2].setpos(i, -f1(x/2))
    turtles[3].setpos(i, -f2(x/2))

    if EXPLODING:
        # This is where the magic happens
        j = 0
        while j < antal_paddor:
            k = 0
            while k<j:
                # Om de överlappar: EXPLODERA!
                s = 5
                if int(turtles[j].ycor()/s) == int(turtles[k].ycor()/s):
                    e.append(t.Turtle())
                    e[-1].penup()
                    e[-1].speed(0)
                    e[-1].setpos(i, turtles[j].ycor())
                    e[-1].shape(image)
                    ps.playsound('explosion.wav', False)
                k += 1
            j += 1
    i+=1








