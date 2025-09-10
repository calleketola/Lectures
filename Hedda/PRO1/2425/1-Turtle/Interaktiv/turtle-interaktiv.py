from turtle import *


# Funktioner som gör att sköldpaddan vänder på sig
def upp():
    setheading(90)

def ner():
    setheading(-90)

def vänster():
    setheading(180)

def höger():
    setheading(0)

shape('turtle')
speed(0)
#penup() # Gör så att vi inte ritar

spelar = True

while spelar == True:
    # Lyssnar efter knapptryck
    listen()
    # Kod som vilken funktion som ska köras när vi
    # trycker på en knapp
    onkey(upp, 'Up')
    onkey(ner, 'Down')
    onkey(vänster, 'Left')
    onkey(höger, 'Right')

    # Kod som får sköldpaddan att flytta på sig
    forward(1)
