import RPi.GPIO as GPIO
import dht11
import time

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()

# read data using Pin GPIO23
instance = dht11.DHT11(pin=23)

def read_temp_humidity():
    result = instance.read()
    if result.is_valid():
        return [result.temperature, result.humidity]
    else:
        return 0

#while True:
    #result = read_temp_humidity()
    #print("Temp: %d C" % result.temperature +' '+"Humid: %d %%" % result.humidity)
    #print(f"Temp: {result[0]} Hum: {result[1]}")
    #time.sleep(1)
