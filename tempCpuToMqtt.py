#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Filename:          systemDataToMqtt.py
# Author:            macbook
# Date:              2018-04-26
# Version:           1.0
###
##------------------------------------------------------------------------
##    Bib
##------------------------------------------------------------------------
import paho.mqtt.publish as publish
from subprocess import check_output
from re import findall
##------------------------------------------------------------------------
##    Variablen
##------------------------------------------------------------------------
host="magicmirror2"

##------------------------------------------------------------------------
##    Funktionen
##------------------------------------------------------------------------
def get_temp():
    temp = check_output(["vcgencmd","measure_temp"]).decode("UTF-8")
    return(findall("\d+\.\d+",temp)[0])

def publish_message(topic, message):
    print("Publishing to MQTT topic: " + topic)
    print("Message: " + message)

    publish.single(topic, message, hostname="192.168.2.142")

##------------------------------------------------------------------------
##    Main
##------------------------------------------------------------------------
temp = get_temp()
publish_message("/server/" + host + "/temp", temp)