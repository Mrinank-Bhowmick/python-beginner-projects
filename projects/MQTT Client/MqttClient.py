from paho.mqtt import client as mqtt_client
from random import randint
from decouple import config

# Reading broker credentials
BROKER = config("BROKER")
PORT = int(config("PORT"))
TOPIC = config("TOPIC")
USER = config("USER")
PASS = config("PASS")

# Create a randdom id for login in MQTT
CLIENT_ID = f"id-mqtt-{randint(0,100)}"


# Create a client to interact with MQTT
def connectMqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("[MQTT] Connected to server.")
        else:
            print("[MQTT] Failure to connect.")

    client = mqtt_client.Client(CLIENT_ID)
    client.username_pw_set(USER, PASS)
    client.on_connect = on_connect
    client.connect(BROKER, PORT)

    return client


# Receiving messages sendings with MQTT
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(
            f"[MQTT] Received message from {msg.topic} topic:",
            f"\n{msg.payload.decode()}",
        )

    client.subscribe(TOPIC)
    client.on_message = on_message


# Publishing messages with MQTT
def publish(client, msg="Hello MQTT"):
    result = client.publish(TOPIC, msg)


if __name__ == "__main__":
    client = connectMqtt()
    subscribe(client)
    publish(client)
    publish(client, msg="Custom Messages Working!")
    client.loop_forever()
