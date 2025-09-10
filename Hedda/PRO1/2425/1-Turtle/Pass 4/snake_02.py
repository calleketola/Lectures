import turtle

def up():
    hungry_turtle.setheading(90)
def down():
    hungry_turtle.setheading(-90)
def left():
    hungry_turtle.setheading(180)
def right():
    hungry_turtle.setheading(0)

# Din lösning behöver vara ovanför den här raden

# Variables
running = True
width = 250
height = 250

# Initialize
hungry_turtle = turtle.Turtle()
hungry_turtle.shape('turtle')
hungry_turtle.penup()

# Draw game board
turtle.tracer(0,0)
hungry_turtle.setpos((-width,height))
hungry_turtle.pendown()
hungry_turtle.setpos((width,height))
hungry_turtle.setpos((width,-height))
hungry_turtle.setpos((-width,-height))
hungry_turtle.setpos((-width,height))
# Lägg till de tre andra sidorna
hungry_turtle.penup()
hungry_turtle.setpos((0,0))
turtle.update()

# Game loop
while running:
    turtle.listen()
    turtle.onkey(up, 'Up')
    turtle.onkey(down, 'Down')
    turtle.onkey(left, 'Left')
    turtle.onkey(right, 'Right')

    # Check if within game board
    if (abs(hungry_turtle.xcor()) < height and
        abs(hungry_turtle.ycor()) < width):
        turtle.Screen().bgcolor('green')
    else:
        turtle.Screen().bgcolor('yellow')

    hungry_turtle.forward(1)
    turtle.update()
