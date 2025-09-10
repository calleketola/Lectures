import turtle
import time
import random

class Sköldpadda():

    def __init__(self, färg):
        self.färg = färg

        self.x = 0
        self.y = 0

        self.hastighet = 20
        self.riktning = 0

        # Grejor för att rita ut
        self.turtle = turtle.Turtle()
        self.turtle.color(self.färg)
        self.turtle.shape('square')
        self.turtle.pu()

    def gå(self):
        # 0: ->
        # 1: ^
        # 2: <-
        # 3: v
        if self.riktning == 0:
            self.x += self.hastighet
        elif self.riktning == 1:
            self.y += self.hastighet
        elif self.riktning == 2:
            self.x -= self.hastighet
        elif self.riktning == 3:
            self.y -= self.hastighet
    
    def höger(self):
        self.riktning = 0

    def vänster(self):
        self.riktning = 2

    def upp(self):
        self.riktning = 1

    def ner(self):
        self.riktning = 3

    def rita(self):
        self.turtle.setpos((self.x, self.y))

    def ät_godis(self, mat):
        if self.x == mat.x and self.y == mat.y:
            mat.ny_position()


class Godis():

    def __init__(self):
        self.x = random.randint(-260//20+1, 260//20-1)*20
        self.y = random.randint(-260//20+1, 260//20-1)*20

        # Grejor för att rita ut
        self.turtle = turtle.Turtle()
        self.turtle.shape('square')
        self.turtle.pu()

    def ny_position(self):
        self.x = random.randint(-260//20+1, 260//20-1)*20
        self.y = random.randint(-260//20+1, 260//20-1)*20

    def rita(self):
        self.turtle.setpos((self.x, self.y))


sköldis = Sköldpadda('blue')
candy = Godis()

# Grejor för att rita ut
window = turtle.Screen()
window.setup(520,520)
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
    sköldis.gå()
    sköldis.ät_godis(candy)
    sköldis.rita()
    candy.rita()
    window.update()
    time.sleep(0.5)
