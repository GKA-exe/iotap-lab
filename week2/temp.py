import RPi.GPIO as GPIO
from time import sleep

from w1thermsensor import W1Thermsensor

s = W1Thermsensor()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.IN)

while True:
    temp = s.get_temperature()
    print(f"Temp is {temp}")
    sleep(5)