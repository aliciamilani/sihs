from .relay import turn_on, turn_off
from .step_motor import setStepMotor

relay_flag = "off"
window_flag = "off"

def set_relay(flag):
    global relay_flag
    relay_flag = flag
    if(flag == "on"):
        turn_on()
        relay_flag = "on"
    else:
        turn_off()
        relay_flag = "off"
        
def printar():
    print("window_flag no printar:", window_flag)
    
def set_window(flag):
    global window_flag
    window_flag = flag
    print("window_flag no set window:", window_flag)
    printar()
    if(flag == "on"):
        setStepMotor(512, 0)
    else:
        setStepMotor(512, 1)

def read_relay_flag():
    return relay_flag

def read_window_flag():
    return window_flag