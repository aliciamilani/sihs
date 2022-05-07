#from sqlalchemy import true
import mqtt_connect
import threading
import time
from weather_api import get_weather
from sensor_dht11 import dht11_read
from control_relay_step import set_relay, set_window, read_relay_flag, read_window_flag
from database.insert_table import insert_historics, search_climate, commit_close


import datetime

list_bad_weather = ['Rain', 'Thunderstorm', "Drizzle", "Squall"]

topic_stepmotor = threading.Thread(target=mqtt_connect.start_subscribe_stepmotor, args=("est/si/sihs/ajv/stepmotor/cmd", 10))
topic_stepmotor.start()

topic_relay = threading.Thread(target=mqtt_connect.start_subscribe_relay, args=("est/si/sihs/ajv/relay/cmd", 12))
topic_relay.start()


while True:
    
    current = datetime.datetime.now()
    
    print("vai ler")

    temp_humid = dht11_read.read_temp_humidity()
    print('Variavel', temp_humid)
    if temp_humid:
        temp = temp_humid[0]
        humid = temp_humid[1]
    else:
        time.sleep(2)
        continue

    weather = get_weather()
    mqtt_connect.publish("est/si/sihs/ajv/weather", weather)
    
    if (weather in list_bad_weather or humid <= 60):
        set_window("off")
        set_relay("off")

    else:
        if (humid > 60 and humid <= 80):
            set_window("on")
            set_relay("off")

        elif (humid > 80):
            set_window("on")
            set_relay("on")

    window = read_window_flag()
    relay = read_relay_flag()
    
    mqtt_connect.publish("est/si/sihs/ajv/stepmotor", window)
    mqtt_connect.publish("est/si/sihs/ajv/relay", relay)
    mqtt_connect.publish("est/si/sihs/ajv/weather", weather)
    mqtt_connect.publish("est/si/sihs/ajv/temperature", int(temp))
    mqtt_connect.publish("est/si/sihs/ajv/humidity", humid)
    
    weather_db = search_climate(weather)
    
    insert_historics("Relay", read_relay_flag(), current.date(), current.time(), 
                    humid, temp, weather_db, 1)
    
    insert_historics("Window", read_window_flag(), current.date(), current.time(), 
                    humid, temp, weather_db, 1)

    
    print('enviou')

    time.sleep((10*60))
