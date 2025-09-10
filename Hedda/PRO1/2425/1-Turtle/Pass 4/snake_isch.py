import turtle

def up():
    hungry_turtle.setheading(90)
def down():
    hungry_turtle.setheading(-90)
def left():
    hungry_turtle.setheading(180)
def right():
    hungry_turtle.setheading(0)

hungry_turtle = turtle.Turtle()
hungry_turtle.shape('turtle')
hungry_turtle.penup()

width = 250
height = 250

# Game loop
running = True
while running:
    turtle.listen()
    turtle.onkey(up, 'Up')
    turtle.onkey(down, 'Down')
    turtle.onkey(left, 'Left')
    turtle.onkey(right, 'Right')
    if abs(hungry_turtle.xcor()) > width: 
        out_of_bounds = True
    elif abs(hungry_turtle.ycor()) > height:
        out_of_bounds = True
    else:
        out_of_bounds = False
    if out_of_bounds:
        turtle.Screen().bgcolor('red')
    else:
        turtle.Screen().bgcolor('green')

    hungry_turtle.forward(1)
    turtle.update()
