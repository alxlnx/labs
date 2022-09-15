import RPi.GPIO as GPIO
import time

print("Starting...")
leds = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setmode(GPIO.BCM)

for led in leds:
    GPIO.setup(led, GPIO.OUT)

for j in range(3):
    for i in leds:
        GPIO.output(i, 1)
        time.sleep(0.2)
        GPIO.output(i, 0)

for led in leds: GPIO.output(led, 0)

GPIO.cleanup()
print("Bye")