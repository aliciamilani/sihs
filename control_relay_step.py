from relay import turn_on, turn_off
from step_motor import setStepMotor
import time

relay_flag = "off"
window_flag = "off"

def set_relay(flag):
    relay_flag = flag
    if(flag == "on"):
        turn_on()
    else:
        turn_off()

def set_window(flag):
    window_flag = flag
    if(flag == "on"):
        setStepMotor(512, 0)
    else:
        setStepMotor(512, 1)

def read_relay_flag():
    return relay_flag

def read_window_flag():
    return window_flag