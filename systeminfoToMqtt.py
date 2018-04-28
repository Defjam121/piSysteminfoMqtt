#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Filename:          systemDataToMqtt.py
# Author:            macbook
# Date:              2018-04-26
# Version:           1.0
###
# install Libs
# pip3 install paho-mqtt
# sudo pip3 install psutil
#
# python3 systemDataToMqtt.py <maschienenname>
#
##------------------------------------------------------------------------
##    Bib
##------------------------------------------------------------------------
import paho.mqtt.publish as publish
from subprocess import check_output
from re import findall
import psutil
import sys

##------------------------------------------------------------------------
##    Funktionen
##------------------------------------------------------------------------
def get_temp():
    temp = check_output(["vcgencmd","measure_temp"]).decode("UTF-8")
    return(findall("\d+\.\d+",temp)[0])

def get_disk_usage():
    return str(psutil.disk_usage('/').percent)

def get_memory_usage():
    return str(psutil.virtual_memory().percent)

def get_cpu_usage():
    return str(psutil.cpu_percent(interval=None))

def publish_message(topic, message):
    print("Publishing to MQTT topic: " + topic)
    print("Message: " + message)

    publish.single(topic, message, hostname="192.168.2.142")

##------------------------------------------------------------------------
##    Main
##------------------------------------------------------------------------
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Specify a computer name as argument to " + __file__)
        sys.exit(2)

    computer_name = 'magicmirror'
    print("Doing measurements for: " + computer_name)

    publish_message("/server/" + computer_name + "/Temp", get_temp())
    publish_message("/server/" + computer_name + "/DiskUsagePercent", get_disk_usage())
    publish_message("/server/" + computer_name + "/MemoryUsagePercent", get_memory_usage())
    publish_message("/server/" + computer_name + "/CpuUsagePercent", get_cpu_usage())