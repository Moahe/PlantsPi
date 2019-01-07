import RPi.GPIO as GPIO
import smtplib
import time

"""Test for raspberry pi with sensor"""

def callback(channel):
    if GPIO.input(channel):
        print("LED OFF")
    else:
        print("LED ON")


GPIO.setmode(GPIO.BCM)
channel = 17
GPIO.setup(channel, GPIO.IN)
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)

while True:
    time.sleep(3600)
