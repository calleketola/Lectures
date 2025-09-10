import paho.mqtt.client as mqtt # Importerar vårt bibliotek
import json

def on_connect(client, userdata, flags, reason_code, properties):
    print("Successfully connected", reason_code)
    client.subscribe("cake")
    print("subscribed to cake")

def on_message(client, userdata, msg):
    print(msg.payload.decode("utf-8"))
    # Task 1
    #task_1(msg.payload.decode("utf-8"))
    task_2(msg.payload.decode("utf-8"))

def task_1(message):
    d = json.loads(message)
    if d not in data:
        data.append(d)
    else:
        pos = [0,0]
        for x in data:
            if x["value"]["direction"] == "up":
                pos[1] += x["value"]["steps"]
            elif x["value"]["direction"] == "down":
                pos[1] -= x["value"]["steps"]
            elif x["value"]["direction"] == "right":
                pos[0] += x["value"]["steps"]
            elif x["value"]["direction"] == "left":
                pos[0] -= x["value"]["steps"]
        print(pos) # (5,7)
    
def task_2(message):
    d = json.loads(message)
    # Vi vet att längden är 10
    data[d['id']] = d['value']
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


    pos = [0,0]
    grid[pos[0]][pos[1]] = 'x'    
    if None not in data: # Ser till att vi bara går framåt när listan är fylld
        for point in data:
            if point['direction'] == 'up':
                for step in range(point['steps']):
                    pos[1] += 1
                    grid[pos[0]][pos[1]] = 'x'
            elif point['direction'] == 'down':
                for step in range(point['steps']):
                    pos[1] -= 1
                    grid[pos[0]][pos[1]] = 'x'
            elif point['direction'] == 'right':
                for step in range(point['steps']):
                    pos[0] += 1
                    grid[pos[0]][pos[1]] = 'x'
            elif point['direction'] == 'left':
                for step in range(point['steps']):
                    pos[0] -= 1
                    grid[pos[0]][pos[1]] = 'x'

        for row in grid:
            for col in row:
                print(col, end="")
            print()
        input("Press enter to continue")
      
            
    

data = []
# För task 2 använd:
data = [None for _ in range(10)]

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.emqx.io", 1883)

client.loop_forever()

# Lösningsförslag






