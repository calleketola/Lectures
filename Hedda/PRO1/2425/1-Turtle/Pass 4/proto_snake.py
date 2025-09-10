import turtle
import random

def up():
    hungry_turtles[0].setheading(90)
def down():
    hungry_turtles[0].setheading(-90)
def left():
    hungry_turtles[0].setheading(180)
def right():
    hungry_turtles[0].setheading(0)

def update_turtles(turtles):
    for i in range(1, len(turtles)):
        old_pos = turtles[-i-1].pos()
        if abs(old_pos[0] - turtles[-i].pos()[0]) > 25: 
            turtles[-i].setpos(old_pos)
        if abs(old_pos[1] - turtles[-i].pos()[1]) > 25:
            turtles[-i].setpos(old_pos)

# Din lösning behöver vara ovanför den här raden

# Variables
running = True
width = 250
height = 250

# Initialize
hungry_turtles = [turtle.Turtle()]
hungry_turtles[0].shape('turtle')
hungry_turtles[0].penup()

## DEBUG
for i in range(9):
    hungry_turtles.append(turtle.Turtle())
    hungry_turtles[-1].shape('turtle')
    hungry_turtles[-1].penup()
    hungry_turtles[-1].setpos((-25*(i+1),0))

# Food stuff
food = turtle.Turtle()
food.shape('square')
food.penup()
food.setpos((random.randint(-width+20,width-20),
             random.randint(-height+20,height-20)))

# Draw game board
turtle.tracer(0,0)
hungry_turtles[0].setpos((-width,height))
hungry_turtles[0].pendown()
hungry_turtles[0].setpos((width,height))
hungry_turtles[0].setpos((width,-height))
hungry_turtles[0].setpos((-width,-height))
hungry_turtles[0].setpos((-width,height))
# Lägg till de tre andra sidorna
hungry_turtles[0].penup()
hungry_turtles[0].setpos((0,0))
turtle.update()

# Game loop
while running:
    turtle.listen()
    turtle.onkey(up, 'Up')
    turtle.onkey(down, 'Down')
    turtle.onkey(left, 'Left')
    turtle.onkey(right, 'Right')

    # Check if within game board
    if (abs(hungry_turtles[0].xcor()) < height and
        abs(hungry_turtles[0].ycor()) < width):
        turtle.Screen().bgcolor('green')
    else:
        turtle.Screen().bgcolor('yellow')

    update_turtles(hungry_turtles)

    hungry_turtles[0].forward(1)
    turtle.update()
