#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import os

# Return CPU temperature as float
def getCPUtemp():
    cTemp = os.popen('vcgencmd measure_temp').readline()
    return float(cTemp.replace("temp=","").replace("'C\n",""))

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setwarnings(False)
p=GPIO.PWM(12, 100)
p.start(100)
time.sleep(1)

while True:
    CPU_temp = getCPUtemp()
    print(CPU_temp)

    if CPU_temp > 70.0:
        p.ChangeDutyCycle(100)
    elif CPU_temp > 60.0:
        p.ChangeDutyCycle(80)
    elif CPU_temp > 50.0:
        p.ChangeDutyCycle(60)
    elif CPU_temp > 45.0:
        p.ChangeDutyCycle(40)
    elif CPU_temp > 40.0:
        p.ChangeDutyCycle(20)
    elif CPU_temp > 30.0:
        p.ChangeDutyCycle(10)
    else:
        p.ChangeDutyCycle(0)
    
    time.sleep(30)

p.stop()

