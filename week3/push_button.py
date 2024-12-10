import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

btn = 16
led = 14

GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.pull_up)
GPIO.setup(led, GPIO.OUT)

while True:
    btn_state = GPIO.input(btn)
    print(btn_state)
    if btn_state == 0:
        GPIO.output(led, GPIO.HIGH)
        print("LED on")
    else:
        GPIO.output(led, GPIO.LOW)
        print("LED off")
    sleep(1)