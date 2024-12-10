import RPi.GPIO as GPIO
from time import sleep

from w1thermsensor import W1Thermsensor

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.IN)

led = 18
GPIO.setup(18, GPIO.OUT)
s = W1Thermsensor()

while True:
    temp_c = s.get_temperature()
    temp_f = s.get_temperature(Unit.DEGREES_F)
    temp_k = s.get_temperature(Unit.KELVIN)
    print(f"Temp in C:{temp_c}, Temp in F:{temp_f}, Temp in K :{temp_k}")

    # LED interfacing
    if int(temp_c) < 25:
        GPIO.output(led, GPIO.HIGH)
        print("LED on")
    
    else:
        GPIO.output(led, GPIO.LOW)
        print("LED off")
    sleep(5)