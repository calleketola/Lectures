from turtle import *
import math

# Innervinkel: 180*(5-2)/5=180*3/5=36*3=90+18=108
# Yttervinkel: 180-108 = 72

# von Koch

def snöflinga(level=5, length=20):
    pu()
    setpos((-250,0))
    seth(0)
    pd()
    speed(1000)
    von_koch(level, length)
    right(120)
    von_koch(level, length)
    right(120)
    von_koch(level, length)
    right(120)

def von_koch(level= 5,length = 10):
    if level == 0:
        return
    forward(length)
    von_koch(level-1,length/3)
    forward(length)
    left(60)
    forward(length)
    von_koch(level-1, length/3)
    forward(length)
    right(120)
    forward(length)
    von_koch(level-1, length/3)   
    forward(length)
    left(60)
    forward(length)
    von_koch(level-1,length/3)
    forward(length)
    
def kvadratspiral():
    n = 0
    speed(0)
    pu()
    setpos((-300,-100))
    pd()
    while n < 100:
        h = 0
        while h < 4:
            fd(100)
            lt(90)
            h += 1
        pu()
        n += 1
        lt(2*n)
        fd(2*n)
        pd()

def mandelbrot_set():
    tracer(0,0)
    pu()
    screenx, screeny = 800, 600
    complexPlaneX, complexPlaneY = (-2.0, 2.0), (-1.0, 2.0)
    step = 2 
    setup(screenx, screeny)
    pixelToX = (complexPlaneX[1] - complexPlaneX[0])/screenx
    pixelToY = (complexPlaneY[1] - complexPlaneY[0])/screeny
    for px in range(-screenx//2, screenx//2, int(step)):
        for py in range(-screeny//2, screeny//2, int(step)):
            x, y = px * pixelToX, py * pixelToY
            m =  mandelbrot(0, x + 1j * y)
            if not math.isnan(m.real):
                colour = [abs(math.sin(m.imag)) for i in range(3)]
                color(colour)
                dot(2.4, colour)
                goto(px, py)
        update()

def mandelbrot(z , c , n=20):
    if abs(z) > 10 ** 12:
        return float("nan")
    elif n > 0:
        return mandelbrot(z ** 2 + c, c, n - 1) 
    else:
        return z ** 2 + c
        
    
    
