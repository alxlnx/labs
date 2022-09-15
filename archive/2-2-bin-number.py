import RPi.GPIO as GPIO
import time
from random import randint

print()
dac = [10, 9, 11, 5, 6, 13, 19, 26]
number = [-1] * len(dac)

GPIO.setmode(GPIO.BCM)

# for pin in dac:
#     GPIO.setup(pin, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)

# number = [number[i] = randint(0,1) for i in range(len(number)
for i  in range(len(number)):
    number[i] = randint(0, 1)

# number = [1, 1, 1, 1, 1, 1, 1, 1] # 255
# number = [0, 1, 1, 1, 1, 1, 1, 1] # 127
# number =  [0, 1, 0, 0, 0, 0, 0, 0] # 64
# number = [0, 0, 1, 0, 0, 0, 0 , 0] # 32
# number = [0, 0, 0, 0, 0, 1, 0, 1] # 5
# number = [0, 0, 0, 0, 0, 0, 0, 0] # 0

print("Data to be diplayed: ", number)
for led, state in zip(dac, list(reversed(number))):
    GPIO.output(led, state)

time.sleep(15)

# for pin in dac:
#     GPIO.output(pin, 0)
GPIO.output(dac, 0)

GPIO.cleanup()