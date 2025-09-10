from turtle import *

shape('turtle')

color("red")
fillcolor('yellow')

begin_fill() # Detta ger färg mellan strecken

forward(100) # Går framåt 100 steg
right(90) # Svänger 90 grader åt höger
forward(100)
left(90) # Svänger 90 grader åt vänster
forward(100)
#right(45)
#back(100*2**0.5) # Backar ~141 steg

end_fill() # Säger till när man ska sluta fylla
