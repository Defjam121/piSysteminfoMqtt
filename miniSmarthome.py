#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Filename:          miniSmarthome.py
# Author:            Helpi
# Date:              2018-04-29
# Version:           1.0
# -----
# Last Modified:     
# Modified By:       
# 
###

import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
import thread
import Adafruit_DHT
 

dia_chi_ip_mosquitto = "127.0.0.1"
 
#dinh nghia chan relay
relay1 = 4
relay2 = 7
# chan DATA duoc noi vao chan GPIO24 cua PI
pin_sensor = 13
chon_cam_bien = Adafruit_DHT.DHT11
 
#chuong trinh se lang nghe nhung message lien quan den relay 
topic1 = "room1/switch1"
topic2 = "room1/switch2"
#chuong trinh se gui message "temperature" den Mosquiito server sau khi do nhiet do, do am tu DHT11
topic3 = "room1/temperature"
#bien state1 va state2 de luu gia tri hien tai cua 2 relays
state1 = "0"
state2 = "0"
#cai dat 2 chan dieu khien relays
GPIO.setmode(GPIO.BCM) # chon kieu danh so chan GPIO la BCM
GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)
#thiet lap gia tri ban dau la HIGH de mo relay
GPIO.output(relay1, GPIO.HIGH)
GPIO.output(relay2, GPIO.HIGH)
 
print ("RASPI.VN Demo SIMPLE SMARTHOME");
 
# Ham do nhiet do va do am
def dht11_thread( threadName, delay):
    global state1
    global state2
    time.sleep(delay)
 
    while(1):
        # Doc Do am va Nhiet do tu cam bien thong qua thu vien Adafruit_DHT
        # Ham read_retry se doc gia tri Do am va Nhiet do cua cam bien neu khong thanh cong se thu 15 lan, moi lan cach nhau 2 giay
        do_am, nhiet_do = Adafruit_DHT.read_retry(chon_cam_bien, pin_sensor);
        # kiem tra gia tri tra ve tu cam bien (do _am va nhiet_do) khac NULL
        if do_am is not None and nhiet_do is not None:
            ketquado = str(("{0:0.1f}-{1:0.1f}\n").format(nhiet_do, do_am));
            print(ketquado)
            publish.single(topic3, ketquado, hostname=dia_chi_ip_mosquitto) #dien IP cua Pi
            publish.single(topic1, state1, hostname=dia_chi_ip_mosquitto)
            publish.single(topic2, state2, hostname=dia_chi_ip_mosquitto)
            time.sleep(2)
        else:
        # Loi 
            print("Loi khong the doc tu cam bien DHT11 :(\n")
 
def on_connect(mqttc, obj, flags, rc):
    pass
    
#ham nay se duoc goi khi nhan duoc message tu Mosquiito server
def on_message(mqttc, obj, msg):
    global state1
    global state2
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    
    if(msg.topic == topic1):
        if(str(msg.payload) == "1"): #bat LED
            GPIO.output(relay1, GPIO.LOW)
        elif(str(msg.payload) == "0"): #tat LED
            GPIO.output(relay1, GPIO.HIGH)
        state1 = str(msg.payload)
        
    elif(msg.topic == "room1/switch2"):
        if(str(msg.payload) == "1"): #bat LED
            GPIO.output(relay2, GPIO.LOW)
        elif(str(msg.payload) == "0"): #tat LED
            GPIO.output(relay2, GPIO.HIGH)
        state2 = str(msg.payload)
 
#ham nay se duoc goi sau khi chuong trinh gui messag toi Mosquiito server
def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))
 
def on_subscribe(mqttc, obj, mid, granted_qos):
    pass
 
def on_log(mqttc, obj, level, string):
    pass
 
 #tao MQTT client va dang ki cac ham callback
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
 
#ket noi den Mosquiito server
mqttc.connect(dia_chi_ip_mosquitto, 1883, 60) #dien IP cua Pi
mqttc.subscribe(topic1, 0)
mqttc.subscribe(topic2, 0)
 
# Tao Tac vu do va gui nhiet do, do am voi gia tri hien tai cua relays chay song song voi tac vu MQTT client
try:
   thread.start_new_thread( dht11_thread, ("DHT 11", 4, ) )
except:
   print "Loi khoi tao DHT11"
 
mqttc.loop_forever()