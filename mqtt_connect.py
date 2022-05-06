import random
# from main import set_relay, set_window
import time
from paho.mqtt import client as mqtt_client
# from relay import turn_on, turn_off
# from step_motor import setStepMotor

broker = 'test.mosquitto.org'
port = 1883
topic = "python/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public

def connect_mqtt():
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

# def run():
    # publish
    # # client.loop_start()
    # publish(client)
    
    # subscribe
    # subscribe("est/si/sihs/ajv/weather")
    # client.loop_forever()

def start_subscribe(topic):
    subscribe(topic)
    while True:
        client.loop()
        time.sleep(10)

def subscribe(topic):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        print("funciona pf")
        # if(msg.payload.decode() == "onRelay"):
        #     turn_on()
        #     set_relay("on")
        # elif(msg.payload.decode() == "offRelay"):
        #     turn_off()
        #     set_relay("off")
        # elif(msg.payload.decode() == "onWindow"):
        #     setStepMotor(512, 0)
        #     set_window("on")
        # elif(msg.payload.decode() == "offWindow"):
        #     setStepMotor(512, 1)
        #     set_window("off")
        # return msg.payload.decode()
    client.subscribe(topic)
    client.on_message = on_message

if __name__ == '__main__':
    start_subscribe("test/python")
