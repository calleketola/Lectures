import paho.mqtt.client as mqtt # Importerar vårt bibliotek
import json

def on_connect(client, userdata, flags, reason_code, properties):
    print("Successfully connected", reason_code)
    client.subscribe("cake")
    print("subscribed to cake")

def on_message(client, userdata, msg):
    # Antal data punkter: 100
    info = json.loads(msg.payload.decode("utf-8"))
    #print(info)

    if info in data:
        action_b()
    else:
        data.append(info)
    
##    if len(data) < 100:
##        data.append(info)
##        if len(data)%10 == 0:
##            print(len(data), "datapunkter laddade.")
##    else:
##        action_a()
##        input("Tryck enter för att fortsätta...")

def action_a():
    print("Totalt faller det", task_1(), "mm regn")
    print("Det faller", task_2(), "mm regn de dagarna")
    print("Maxtemperaturen var", task_3(), "grader Celsius")
    print("Den genomsnittliga längden mellan dagarna är", task_4())
    # Hur mycket regn faller det totalt?
    # Hur mycket regn faller det de dagar det är intressant?
    # Vad är den genomsnittliga längden mellan de intressanta dagarna?
    # Vad är maxtemperaturen de intressanta dagarna?

def action_b():
    # Med den nya datan.
    # Den här datan har blandats.
    # Hur många datapunkter är det i serien?
    # Hur många värden finns det totalt bland alla punkter?
    # Vilken datapunkt har högst summa?
    # Vad är den genomsnittliga summan av alla värden?
    # a) Om man räknar ALLA värden
    # b) Om man räknar genomsnitt per datapunkt
    # 1
    print("Det är", len(data), "element")
    # 2
    antal_tal = 0
    for point in data:
        antal_tal += point["values"]["length"]
    print("Det är totalt", antal_tal, "tal")
    # 3
    highest_pos = 0
    for i in range(len(data)):
        summa = sum(data[i]["values"]["values"])
        if summa > sum(data[highest_pos]["values"]["values"]):
            highest_pos = i
    print("Den högsta summan finns i", data[highest_pos]["id"], "och är", sum(data[highest_pos]["values"]["values"]))
    input("Tryck för att fortsätta...")

def task_1():
    # Hur mycket regn faller det totalt?
    rain = 0
    for i in range(len(data)):
        rain += data[i]["values"]["perspiration"]
    return rain
        
def task_2():
    # Hur mycket regn faller det de dagar det är intressant?
    rain = 0
    for i in range(len(data)):
        if data[i]["search-term"] == "perspiration":
            rain += data[i]["values"]["perspiration"]
    return rain

def task_3():
    # Vad är max temperaturen de intressanta dagarna?
    temperatures = []
    for i in range(len(data)):
        if data[i]["search-term"] == "temperature":
            temperatures.append(data[i]["values"]["temperature"])
    max_temperature = -274
    for i in range(len(data)):
        if data[i]["search-term"] == "temperature":
            if data[i]["values"]["temperature"] > max_temperature:
                max_temperature = data[i]["values"]["temperature"]
    return max(temperatures)

def task_4():
    # Vad är den genomsnittliga längden mellan de intressanta dagarna?
    length = 0
    days = []
    for i in range(len(data)):
        if data[i]['search-term'] == "day":
            days.append(data[i]['values']['day'])
    length = (max(days)-min(days))/len(days)

    return round(length,2)
        
data = []

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.emqx.io", 1883)

client.loop_forever()








