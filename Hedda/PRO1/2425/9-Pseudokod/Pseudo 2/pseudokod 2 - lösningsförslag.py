###############
## ÖVNING 01 ##
###############

"""
Implementera följande pseudokod för att hitta
största gemensamma nämnare mellan två heltal:

function gcd(a, b)
    while b ≠ 0
        t := b
        b := a mod b (mod motsvarar % i Python)
        a := t
    return a
"""
print("Övning 1")

def gcd(a, b): # Funktion som räknar ut största möjliga delare mellan a och b
    while b != 0: # När resten är noll ska vi sluta
        t = b # Kom ihåg värdet av b
        b = a%b # Resten mellan a och b
        a = t # Sätt a till gamla b värdet
    return a # Detta är nu största gemensamma delare

try:
    print("537, 63:", gcd(537, 63)) # Ska spotta ut 3
    print("700, 200:", gcd(700,200)) # Ska spotta ut 100
    print("15390127242, 963715242:", gcd(15390127242,963715242)) # Ska spotta ut 42
except NameError:
    print("Övning 1 ej påbörjad")
    

###############
## ÖVNING 02 ##
###############

"""
Implementera följande pseudokod:

FUNCTION gcd_rec(a,b):
    IF b EQUAL TO 0
        RETURN a
    ENDIF
    ELSE
        RETURN gcd_rec(b, a mod b)
"""

print("Övning 2")

def gcd_rec(a,b): # Funktion som hittar största gemensamma delare mellan a och b
    if b == 0: # Är b noll är vi klara
        return a # a är största gemensamam delare
    else: # Annars ska vi göra algoritmen
        return gcd_rec(b, a % b) # Gör nästa steg

try:
    print("537, 63:", gcd_rec(537, 63)) # Ska spotta ut 3
    print("700, 200:", gcd_rec(700,200)) # Ska spotta ut 100
    print("15390127242, 963715242:", gcd_rec(15390127242,963715242)) # Ska spotta ut 42
except NameError:
    print("Övning 2 ej påbörjad")

###############
## ÖVNING 03 ##
###############

"""
Implementera följande pseudokod:

function count_neighbours(board, row, col)
    n := length of board
    m := length of board[row]
    neighbours := 0
    for -1 <= y < 2
        for -1 <= x < 2
            if (0 <= row+y < n and 0 <= col+x < m
                and y != 0 and x != 0
                and board[row+y][col+x] == 'x')
                neighbours += 1
    return neighbours
"""

print("Övning 3")

task3 = [["~" for _ in range(10)] for _ in range(10)]
task3[0][2] = 'x'
task3[0][4] = 'x'
task3[0][8] = 'x'
task3[1][1] = 'x'
task3[1][9] = 'x'
task3[2][0] = 'x'
task3[2][1] = 'x'
task3[2][3] = 'x'
task3[2][6] = 'x'
task3[3][7] = 'x'
task3[3][8] = 'x'
task3[4][1] = 'x'
task3[4][5] = 'x'
task3[5][0] = 'x'
task3[5][8] = 'x'
task3[6][0] = 'x'
task3[6][4] = 'x'
task3[6][6] = 'x'
task3[6][9] = 'x'
task3[8][3] = 'x'
task3[8][7] = 'x'
task3[9][1] = 'x'
task3[9][9] = 'x'

for row in task3: # Gå igenom alla rader
    for col in row: # Gå igenom varje kolumn
        print(col, end="") # Skriv ut
    print() # Ny rad

def count_neighbours(board, row, col): # Funktion som räknar antalet grannar runt en punkt
    n = len(board) # Antal rader
    m = len(board[row]) # Antal kolumner
    neighbours = 0 # Antal grannar
    for y in range(-1, 2): # Kolla över och under
        for x in range(-1, 2): # Kolla vänster och höger
            if (0 <= row+y < n and 0 <= col+x < m 
                and y != 0 and x != 0
                and board[row+y][col+x] == 'x'): # Om innanför brädet, och inte den vi är i, har ett x
                neighbours += 1 # Öka antalet grannar
    return neighbours # Skicka tillbaka svaret

try:
    for row in range(len(task3)):
        for col in range(len(task3[row])):
            print(count_neighbours(task3, row, col), end="")
        print()
    """
Förväntad utskrift:
1010000010
1222120201
1010001121
2130211100
0100001212
1111121110
0100000101
0111121120
1010000010
0010101010
    """
except NameError:
    print("Övning 3 ej påbörjad")
            

###############
## ÖVNING 04 ##
###############

"""
Implementera följande pseudokod:

FUNCTION find_most_neighbours(board)
    SET x TO 0
    SET y TO 0
    FOR EVERY row ON board
        FOR EVERY col IN row
            IF VALUE IN board row col GREATER THAN VALUE IN board y x
                SET y TO row
                SET x TO col
    RETURN board y x
"""

def find_most_neighbours(board): # Funktion som hittar det högsta antalet grannar
    x = 0 # Antag 0
    y = 0 # Antag 0
    for row in range(len(board)): # För varje rad
        for col in range(len(board[row])): # För varje kolumn
            if board[row][col] >= board[y][x]: # Har den positionen fler än flest
                y = row # Uppdatera y
                x = col # Uppdatera x
    return board[y][x] # Skicka tillbaka största värdet

try:
    task4 = [[count_neighbours(task3, row, col) for col in range(len(task3[row]))] for row in range(len(task3))]
    print("Positionen med flest grannar har", find_most_neighbours(task4))
except NameError:
    print("Övning 4 ej klar")

###############
## ÖVNING 05 ##
###############

"""
Kommentera varje rad med kod.
"""

