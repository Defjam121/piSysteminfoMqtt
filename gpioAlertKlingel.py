#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Filename:          gpioAlertKlingel.py
# Author:            Helpi
# Date:              2018-05-01
# Version:           1.0
# -----
# Last Modified:     
# Modified By:       
# 
###

import RPi.GPIO as GPIO
import time
import paho.mqtt.client as paho



GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # push button
print("set up pin")

def alert_action():
	print(time.strftime('%d/%m/%Y %X') + ' Edge detected on channel')
	time.sleep(0.01)         # need to filter out the false positive of some power fluctuation
    if GPIO.input(19):
        print("TESt")
    if GPIO.input(19) != 1:
        print('Quitting event handler because this was probably a false positive')
        return
    mosq.publish("/server/doorbell",time.strftime('%x %X'))


mosq = paho.Client()
mosq.connect("192.168.2.142")
mosq.loop_start()

GPIO.add_event_detect(19, GPIO.RISING, callback=alert_action, bouncetime=200)

while True:
	time.sleep(1)
	
GPIO.cleanup()
mosq.discconect()
mosq.loop_stop()