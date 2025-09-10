class Player():

    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0


    def move(self, direction):
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
        with open(file) as f:
            data = f.readlines()
        # Clean data
        for i in range(len(data)):
            data[i] = data[i].strip("\n")
            
        self.width = len(data[i])
        self.height = len(data)

        self.passable = [[False if pos == "#" else True for pos in row] for row in data]

        self.player = Player()
        self.wolf = Player()

        self.goal = [0,0] # ROW; COL

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

    def move_player(self, direction):
        # Move player
        # Check if it can move
        if direction == "u":
            if self.passable[self.player.pos_y-1][self.player.pos_x]:
                self.player.move(direction)
        elif direction == "d" or direction == "n":
            if self.passable[self.player.pos_y+1][self.player.pos_x]:
                self.player.move(direction)
        elif direction == "l" or direction == "v":
            if self.passable[self.player.pos_y][self.player.pos_x-1]:
                self.player.move(direction)
        elif direction == "r" or direction == "h":
            if self.passable[self.player.pos_y][self.player.pos_x+1]:
                self.player.move(direction)

    def move_wolf(self, direction):
        # Move player
        # Check if it can move
        if direction == "u":
            if self.passable[self.wolf.pos_y-1][self.wolf.pos_x]:
                self.wolf.move(direction)
        elif direction == "d" or direction == "n":
            if self.passable[self.wolf.pos_y+1][self.wolf.pos_x]:
                self.wolf.move(direction)
        elif direction == "l" or direction == "v":
            if self.passable[self.wolf.pos_y][self.wolf.pos_x-1]:
                self.wolf.move(direction)
        elif direction == "r" or direction == "h":
            if self.passable[self.wolf.pos_y][self.wolf.pos_x+1]:
                self.wolf.move(direction)

    def check_game_over(self):
        if self.player.pos_x == self.wolf.pos_x and self.player.pos_y == self.wolf.pos_y:
            return True

    def __debug_print_world(self):
        for row in self.passable:
            for col in row:
                if col:
                    print(" ", end="")
                else:
                    print("#", end="")
            print()

game = Game_World("bana-1.txt")
wolf_speed = 2
# Game Loop
playing = True
won = False
while playing == True:
    game.print_world()
    direction = input("Hur vill du gå (vänster, höger, ner eller upp)? ")[0].lower()
    # Uppdatera din position
    game.move_player(direction)
    # Kolla om du vunnit
    if game.player.pos_x == game.goal[1] and game.player.pos_y == game.goal[0]:
        playing = False
        won = True
        continue
    # Uppdatera vargens position
    for i in range(wolf_speed):
        game.move_wolf(direction)
    # Kolla om vargen äter upp dig
        if game.check_game_over():
            playing = False
            continue
game.print_world()
if won:
    print("Grattis!")
else:
    print("Vargen åt upp dig")
    
