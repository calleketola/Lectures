import turtle
import tool
import block as b

BLOCK_SIZE = 25

class Painter():

    def __init__(self):
        self.t = turtle.Turtle()
        self.t.penup()
        self.t.speed(0)
        self.t.hideturtle()

    def draw_block(self, block):
        self.t.setpos(block.position)
        self.t.fillcolor(block.colour)
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(BLOCK_SIZE)
            self.t.left(90)
        self.t.end_fill()

    def draw_inventory(self, tools, blocks):
        self.draw_player_tools(tools)
        self.draw_player_blocks(blocks)
        
    def draw_player_tools(self, tools):
        # Ritar ut verktygen först
        self.t.setpos(-2*BLOCK_SIZE,0)
        self.t.pendown()
        self.t.color("black")
        self.t.seth(0)
        for i in range(len(tools)):
            # Draw square
            for _ in range(4):
                self.t.fd(BLOCK_SIZE)
                self.t.lt(90)
            if isinstance(tools[i], tool.Tool):
                self.t.pu()
                self.t.lt(90)
                self.t.fd(BLOCK_SIZE//3)
                self.t.rt(90)
                self.t.fd(5)
                self.t.write(tools[i].name)
                self.t.bk(5)
                self.t.rt(90)
                self.t.fd(BLOCK_SIZE//3)
                self.t.lt(90)
                self.t.pd()
            # Adjust position
            self.t.lt(90)
            self.t.fd(BLOCK_SIZE)
            self.t.rt(90)
        self.t.pu()

    def draw_player_blocks(self, blocks):
        # rita ut block-raden
        self.t.setpos(0,-2*BLOCK_SIZE)
        self.t.pendown()
        self.t.color("black")
        self.t.seth(0)
        for i in range(len(blocks)):
            # Draw square
            if isinstance(blocks[i], b.Block):
                self.t.fillcolor(blocks[i].colour)
                self.t.begin_fill()
                for _ in range(4):
                    self.t.fd(BLOCK_SIZE)
                    self.t.lt(90)
                self.t.end_fill()
            else:
                for _ in range(4):
                    self.t.fd(BLOCK_SIZE)
                    self.t.lt(90)
            # Adjust position
            self.t.fd(BLOCK_SIZE)
        self.t.pu()
