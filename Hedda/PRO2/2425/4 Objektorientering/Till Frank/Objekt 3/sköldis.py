import turtle
import time
import random

class Sköldpadda():

    def __init__(self, färg):
        
        # Grejor för att rita ut
        self.turtle = turtle.Turtle()
        self.turtle.color(färg)
        self.turtle.shape('square')
        self.turtle.pu()

        self.riktning = 0
        self.x = 0
        self.y = 0
        self.hastighet = 20
                
    def rita(self):
        self.turtle.setpos((self.x, self.y))

    def gå(self):
        # 0: ->
        # 1: ^
        # 2: <-
        # 3: v
        if self.riktning == 0:
            self.x += 20

    def vänster(self):
        self.turtle.seth(180)

    def höger(self):
        pass

    def upp(self):
        pass

    def ner(self):
        pass


class Godis():

    def __init__(self):
        # Turtle specifika grejor
        self.turtle = turtle.Turtle()
        self.turtle.pu()
        self.turtle.shape("square")
        self.turtle.color("red")

        self.x = 40
        self.y = 40

    def rita(self):
        self.turtle.setpos(self.x, self.y)

    def ny_position(self):
        pass


sköldis = Sköldpadda('blue')
candy = Godis()

# Grejor för att rita ut
window = turtle.Screen()
window.setup(500,500)
window.tracer(0)

# Grejor för att knapptryck ska fungera
window.listen()
window.onkey(sköldis.vänster, 'a')
window.onkey(sköldis.höger, 'd')
window.onkey(sköldis.upp, 'w')
window.onkey(sköldis.ner, 's')

window.onkey(sköldis.vänster, 'Left')
window.onkey(sköldis.höger, 'Right')
window.onkey(sköldis.upp, 'Up')
window.onkey(sköldis.ner, 'Down')

while True:
    time.sleep(0.2)
    window.update()
    sköldis.gå()
    sköldis.rita()
    candy.rita()
