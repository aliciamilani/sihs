#from sqlalchemy import true
import mqtt_connect
import time
from weather_api import get_weather
from sensor_dht11 import dht11_read
from control_relay_step import set_relay, set_window, read_relay_flag, read_window_flag
from database.insert_table import insert_historics, search_climate, commit_close


import datetime
current = datetime.datetime.now() 

list_bad_weather = ['Rain', 'Thunderstorm', "Drizzle", "Squall"]

#mqtt_connect.start_subscribe("est/si/sihs/ajv/relay/cmd")
#mqtt_connect.start_subscribe("est/si/sihs/ajv/stepmotor/cmd")


while True:
    
    print("vai ler")

    temp_humid = dht11_read.read_temp_humidity()
    print('Variavel', temp_humid)
    if temp_humid:
        temp = temp_humid[0]
        humid = temp_humid[1]
    else:
        time.sleep(2)
        continue
    mqtt_connect.publish("est/si/sihs/ajv/temperature", temp)
    mqtt_connect.publish("est/si/sihs/ajv/temperature", humid)

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
    print("flags:", window)
    mqtt_connect.publish("est/si/sihs/ajv/stepmotor", window)
    mqtt_connect.publish("est/si/sihs/ajv/relay", relay)

    time.sleep(5)

    insert_historics("Relay", read_relay_flag(), current.date(), current.time(), 
                    humid, temp, search_climate(weather), 1)

    time.sleep(5)

    insert_historics("Window", read_window_flag(), current.date(), current.time(), 
                    humid, temp, search_climate(weather), 1)
    
    commit_close()
    
    print('enviou')

    time.sleep((10*60))
