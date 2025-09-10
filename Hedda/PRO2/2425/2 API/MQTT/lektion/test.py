import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Successfully connected", rc)
    client.subscribe("cake")
    print("subscribed to cake")

def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)
    data.append(msg.payload)
    action()

def action():
    print(data)

data = []

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.emqx.io", 1883)

client.loop_forever()
