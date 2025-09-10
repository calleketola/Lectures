import turtle





# Initialize
hungry_turtle = turtle.Turtle()
hungry_turtle.shape('turtle')
width = 250
height = 250

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

hungry_turtle.penup()
# Variables
running = True
# Game loop
while running:
    turtle.listen()
    
    turtle.onkey(up, 'Up')
    turtle.onkey(down, 'Down')
    turtle.onkey(left, 'Left')
    turtle.onkey(right, 'Right')

    hungry_turtle.forward(1)
    turtle.update()
