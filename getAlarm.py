import requests
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.LOW)

while(True):
    requestString = "http://192.168.2.109:8080/alarm"
    response = requests.get(requestString).text
    if (response == 'True'):
        GPIO.output(11, GPIO.HIGH)
    else:
        GPIO.output(11, GPIO.LOW)
    time.sleep(5)
