import turtle

BLOCK_WIDTH = 10

class Player():

    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0

    def move(self, direction):
        """
        En metod som förflyttar karaktären
        """
        if direction == "u":
            self.pos_y -= 1
        elif direction == "d" or direction == "n":
            self.pos_y += 1
        elif direction == "r" or direction == "h":
            self.pos_x += 1
        elif direction == "l" or direction == "v":
            self.pos_x -= 1
            
            

    
class Game_World():

    def __init__(self, file):
        # Läs in filen
        with open(file) as f:
            data = f.readlines()
        # Rensa datan
        for i in range(len(data)):
            data[i] = data[i].strip("\n")

        # Spara ner kartans storlek
        self.width = len(data[i])
        self.height = len(data)

        # Läs in banan och väggar
        self.passable = [[False if pos == "#" else True for pos in row] for row in data]
        # Skapa karaktärerna
        self.player = Player()
        self.wolf = Player()
        # Målets position
        self.goal = [0,0] # ROW; COL

        # Hitta speleare, varg och mål
        for row in range(self.height):
            for col in range(self.width):
                if data[row][col] == "O":
                    self.player.pos_x = col
                    self.player.pos_y = row
                elif data[row][col] == "X":
                    self.wolf.pos_x = col
                    self.wolf.pos_y = row
                elif data[row][col] == "G":
                    self.goal = [row,col]

    def print_world(self):
        """
        Metod som ritar ut spelplanen
        """
        for row in range(self.height):
            for col in range(self.width):
                if self.wolf.pos_x == col and self.wolf.pos_y == row:
                    print("W", end="")
                elif self.player.pos_x == col and self.player.pos_y == row:
                    print("O", end="")
                elif self.passable[row][col] == True:
                    print(" ", end="")
                else:
                    print("#", end="")
            print()

g = Game_World("bana-1.txt")
# Game Loop
playing = True
while playing == True:
    g.print_world()
    # Här tar vi emot en position, men bryr
    # oss bara om första bokstaven
    direction = input("Hur vill du gå (vänster, höger, ner eller upp)? ")[0].lower()
    # Kolla om du får flytta på dig

    # Uppdatera din position

    # Kolla om du vunnit

    # Kolla om vargen kan flytta på sig

    # Uppdatera vargens position

    # Kolla om vargen äter upp dig

    # Låt vargen gå igen

# Hantera vinst/förlust
    
