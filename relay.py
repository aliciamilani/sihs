import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
RELAIS_1_GPIO = 16
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)

def turn_on():
    GPIO.output(RELAIS_1_GPIO, True)

def turn_off():
    GPIO.output(RELAIS_1_GPIO, False)

for i in range(2):
    print('liga')
    turn_on() # on
    time.sleep(1)
    print('desliga')
    turn_off()
    time.sleep(1)

GPIO.cleanup()
