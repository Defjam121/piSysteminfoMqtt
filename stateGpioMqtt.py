#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Filename:          stateGpioMqtt.py
# Author:            Helpi
# Date:              2018-04-29
# Version:           1.0
# -----
# Last Modified:     
# Modified By:       
# 
###

import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time

sensor = 18
mqttserver = "192.168.1.194"
mqttusr = "mqtt"
mqttpsw = "mqtt"
mqtttopic = "home/office/presence"

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False

while True:
    time.sleep(0.1)
    previous_state = current_state
    current_state = GPIO.input(sensor)
    if current_state != previous_state:
        new_state = "HIGH" if current_state else "LOW"
        mqttc = mqtt.Client()
        mqttc.username_pw_set(mqttusr, mqttpsw)
        mqttc.connect("192.168.1.194", 1883,60)
        if new_state == "HIGH":
            mqttc.publish(mqtttopic,1);
        else:
            mqttc.publish(mqtttopic,0);