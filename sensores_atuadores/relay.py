import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
RELAIS_1_GPIO = 24
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)

def turn_on():
    GPIO.output(RELAIS_1_GPIO, False)

def turn_off():
    GPIO.output(RELAIS_1_GPIO, True)
