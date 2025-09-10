"""
Använd turtle för att rita ut en gran
"""

import turtle

turtle.speed(0)


def make_triangle(n):
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(50*n)
        turtle.left(120)
    turtle.end_fill()

def setup_triangle(n):
    turtle.forward(25*(n-1))

    turtle.left(90)
    turtle.forward(25*(n-1))
    turtle.right(90)

    turtle.right(120)
    turtle.forward(50*n)
    turtle.left(120)

def draw_foot():

    turtle.forward(25*3-5)
    turtle.right(90)
    
    turtle.color('brown')

    turtle.begin_fill()
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(25)
    turtle.end_fill()

def setup_star():
    turtle.pu()

    turtle.setposition(0,55)
    turtle.setheading(0)

    turtle.pd()
    

def draw_star():
    turtle.color('yellow')

    turtle.begin_fill()

    for i in range(5):
        turtle.forward(50)
        turtle.right(180-180/5)

    turtle.end_fill()

turtle.color('green')

n = 1

make_triangle(n)

n+=1

setup_triangle(n)
make_triangle(n)

n+=1

setup_triangle(n)
make_triangle(n)


draw_foot()

setup_star()
draw_star()



