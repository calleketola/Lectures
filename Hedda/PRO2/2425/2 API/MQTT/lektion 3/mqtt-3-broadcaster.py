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
    # Ta reda på antalet element
    topic = "cake"
    x = 0
    data = [i for i in range(24)]
    while True:
        time.sleep(0.25)
        now = datetime.now()
        message = data[x]
        client.publish(topic, str(message))
        x += 1
        if x >= len(data):
            x = 0


def send_2():
    # Send data to the broker
    # Ta reda på antalet element
    topic = "cake"
    x = 0
    data = [i for i in range(60)]
    while True:
        time.sleep(0.25)
        x = random.randint(0, len(data)-1)
        message = data[x]
        client.publish(topic, str(message))


def send_3():
    # a. Ta reda på antalet element
    # b. Ta reda på hur lång en cykel är
    topic = "cake"
    x = 0
    data = [i for i in range(60)]
    random.shuffle(data)
    while True:
        time.sleep(0.25)
        now = datetime.now()
        message = {"time": now.strftime("%H:%M:%S"),
                "value": data[x]}
        client.publish(topic, json.dumps(message))
        x += 1
        if x >= len(data):
            x = 0
            
            
# Define the client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect

client.connect("broker.emqx.io", 1883)

#send_1()
#send_2()
send_3()






