import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ir = 14
led = 16

GPIO.setup(ir, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

while True:
    state = GPIO.input(ir)
    if state == 0:
        GPIO.output(led, GPIO.HIGH)
        print("LED on")
    else:
        GPIO.output(led, GPIO.LOW)
        print("LED off")