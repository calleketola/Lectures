import random

class Block():

    def __init__(self, sym, x, y):
        assert len(sym)==1
        self.x = x
        self.y = y
        self.symbol = sym

    def __str__(self):
        return self.symbol


class Grid():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.positions = [[None for _ in range(width)] for _ in range(height)]

    def insert_block(self, block):
        self.positions[block.y][block.x] = block

    def __repr__(self):
        out = ""
        for row in self.positions:
            for col in row:
                if col:
                    out += str(col)
                else:
                    out += "."
            out += "\n"
        return out



def insert_block_in_grid(b, g):
    # Insert a block into the grid
    grid[b.y][b.x] = b

# Create the grid
grid = Grid(10,10)
# Create blocks
blocks = [Block(str(i), random.randint(0,9), random.randint(0,9)) for i in range(10)]
# Insert blocks into grid
for block in blocks:
    grid.insert_block(block)
# Print the grid
print(grid)
