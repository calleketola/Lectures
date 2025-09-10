import random

class Block():

    def __init__(self, x, y, sym):
        self.x = x
        self.y = y
        self.symbol = sym

    def move_x(self, dx):
        self.x += dx

    def move_y(self, dy):
        self.y += dy

    def __str__(self):
        return self.symbol


class Grid():

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.positions = [[None for i in range(self.width)] for j in range(self.height)]

    def insert_block(self, b):
        """
        En  metod som stoppar in ett block i rutnätet.
        Om där redan är ett block så ska det skrivas över.
        """
        self.positions[b.y][b.x] = b

    def push_block(self, row, col, direction, steps):
        """
        Detta är en metod som flyttar ett block steps
        steg. Om ett block krockar så ska den föra över
        kvarvarande steg till det den krockar i.
        Om ett block krockar i väggen ska det studsa.

        Detta är en "rekursiv" lösning. Vi tar alltså
        bara ett steg i taget och ser vad som händer,
        sen gör vi om hela funktionen.
        """
        if isinstance(self.positions[row][col], Block) == False:
            return
        if steps == 0:
            return
        if direction == "up":
            if row == 0: # Vi krockar i väggen
                self.push_block(row, col, "down", steps)
            else:
                # Kolla om vi krockar i ett annan block
                if isinstance(self.positions[row-1][col], Block) == False:
                    # Uppdatera positioner
                    self.positions[row-1][col] = self.positions[row][col]
                    self.positions[row][col] = None
                self.push_block(row-1, col, direction, steps-1)
        elif direction == "down":
            if row == self.height-1: # Vi krockar i väggen
                self.push_block(row, col, "up", steps)
            else:
                # Kolla om vi krockar i ett annan block
                if isinstance(self.positions[row+1][col], Block) == False:
                    # Uppdatera positioner
                    self.positions[row+1][col] = self.positions[row][col]
                    self.positions[row][col] = None
                self.push_block(row+1, col, direction, steps-1)
        elif direction == "left":
            if col == 0: # Vi krockar i väggen
                self.push_block(row, col, "right", steps)
            else:
                # Kolla om vi krockar i ett annan block
                if isinstance(self.positions[row][col-1], Block) == False:
                    # Uppdatera positioner
                    self.positions[row][col-1] = self.positions[row][col]
                    self.positions[row][col] = None
                self.push_block(row, col-1, direction, steps-1)
        elif direction == "right":
            if col == self.width-1: # Vi krockar i väggen
                self.push_block(row, col, "left", steps)
            else:
                # Kolla om vi krockar i ett annan block
                if isinstance(self.positions[row][col+1], Block) == False:
                    # Uppdatera positioner
                    self.positions[row][col+1] = self.positions[row][col]
                    self.positions[row][col] = None
                self.push_block(row, col+1, direction, steps-1)

    def __repr__(self):
        out = ""
        for row in self.positions:
            for column in row:
                if column:
                    out += str(column)
                else:
                    out += "."
            out += "\n"
        return out

grid = Grid(10,10)
for i in range(10):
    grid.insert_block(Block(random.randint(0,9),random.randint(0,9),chr(i+65)))

print(grid)





