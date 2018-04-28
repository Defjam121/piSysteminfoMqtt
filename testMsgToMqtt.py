#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Filename:          testMsgToMqtt.py
# Author:            macbook 
# Date:              2018-04-28
# Version:           1.0
###
import time
import paho.mqtt.client as mqtt

server="192.168.2.142"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

client = mqtt.Client()
client.on_connect = on_connect

client.connect(server, 1883, 60)

client.loop_start()

while True:
    time.sleep(2)
    client.publish("test/temperature", "test")