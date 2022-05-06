from sqlalchemy import true
import mqtt_connect
import time
from weather_api import get_weather
from step_motor import setStepMotor
from sensor_dht11 import dht11_read
from relay import turn_on, turn_off

#flags
relay_flag = "off"
window_flag = "off"

def set_relay(flag):
    relay_flag = flag

def set_window(flag):
    window_flag = flag

list_bad_weather = ['rain', 'thunderstorm']

mqtt_connect.start_subscribe("est/si/sihs/ajv/relay/cmd")
mqtt_connect.start_subscribe("est/si/sihs/ajv/stepmotor/cmd")

while True:

    temp, humid = dht11_read.read_temp_humidity()
    mqtt_connect.publish("est/si/sihs/ajv/temperature", temp)
    mqtt_connect.publish("est/si/sihs/ajv/temperature", humid)

    weather = get_weather()
    mqtt_connect.publish("est/si/sihs/ajv/weather", weather)

    if(humid >= 60 and weather not in list_bad_weather):
        setStepMotor(512, 0)
        window = "on"
        if(humid >= 80):
            turn_on()
            relay_flag = "on"
        elif(humid < 80):
            turn_off()
            relay_flag = "off"
        #registrar no bd
    elif(humid <= 50):
        setStepMotor(512, 1)
        window = "off"
        turn_off()
        relay_flag = "off"
    elif(temp > 26):
        turn_on()
        relay_flag = "on"
        if(weather not in list_bad_weather):
            setStepMotor(512, 0)
            window_flag = "on"
    else:
        turn_off()
        relay_flag = "off"
        setStepMotor(512, 1)
        window_flag = "off"

    mqtt_connect.publish("est/si/sihs/ajv/stepmotor", window_flag)
    mqtt_connect.publish("est/si/sihs/ajv/relay", relay_flag)

    time.sleep((10*60))

#BANCO #BANCO #BANCO #BANCO #BANCO #BANCO #BANCO #BANCO #BANCO
