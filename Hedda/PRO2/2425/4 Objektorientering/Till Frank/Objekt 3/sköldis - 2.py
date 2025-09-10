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

        self.svans = []

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
        self.uppdatera_svans()
        if self.riktning == 0:
            self.x += self.hastighet
        elif self.riktning == 1:
            self.y += self.hastighet
        elif self.riktning == 2:
            self.x -= self.hastighet
        elif self.riktning == 3:
            self.y -= self.hastighet

    def uppdatera_svans(self):
        for i in range(len(self.svans)-1,0,-1):
            self.svans[i].x = self.svans[i-1].x
            self.svans[i].y = self.svans[i-1].y
            self.svans[i].turtle.seth(self.svans[i-1].turtle.heading())
        if len(self.svans) >= 1:
            self.svans[0].x = self.x
            self.svans[0].y = self.y
            self.svans[0].turtle.seth(self.turtle.heading())
    
    def höger(self):
        if self.riktning != 2:
            self.riktning = 0
            self.turtle.seth(0)

    def vänster(self):
        if self.riktning != 0:
            self.riktning = 2
            self.turtle.seth(180)

    def upp(self):
        if self.riktning != 3:
            self.riktning = 1
            self.turtle.seth(90)

    def ner(self):
        if self.riktning != 1:
            self.riktning = 3
            self.turtle.seth(270)

    def rita(self):
        self.turtle.setpos((self.x, self.y))
        for bit in self.svans:
            bit.rita()
            
    def ät_godis(self, mat):
        if self.x == mat.x and self.y == mat.y:
            mat.ny_position()
            self.lägg_till_svans()
            return True
        return False

    def ät_svans(self):
        for bit in self.svans[1:]: # Man kan inte äta den närmsta biten
            if self.x == bit.x and self.y == bit.y:
                return True
        return False

    def lägg_till_svans(self):
        self.svans.append(Sköldpadda("black"))
        self.svans[-1].x = self.x
        self.svans[-1].y = self.y
        self.uppdatera_svans()


class Godis():

    def __init__(self):
        self.x = random.randint(-260//20+1, 260//20-1)*20
        self.y = random.randint(-260//20+1, 260//20-1)*20

        # Grejor för att rita ut
        self.turtle = turtle.Turtle()
        self.turtle.shape('square')
        self.turtle.color("green")
        self.turtle.pu()

    def ny_position(self):
        self.x = random.randint(-260//20+1, 260//20-1)*20
        self.y = random.randint(-260//20+1, 260//20-1)*20

    def rita(self):
        self.turtle.setpos((self.x, self.y))

def inom_planen(padda):
    if -260 <= padda.x < 260 and -260 <= padda.y < 260:
        return True
    return False

def game_over():
    turtle.setpos(-75,75)
    turtle.write("Game over", font=("Arial",24,"bold"))

def rita_poäng():
    turtle.setpos(-250,230)
    turtle.write("Poäng: "+ str(poäng), font=("Arial", 18,"normal"))

sköldis = Sköldpadda('blue')
candy = Godis()
poäng = 0

# Grejor för att rita ut
window = turtle.Screen()
window.setup(520,520)
window.tracer(0)
turtle.pu()
turtle.hideturtle()

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

spelar = True

while spelar:
    turtle.clear()
    rita_poäng()
    sköldis.gå()
    candy.rita()
    if sköldis.ät_godis(candy):
        poäng += 1
    if sköldis.ät_svans():
        game_over()
        spelar = False
    sköldis.rita()
    if not inom_planen(sköldis):
        game_over()
        spelar = False
    time.sleep(0.25)
    window.update()



