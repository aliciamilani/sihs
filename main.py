import mqtt_connect
from weather_api import get_weather

# API

response = get_weather()

mqtt_connect.publish("est/si/sihs/weather", response)

