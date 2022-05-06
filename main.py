from sqlalchemy import true
import mqtt_connect
# import time
from weather_api import get_weather
# from step_motor import setStepMotor
# from sensor_dht11 import dht11_read
# from relay import turn_on, turn_off

# API
response = get_weather()

relay_flag = "off"
stepmotor = "off"

for i in range(10):
    tempo = get_weather()

    # print(f"Tempo:{tempo}")
    # print("Motor girando sentido horario")

    # setStepMotor(512, 1)

    # temp_hum = dht11_read.read_temp_humidity()

    # if temp_hum:
    #     print(f"Temperatura: {temp_hum[0]}C")
    #     print(f"Umidade: {temp_hum[1]}%")
        
    # mqtt_connect.publish("est/si/sihs/ajv/weather", response)
    # mqtt_connect.publish("est/si/sihs/ajv/humidity", temp_hum[1])
    # mqtt_connect.publish("est/si/sihs/ajv/temperature", temp_hum[0])
    # mqtt_connect.publish("est/si/sihs/ajv/relay", relay_flag)
    # mqtt_connect.publish("est/si/sihs/ajv/stepmotor", stepmotor)

    mqtt_connect.publish("est/si/sihs/ajv/weather", "banana")
    mqtt_connect.publish("est/si/sihs/ajv/humidity", 74)
    mqtt_connect.publish("est/si/sihs/ajv/temperature", 40)
    mqtt_connect.publish("est/si/sihs/ajv/relay", "off")
    mqtt_connect.publish("est/si/sihs/ajv/stepmotor", "on")

    # subscribe("est/si/sihs/ajv/relay/cmd")
    # subscribe("est/si/sihs/ajv/stepmotor/cmd")

    # print("Ligando Rele")

    # turn_on()
    # time.sleep(1)

    # print("desligando rele")

    # turn_off()
