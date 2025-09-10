import block as b

class Player():

    def __init__(self, t):
        self.score = 0
        self.active_tool = t

        # Detta är vårt inventory
        self.tools = [None for _ in range(8)]
        self.blocks = [None for _ in range(8)]

        self.tools[0] = self.active_tool

        self.blocks[0] = b.Block("Dirt", 1, 0, "brown")

        self.active_block = self.blocks[0]

    def add_score(self, x):
        self.score += x
