def draw_board(board):
    print(" ___")
    for row in board:
        print("|" + row[0] + row[1] + row[2] + "|")
    print(" ---")

def check_victory(board, player):
    for i in range(3):
        if row_victory(board, player, i):
            return True
        if col_victory(board, player, i):
            return True
    if dia_victory_1(board, player):
        return True
    if dia_victory_2(board, player):
        return True
    return False

def row_victory(board, player, row):
    return board[row][0] == board[row][1] == board[row][2] == player

def col_victory(board, player, col):
    return board[0][col] == board[1][col] == board[2][col] == player

def dia_victory_1(board, player):
    return board[0][0] == board[1][1] == board[2][2] == player

def dia_victory_2(board, player):
    return board[0][2] == board[1][1] == board[2][0] == player

def create_board():
    board = []
    for i in range(3):
        board.append([" "] * 3)
    return board

def take_position():
    valid = False
    while not valid:
        row = int(input("Choose row: "))
        if 1 <= row < 4:
            valid = True
    valid = False
    while not valid:
        col = int(input("Choose column: "))
        if 1 <= col < 4:
            valid = True
    return row-1, col-1

board = create_board()
player = "X"
playing = True
turn = 0
draw = False

while playing:
    turn += 1
    draw_board(board)
    print("Player " + player + "'s turn")
    row, col = take_position()
    
    while board[row][col] != " ":
        print("Position taken, choose again")
        row, col = take_position()
    
    board[row][col] = player
    
    if check_victory(board, player):
        playing = False
    else:
        if player == "X":
            player = "O"
        else:
            player = "X"
    if turn == 9:
        draw = True
        playing = False

draw_board(board)
if not draw:
    print("Player " + player + " has won!")
else:
    print("It's a draw")

input("Game over")
