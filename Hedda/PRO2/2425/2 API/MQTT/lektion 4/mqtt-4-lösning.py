import paho.mqtt.client as mqtt # Importerar vårt bibliotek
import json
import sys

def on_connect(client, userdata, flags, reason_code, properties):
    print("Successfully connected", reason_code)
    client.subscribe("cake")
    print("subscribed to cake")

def on_message(client, userdata, msg):
    d = json.loads(msg.payload.decode("utf-8"))
    print(d)
    if len(data) == d['id']: # if d not in data:    
        data.append(d)
    if len(data) == 50: # När vi har allt
        action()
        
def action():
    position = [0,0] # Nuvarande position
    ones = 0 # Hur många ettor vi ätit
    grid[position[0]][position[1]] = '#' # Uppdatera kartan
    for i in range(len(data)): # Gå igenom all data
        for step in range(data[i]['value']['steps']): # Ta alla steg
            move(position, i) # Flytta positionen
            if grid[position[0]][position[1]] == '1': # Kolla om etta
                ones += 1 # Ät ettan
            grid[position[0]][position[1]] = '#' # Uppdatera kartan
    print_grid()
    print("Position:", position)
    input("Tryck enter för att forstätta...")
    
def move(pos, i):
    if data[i]['value']['direction'] == 'right':
        if pos[0]+1 < 20:
            if grid[pos[0]+1][pos[1]] != "x":
                pos[0] += 1
    elif data[i]['value']['direction'] == 'left':
        if pos[0]-1 >= 0:
            if grid[pos[0]-1][pos[1]] != "x":
                pos[0] -= 1
    elif data[i]['value']['direction'] == 'up':
        if pos[1]+1 < 20:
            if grid[pos[0]][pos[1]+1] != "x":
                pos[1] += 1
    elif data[i]['value']['direction'] == 'down':
        if pos[1]-1 >= 0:
            if grid[pos[0]][pos[1]-1] != "x":
                pos[1] -= 1

def print_grid():
    color = sys.stdout.shell
    for row in grid:
        for col in row:
            if col == "x":
                color.write(col+" ", "COMMENT")
            elif col == "#":
                color.write(col+" ", "KEYWORD")
            else:
                color.write(col+" ", "STRING")
        print()

grid = [['0', '1', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '1', '0', '0', '1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
        ['0', '0', '0', '0', '0', '0', '1', '0', '0', '0'],
        ['1', '0', '0', '0', '0', '0', '0', '1', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '1', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '1', '0', '1'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '1', '1', '0', '0', '0', '0', '0']]

grid = [['0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0'],
        ['1', 'x', '0', 'x', 'x', 'x', '0', '0', 'x', 'x', 'x', '0', '0', 'x', '1', '0', '0', '0', '0', '1'],
        ['0', 'x', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', 'x', 'x', '1', '0', '0', '0', '0', '0'],
        ['0', 'x', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'x', '0', '0', '0', '0', '0', '0'],
        ['0', 'x', '0', '0', 'x', 'x', 'x', '0', '0', '0', 'x', '1', '0', 'x', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', 'x', '0', '0', 'x', 'x', '0', '0', 'x', '0', '0', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', 'x', '0', '0', '0', '1', '0', '1', '0', '0', '1', '1'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', 'x', '1', '0', '0', 'x', '0', '0', '0', 'x', 'x', 'x'],
        ['0', 'x', '0', 'x', 'x', '0', 'x', '0', '0', 'x', '0', '0', '0', '1', '0', '1', '0', 'x', '0', '0'],
        ['0', 'x', '0', 'x', 'x', '0', 'x', '1', '0', '0', 'x', '0', '0', 'x', '0', '1', '0', 'x', '0', '0'],
        ['1', '0', '0', 'x', 'x', '0', '0', '0', '0', '0', 'x', '0', '0', 'x', '0', '0', '0', 'x', '0', '0'],
        ['0', '0', '0', 'x', 'x', '0', '0', '0', 'x', 'x', 'x', '0', '1', 'x', '0', '1', '0', '1', '1', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', 'x', '0', '1', '0', '0', '0', '0', 'x', 'x', '0', '1', '0'],
        ['0', '0', '0', '0', '0', '0', 'x', 'x', 'x', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', 'x', 'x', '1', '0', '0', '0', '0', '0', '0', '0', 'x', '0', '0', '1', '0', 'x', '0'],
        ['0', 'x', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'x', '0', '0', '0', '0', 'x', '0'],
        ['0', 'x', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '1', 'x', '0', '0', '0', '1', 'x', '0'],
        ['0', 'x', '0', 'x', 'x', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'x', 'x', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'x', 'x', '0', 'x', 'x', 'x', '0', '0', '0'],
        ['0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']]


#for row in grid_2:
#    for col in row:
#        print(col, end=" ")
#    print()

data = []

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.emqx.io", 1883)

client.loop_forever()








