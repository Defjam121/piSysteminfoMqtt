#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Filename:          subMsgfromMqtt.py
# Author:            macbook 
# Date:              2018-04-28
# Version:           1.0
###
#!/usr/bin/env python
import paho.mqtt.client as mqtt

server="192.168.2.142"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe("test/#")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(server, 1883, 60)

client.loop_forever()