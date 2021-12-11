#subscribe

import paho.mqtt.client as paho

broker = "broker.hivemq.com"  #virtual broker

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print(message)

client = paho.Client()
client.on_message = on_message
client.connect(broker, 1883)
client.subscribe("bayan-181237")

client.loop_forever()

