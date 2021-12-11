 # publish

import paho.mqtt.client as paho

broker = "broker.hivemq.com"  #virtual broker

client = paho.Client()
client.connect(broker, 1883)

client.publish("bayan-181237", "SE-443")