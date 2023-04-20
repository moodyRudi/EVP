#!/usr/bin/env python3
########################################################################
# Dateiname       : setAlarm.py
# Beschreibung    : Beim Drücken des Buttons wird eine Nachricht
#                   gesendet, die einen Alarm auslöst
# Autor           : Raphael Gardemann
# Letzte Änderung : 24.03.2023
########################################################################
import requests
import datetime
from datetime import datetime as date
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

lastMessageTimeStamp = date.now()
alarm = False
requestString = "http://192.168.2.109:8080/alarm/"
        
def checkAlarm():
    global alarm, lastMessageTimeStamp
    if (not alarm and GPIO.input(12)==GPIO.LOW):
        alarm = True
        requests.post(requestString + str(alarm))
        lastMessageTimeStamp = date.now()
        time.sleep(0.1)

def checkReset():
    global alarm, lastMessageTimeStamp
    if (alarm and GPIO.input(16)==GPIO.LOW):
        alarm = False
        requests.post(requestString + str(alarm))
        lastMessageTimeStamp = date.now()
        time.sleep(0.1)
    
def sendStatus():
    global lastMessageTimeStamp
    if (lastMessageTimeStamp + datetime.timedelta(0, 3) < date.now()):
        requests.post(requestString + str(alarm))
        lastMessageTimeStamp = date.now()

while(True):
    checkAlarm()
    checkReset()
    sendStatus()