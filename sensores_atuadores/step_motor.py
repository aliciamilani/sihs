import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

control_pins = [4,17,27,22]

for pin in control_pins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,0)

halfstep_seq = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]
]

def setStepMotor(step,sent):
    # step = quantidade de passos
    # sent = sentido: 1 horario e 0 antihorario
    if sent == 0:
        control_pins = [4,17,27,22]
    else :
        control_pins = [22,27,17,4]

    for i in range(step):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins[pin],halfstep_seq[halfstep][pin])
            time.sleep(0.001)