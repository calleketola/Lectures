import paho.mqtt.client as mqtt
import time
import random

import math

def on_connect(client, userdata, flags, reason_code, properties): # Called on connect
    print("Connected with result code "+str(reason_code))
    #send()

def send():
    # Send data to the broker
    topic = "cake"
    x = 0
    while True:
        time.sleep(1)
        #y = random.randint(-10,100)
        y = math.sin(x)
        out = str(x)+" "+str(y)
        client.publish(topic, out)
        print("Destination: ", topic, "; Message: ", out, sep="")
        x += 0.125
            
# Define the client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
#client.on_message = on_message


client.connect("broker.emqx.io", 1883)
#client.loop_forever()
send() 
