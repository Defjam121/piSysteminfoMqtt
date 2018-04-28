#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Filename:          gpioToMqtt.py
# Author:            macbook 
# Date:              2018-04-29
# Version:           1.0
###
import RPi.GPIO as GPIO
import time
import sys
import os

# GLOBAL FLAG
reverse = 0
curr_pin = 0

GPIO.setmode(GPIO.BCM)

# DISABLE WARNING, BECAUSE SOME GPIO IS BEEN USING BY NODE-RED DEAMON.
GPIO.setwarnings(False)

# THIS IS THE MOTOR PIN CONTROL
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
# 5 SWITCH ON/OFF CONTROL
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#INIITIAL THE MOTOR TO START ONCE LAUNCH THIS APPLICATION
GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.LOW)

#def reversefunc():
#        GPIO.output(23,GPIO.HIGH)
#        GPIO.output(24,GPIO.HIGH)

def standardStep(pinnumber):
        global reverse
        global curr_pin

        if(pinnumber == 17):
                GPIO.output(23, GPIO.LOW)
                GPIO.output(24, GPIO.LOW)
                reverse = 0

        #print 'current pin %d' % curr_pin
        if((reverse == 0) and (curr_pin != pinnumber)):
        #if(reverse == 0):
                GPIO.output(23, GPIO.HIGH) #STOP THE MOTOR
                # SEND MQTT TO GATEWAY START
                if(pinnumber == 17):
                        machinename = "spi"
                elif(pinnumber == 22 or pinnumber == 25):
                        machinename = "smt"
                elif(pinnumber == 26 or pinnumber == 27):
                        machinename = "aoi"

                mqttSendOn = 'sudo mosquitto_pub -h 192.168.88.1 -t /conveyer/%s -m ON' % machinename
                os.system(mqttSendOn)
                print mqttSendOn
                print 'pin number is %d\r\n' % pinnumber
                time.sleep(5)
                if(pinnumber != 27):
                        GPIO.output(23, GPIO.LOW)
                # SEND MQTT TO GATEWAY STOP
                mqttSendOff = 'sudo mosquitto_pub -h 192.168.88.1 -t /conveyer/%s -m OFF' % machinename
                os.system(mqttSendOff)
                print mqttSendOff

        if(pinnumber == 27):
                GPIO.output(23, GPIO.HIGH)
                GPIO.output(24, GPIO.HIGH)
                reverse = 1

while True:
        #print("in loop")
        #GPIO.wait_for_edge(23, GPIO.RISING)
        #print("Button 1 Pressed")
        #GPIO.wait_for_edge(23, GPIO.FALLING)
        #print("Button 1 Released")
        #GPIO.wait_for_edge(24, GPIO.FALLING)
        #print("Button 2 Pressed")
        #GPIO.wait_for_edge(24, GPIO.RISING)
        #print("Button 2 Released")
        if(GPIO.input(17) == 0):
                standardStep(17)
                curr_pin = 17
        elif(GPIO.input(22) == 0):
                standardStep(22)
                curr_pin = 22
        elif(GPIO.input(25) == 0):
                standardStep(25)
                curr_pin = 25
        elif(GPIO.input(26) == 0):
                standardStep(26)
                curr_pin = 26
        elif(GPIO.input(27) == 0):
                standardStep(27)
                curr_pin = 27
                #print("button =-==========================")
        time.sleep(0.01)
GPIO.cleanup()