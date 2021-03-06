#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)

TRIG = 24
ECHO = 23

print "Misuro la distanza..."

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)

print "Aspetto che il sensore sia comodo..."

time.sleep(2)

try:
	while True:

		GPIO.output(TRIG, True)
		time.sleep(0.00001)
		GPIO.output(TRIG, False)

		while GPIO.input(ECHO) == 0:
		    pulse_start = time.time()


		while GPIO.input(ECHO) == 1:
		    pulse_end = time.time()

		pulse_duration = pulse_end - pulse_start

		distance = pulse_duration * 17150

		distance = round(distance, 2)

		print "Distanza: ", distance, "cm"
		print "Come er cazzo tuo!"
		time.sleep(1)
except KeyboardInterrupt:
	pass

GPIO.cleanup()
