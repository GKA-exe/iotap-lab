import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

led = 18

GPIO.setup(led, GPIO.OUT)

while(True):
    inp = input()

    if(inp.lower() == "on"):
        GPIO.output(led, GPIO.HIGH)
        print("LED on")
    else:
        GPIO.output(led, GPIO.LOW)
        print("LED off")