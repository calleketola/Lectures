from turtle import *
from math import *


speed(0)
def rita_rektangel(höjd, bredd):
    forward(bredd)
    left(90)
    forward(höjd)
    left(90)
    forward(bredd)
    left(90)
    forward(höjd)
    left(90)

    write("Area: "+str(höjd*bredd))

def draw_rectangle(höjd, bredd):
    for i in range(4):
        if i%2 == 0:
            forward(bredd)
        else:
            forward(höjd)
        left(90)
    write("Area: "+str(höjd*bredd))

def star(n, length=100):
    if n%2==1:
        angle = 180-180/n
        for i in range(n):
            fd(length)
            rt(angle)
    elif n%4==0:
        angle = 180-360/n
        for i in range(n):
            fd(length)
            rt(angle)
    else: # n%4==2 i.e. 6, 10, 14...
        if (n//2)%2==1:
            angle = 180-180/(n//2)
        else:
            angle = 0
        for i in range(n//2):
            fd(length)
            rt(angle)
        pu()
        rt(90)
        fd(length*sin(pi/n))
        lt(90)
        pd()
        for i in range(n//2):
            fd(length)
            lt(angle)
    
        

star(14,300)

##############
## ÖVNING 1 ##
##############

## Använd funktionen rita_rektangel för att
## rita en rektangel som är 100 steg hög och
## 150 steg bred.
        
#rita_rektangel(200,300)

##############
## ÖVNING 2 ##
##############

## Använd funktionen draw_rectangle för att
## rita en kvadrat med sidorna 200x200.


##############
## ÖVNING 3 ##
##############

## Varför blir resultatet av att köra
## rita_rektangel(50,75) det samma som
## att köra draw_rectangle(50,75)?

##############
## ÖVNING 4 ##
##############

## Skapa funktionen rita_kvadrat(sida)
## som bara behöver ta emot ett värde
## för att rita ut en kvadrat.
