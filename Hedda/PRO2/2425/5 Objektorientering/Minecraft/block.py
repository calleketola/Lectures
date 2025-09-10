class Block():

    def __init__(self, a, b, c, d):
        self.name = a
        self.hp = b
        self.defence = c
        self.colour = d

        self.position = [0,0]

    def hit(self, strength):
        if strength >= self.defence:
            self.hp -= 1
        if self.hp == 0:
            return False
        return True
