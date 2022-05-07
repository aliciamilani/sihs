#from sqlalchemy import true
import mqtt_connect
import time
from weather_api import get_weather
from sensor_dht11 import dht11_read
from control_relay_step import set_relay, set_window, read_relay_flag, read_window_flag
from database import insert_table


import datetime
current = datetime.datetime.now() 

list_bad_weather = ['Rain', 'Thunderstorm', "Drizzle", "Squall"]

#mqtt_connect.start_subscribe("est/si/sihs/ajv/relay/cmd")
#mqtt_connect.start_subscribe("est/si/sihs/ajv/stepmotor/cmd")


while True:
    
    print("vai ler")

    temp_humid = dht11_read.read_temp_humidity()
    if temp_humid:
        temp = temp_humid[0]
        humid = temp_humid[1]
    else:
        pass
    mqtt_connect.publish("est/si/sihs/ajv/temperature", temp)
    mqtt_connect.publish("est/si/sihs/ajv/temperature", humid)

    weather = get_weather()
    mqtt_connect.publish("est/si/sihs/ajv/weather", weather)

    if(humid >= 60 and weather not in list_bad_weather):
        set_window("on")
        if(humid >= 80):
            set_relay("on")
        elif(humid < 80):
            set_relay("off")

    elif(humid <= 50):
        set_window("off")
        set_relay("off")

    elif(temp > 26):
        set_relay("on")
        if(weather not in list_bad_weather):
            set_window("on")
    else:
        set_window("off")
        set_relay("off")
    
    window = read_window_flag()
    relay = read_relay_flag()
    print("flags:", window)
    mqtt_connect.publish("est/si/sihs/ajv/stepmotor", window)
    mqtt_connect.publish("est/si/sihs/ajv/relay", relay)

    time.sleep(10)

    insert_table.insert_historics("Relay", read_relay_flag(), current.date(), current.time(), 
                    humid, temp, insert_table.search_climate(weather), 1)

    time.sleep(10)

    insert_table.insert_historics("Window", read_window_flag(), current.date(), current.time(), 
                    humid, temp, insert_table.search_climate(weather), 1)

    time.sleep((10*60))
