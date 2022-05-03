import mqtt_connect
import time
from weather_api import get_weather
from step_motor import setStepMotor
from sensor_dht11 import dht11_read
from relay import turn_on, turn_off

# API

#response = get_weather()

#mqtt_connect.publish("est/si/sihs/weather", response)

for i in range(10):
    tempo = get_weather()
    print(f"Tempo:{tempo}")
    print("Motor girando sentido horario")
    setStepMotor(512, 1)
    temp_hum = dht11_read.read_temp_humidity()
    if temp_hum:
        print(f"Temperatura: {temp_hum[0]}C")
        print(f"Umidade: {temp_hum[1]}%")
    print("Ligando Rele")
    turn_on()
    time.sleep(1)
    print("desligando rele")
    turn_off()
