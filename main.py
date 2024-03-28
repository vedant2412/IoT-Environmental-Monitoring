import network
import time
import urandom
from umqtt.simple import MQTTClient

# Configuration for ThingSpeak MQTT
client_id = "KjsANxs2OiExLTYmEBUpIi8"
user = "KjsANxs2OiExLTYmEBUpIi8"
password = "sRG0rL9Ws23ln8SDPAFk4CYQ"
server = "mqtt3.thingspeak.com"
port = 1883
topic_temp = "channels/2488653/publish/fields/field1"
topic_humidity = "channels/2488653/publish/fields/field2"
topic_co2 = "channels/2488653/publish/fields/field3"

# Wi-Fi Connection Information
ssid = "Wokwi-GUEST"
passwrd = ""

# Store sensor data over time
data_log = []

# Generates random sensor values
def generate_simulated_sensor_data():
    temp = urandom.uniform(-50, 50)  #Temperature range : -50 Celsius to 50 Celsius 
    humidity = urandom.uniform(0, 100) #Humidity range : 0 to 100%
    co2 = urandom.uniform(300, 2000)  # CO2 range: 300 to 2000 ppm
    return temp, humidity, co2

# Publishes sensor data to ThingSpeak
def publish_data(temp, humidity, co2):
    mqtt_client = MQTTClient(client_id, server, user=user, password=password)
    mqtt_client.connect()
    mqtt_client.publish(topic_temp, str(temp))
    mqtt_client.publish(topic_humidity, str(humidity))
    mqtt_client.publish(topic_co2, str(co2))
    mqtt_client.disconnect()

# Wi-Fi setup and connection
network_interface = network.WLAN(network.STA_IF)
network_interface.active(True)
network_interface.connect(ssid, passwrd)

# Wait until connected to Wi-Fi
while not network_interface.isconnected():
    pass
print("Wi-Fi Connected Successfully")

# Main operation loop
while True:
    temp, humidity, co2 = generate_simulated_sensor_data()
    data_log.append((temp, humidity, co2))  # Append new data to log
    if len(data_log) > 720:  # Limit log size to approx 5 hours (@ 5-second intervals)
        data_log.pop(0)  # Remove oldest entry
    publish_data(temp, humidity, co2)
    print(f"Published: Temperature={temp:.2f}C, Humidity={humidity:.2f}%, CO2={co2:.2f}ppm")
    time.sleep(5)  # Interval between data publications
