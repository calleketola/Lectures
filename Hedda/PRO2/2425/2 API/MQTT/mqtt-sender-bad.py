import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, reason_code, properties): # Called on connect
    print("Connected with result code "+str(reason_code))
    send_test()
    

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def send_test():
    # Send data to the broker
    time.sleep(1)
    client.publish("cake", "0 5")
    time.sleep(1)
    client.publish("cake", "1 7")
    time.sleep(1)
    client.publish("cake", "2 8")
    time.sleep(1)
    client.publish("cake", "3 1")

# Define the client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.emqx.io", 1883)

client.loop_forever()


