#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Filename:          shutdownGpio.py
# Author:            Helpi
# Date:              2018-04-29
# Version:           1.0
# -----
# Last Modified:     
# Modified By:       
# 
###

import RPi.GPIO as GPIO
import subprocess
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(3, GPIO.FALLING)

os.system("shutdown -h now")