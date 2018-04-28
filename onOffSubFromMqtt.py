#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Filename:          onOffSubFromMqtt.py
# Author:            macbook 
# Date:              2018-04-28
# Version:           1.0
###
###
##------------------------------------------------------------------------
##    Bib
##------------------------------------------------------------------------
import paho.mqtt.client as mqtt

##------------------------------------------------------------------------
##    Variablen
##------------------------------------------------------------------------
server="192.168.2.142"
topic="/test"

##------------------------------------------------------------------------
##    Funktionen
##------------------------------------------------------------------------
def on_connect(client, data, flags, rc):
    #print ("Connected with rc: " + str(rc))
    client.subscribe(topic)

def on_message(client, obj, msg):
    print ("Topic: "+ msg.topic+"\nMessage: "+ str(msg.payload))
    if "green" in str(msg.payload):
        print("  Green on!")     
    else:
        print("  Green off!")

##------------------------------------------------------------------------
##    Pointer
##------------------------------------------------------------------------
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(server, 1883, 60)

##------------------------------------------------------------------------
##    Main
##------------------------------------------------------------------------
client.loop_forever()