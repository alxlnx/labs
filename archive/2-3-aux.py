import RPi.GPIO as GPIO
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]

GPIO.setmode(GPIO.BCM)

# for pin in leds:
#     GPIO.setup(pin, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)

# for pin in aux:
#     GPIO.setup(pin, GPIO.IN)
GPIO.setup(aux, GPIO.OUT)

while(1):
    for i in range(len(leds)):
        state = GPIO.input(aux[i])
        GPIO.output(leds[i], state)