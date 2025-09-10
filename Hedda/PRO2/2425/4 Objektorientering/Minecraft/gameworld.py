import player
import random
import block as b
import tool

BLOCK_TYPES = ["Stone",
               "Dirt",
               "Wood",
               "Water",
               "Ore"]

BLOCK_SIZE = 25

class World():

    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.blocks = []

        self.player = player.Player(tool.Tool("Pick", 2))

    def generate_world(self):
        for i in range(self.width*self.height):
            block = random.choice(BLOCK_TYPES)
            if block == "Stone":
                self.blocks.append(b.Block("Stone", 3,1, "grey"))
            elif block == "Dirt":
                self.blocks.append(b.Block("Dirt", 1,0, "brown"))
            elif block == "Wood":
                self.blocks.append(b.Block("Wood", 2,0, "green"))
            elif block == "Ore":
                self.blocks.append(b.Block("Ore", 4,2, "cyan"))
            elif block == "Water":
                self.blocks.append(b.Block("Water", 1,0, "blue"))
            else:
                raise TypeError("Invalid block type")
            self.blocks[i].position[0] = (i%self.width)*BLOCK_SIZE # Set x position
            self.blocks[i].position[1] = i//self.width*BLOCK_SIZE # Set y position

    def update_block(self, i, block):
        pos = self.blocks[i].position
        self.blocks[i] = block
        self.blocks[i].position = pos        

    def draw_world(self, p):
        for block in self.blocks:
            p.draw_block(block)

    def draw_player(self, p):
        p.draw_inventory(self.player.tools, self.player.blocks)

    def add_score(self, x):
        self.player.add_score(x)
