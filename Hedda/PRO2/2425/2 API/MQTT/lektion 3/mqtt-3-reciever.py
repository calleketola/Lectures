import paho.mqtt.client as mqtt # Importerar vårt bibliotek
import json

def on_connect(client, userdata, flags, reason_code, properties):
    print("Successfully connected", reason_code)
    client.subscribe("cake")
    print("subscribed to cake")

def on_message(client, userdata, msg):
    print(msg.payload.decode("utf-8"))
    info = json.loads(msg.payload.decode("utf-8"))
##    if len(data) == 0:
##        data.append(info["value"])
##        time.append(info["time"])
##    elif info["value"] in data:
##        print("Length of data:", len(data))
##        time.append(info["time"])
##
##        
##        starttime = time[0].split(":")
##        start_seconds = int(starttime[2])
##        start_minutes = int(starttime[1])
##        start_hours = int(starttime[0])
##        secs_0 =start_seconds+60*start_minutes+60*60*start_hours
##
##        endtime = time[1].split(":")
##        end_seconds = int(endtime[2])
##        end_minutes = int(endtime[1])
##        end_hours = int(endtime[0])
##        secs_1 =end_seconds+60*end_minutes+60*60*end_hours
##        print("Cycle time", secs_1-secs_0)
##    else:
##        data.append(info["value"])
        
data = []
time = []

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.emqx.io", 1883)

client.loop_forever()








