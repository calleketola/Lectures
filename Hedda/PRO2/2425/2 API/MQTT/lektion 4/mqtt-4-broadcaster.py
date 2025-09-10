import paho.mqtt.client as mqtt
import time
import random
from datetime import date, datetime
import json

import math

def on_connect(client, userdata, flags, reason_code, properties): # Called on connect
    print("Connected with result code "+str(reason_code))
    #send()

def send_1():
    # Send data to the broker
    # a. Bestäm slutposition
    # b. Gör så att den går från id 0 först
    # c. Rita ut den tagna vägen
    # d. Hur många ettor passerar man?

    # Load the data
    with open("data.json") as f:
        data = json.load(f)
    topic = "cake"
    x = 0
    print("Broadcasting to", topic)
    while True:
        time.sleep(0.5)
        message = json.dumps(data["task-1"][x])
        client.publish(topic, message)
        x += 1
        if x >= len(data["task-1"]):
            x = 0

def send_2():
    # Load the data
    with open("data-2.json") as f:
        data = json.load(f)
    topic = "cake"
    x = 0
    print("Broadcasting to", topic)
    while True:
        time.sleep(0.1)
        message = json.dumps(data[x])
        client.publish(topic, message)
        x += 1
        if x >= len(data):
            x = 0
            
# Define the client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect

client.connect("broker.emqx.io", 1883)

#send_1()
send_2()
#send_3()






