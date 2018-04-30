#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Filename:          platOnOff.py
# Author:            Helpi
# Date:              2018-04-29
# Version:           1.0
# -----
# Last Modified:     
# Modified By:       
# 
###

import paho.mqtt.client as paho
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
PINNR=7
GPIO.setup(PINNR, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
GPIO.output(PINNR,True) ## Turn on GPIO pin 7

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
    if (msg.payload=="1"):
        print "on"
        GPIO.output(PINNR,True)
    else:
        print "off"
        GPIO.Output(PINNR,False)

client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.username_pw_set("mqtt", "mqtt")
client.connect("192.168.1.1", 1883)
client.subscribe("3dprinter/plafan", qos=1)

client.loop_forever()