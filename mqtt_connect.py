import random
from sensores_atuadores.control_relay_step import set_relay, set_window
import time
from paho.mqtt import client as mqtt_client

broker = 'test.mosquitto.org'
port = 1883
topic = "python/mqtt"

def connect_mqtt():

    client_id = f'python-mqtt-{random.randint(0, 1000)}'
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

client = connect_mqtt()
client_stepmotor = connect_mqtt()
client_relay = connect_mqtt()


def publish(topic, msg):
    result = client.publish(topic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        # print(f"Send to topic `{topic}`")
        return 1
    else:
        # print(f"Failed to send message to topic {topic}")
        return 0

def subscribe_stepmotor(topic):
    def on_message(client, userdata, msg):
        
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        if(msg.payload.decode() == "on"):
            print("entrou no on do motor")
            set_window("on")
        elif(msg.payload.decode() == "off"):
            print("entrou no off do motor")
            set_window("off")
    
    client_stepmotor.subscribe(topic)
    client_stepmotor.on_message = on_message

def subscribe_relay(topic):
    def on_message(client, userdata, msg):
        
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        if(msg.payload.decode() == "on"):
            print("entrou no on do relay")
            set_relay("on")
        elif(msg.payload.decode() == "off"):
            print("entrou no off do relay")
            set_relay("off")
    
    client_relay.subscribe(topic)
    client_relay.on_message = on_message

def start_subscribe_relay(topic, period):
    subscribe_relay(topic)
    while True:
        client_relay.loop()
        time.sleep(period)

def start_subscribe_stepmotor(topic, period):
    subscribe_stepmotor(topic)
    while True:
        client_stepmotor.loop()
        time.sleep(period)

#if __name__ == '__main__':
    #start_subscribe("est/si/sihs/ajv/stepmotor/cmd", 1)
