#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Filename:          mqttGpioPaho.py
# Author:            Helpi
# Date:              2018-04-29
# Version:           1.0
# -----
# Last Modified:     
# Modified By:       
# 
###

 
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO 
 
gpio_pin = 14 
 
GPIO.setmode(GPIO.BCM) # chon kieu danh so chan GPIO la BCM
GPIO.setup(gpio_pin, GPIO.OUT)
 
def on_connect(mqttc, obj, flags, rc):
 pass
 
def on_message(mqttc, obj, msg):
 print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
 if(msg.topic == "raspivn/demo/led"):
   if(str(msg.payload) == "1"): #bat LED
     GPIO.output(gpio_pin, GPIO.HIGH)
   elif(str(msg.payload) == "0"): #tat LED
     GPIO.output(gpio_pin, GPIO.LOW)
 
def on_publish(mqttc, obj, mid):
 print("mid: "+str(mid))
 
def on_subscribe(mqttc, obj, mid, granted_qos):
 pass
 
def on_log(mqttc, obj, level, string):
 pass
 
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
 
mqttc.connect("192.168.1.77", 1883, 60) #dien IP cua Pi, vd: 192.168.1.77
mqttc.subscribe("raspivn/demo/led", 0) 
mqttc.loop_forever()