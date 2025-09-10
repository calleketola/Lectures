import paho.mqtt.client as mqtt # Importerar vårt bibliotek
import json

def on_connect(client, userdata, flags, reason_code, properties):
    print("Successfully connected", reason_code)
    client.subscribe("cake")
    print("subscribed to cake")

def on_message(client, userdata, msg):
    # Antal data punkter: 100
    info = json.loads(msg.payload.decode("utf-8"))
    if len(data) < 100:
        data.append(info)
        if len(data)%10 == 0:
            print(len(data), "datapunkter laddade.")
    else:
        action()
        input("Tryck enter för att fortsätta...")

def action():
    print("Totalt faller det", task_1(), "mm regn")
    print("Det faller", task_2(), "mm regn de dagarna")
    print("Maxtemperaturen var", task_3(), "grader Celsius")
    print("Den genomsnittliga längden mellan dagarna är", task_4())
    # Hur mycket regn faller det totalt?
    # Hur mycket regn faller det de dagar det är intressant?
    # Vad är den genomsnittliga längden mellan de intressanta dagarna?
    # Vad är maxtemperaturen de intressanta dagarna?


def task_1():
    # Hur mycket regn faller det totalt?
    rain = 0
    for point in data:
        rain += point["values"]["perspiration"]
    return rain
        
def task_2():
    # Hur mycket regn faller det de dagar det är intressant?
    rain = 0
    for point in data:
        if point["search-term"] == "perspiration":
            rain += point["values"]["perspiration"]
    return rain

def task_3():
    # Vad är max temperaturen de intressanta dagarna?
    temperatures = []
    for point in data:
        if point["search-term"] == "temperature":
            temperatures.append(point["values"]["temperature"])
    return max(temperatures)

def task_4():
    # Vad är den genomsnittliga längden mellan de intressanta dagarna?
    length = 0
    days = []
    for point in data:
        if point["search-term"] == "day":
            days.append(point["values"]["day"])
    total_length = max(days)-min(days)
    length = total_length/len(days)
    return round(length,2)


        
data = []

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.emqx.io", 1883)

client.loop_forever()








