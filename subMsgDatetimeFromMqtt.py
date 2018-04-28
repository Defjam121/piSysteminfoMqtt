#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Filename:          datetimeToMqtt.py
# Author:            macbook 
# Date:              2018-04-28
# Version:           1.0
###
##------------------------------------------------------------------------
##    Bib
##------------------------------------------------------------------------
import paho.mqtt.client as mqtt
import datetime

##------------------------------------------------------------------------
##    Funktionen
##------------------------------------------------------------------------
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("Home/#")

def on_message(client, userdata, msg):
    print(str(datetime.datetime.now()) + ": " + msg.topic + " " + str(msg.payload))

##------------------------------------------------------------------------
##    Main
##------------------------------------------------------------------------
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.2.142", 1883, 60)

client.loop_forever()