import matplotlib.pyplot as plt
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, reason_code, properties): # Called on connect
    print("Successfully connected")
    topic = "cake"
    client.subscribe(topic) # Subscribe to topic
    print("Subscribed to", topic)

def on_message(client, userdata, msg):
    print(msg.topic, msg.payload) # Print recieved message
    point = msg.payload.split() # Messages will be on the form "x y"
    try:
        if len(point) != 2:
            raise IndexError
        x.append(float(point[0])) # Convert to float
        y.append(float(point[1])) # Convert to float
        update_plot()
    except ValueError:
        print("Bad massage")
    except IndexError:
        print("Wrong size")

    

def create_plot():
    plt.ion() # Keeps the plot updating
    fig = plt.figure() # Creates the plot area
    ax = fig.add_subplot(111)
    line, = ax.plot(x, y) # Add data points
    fig.canvas.draw() # Draw plot
    fig.canvas.flush_events() # Update screen

    return fig, line, ax # These are needed outside the function

def update_plot():
    line.set_data(x, y) # Update with the new data, this will slow as the data set increases
    ax.relim() # Adjust the axes
    ax.autoscale_view() # Adjust the view
    fig.canvas.draw() # Draw plot
    fig.canvas.flush_events() # Update screen
    
x = []
y = []
fig, line, ax = create_plot()

# Create and define the client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.emqx.io", 1883)

client.loop_forever()


