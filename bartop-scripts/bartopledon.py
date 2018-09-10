#!/usr/bin/env python
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# enable power button LED
GPIO.setup(8, GPIO.OUT)
GPIO.output(8, GPIO.HIGH)

# enable bartop relays
GPIO.setup(16, GPIO.OUT)
GPIO.output(16, GPIO.HIGH)