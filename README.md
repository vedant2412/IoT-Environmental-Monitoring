# IoT-Environmental-Monitoring
This Python script facilitates the generation and publication of simulated environmental sensor data to the ThingSpeak IoT platform.
The first step involves configuring the MQTT broker with the client ID, username, password, server address, and topics for CO2, humidity, and temperature readings. 
After that, Wi-Fi credentials are set up for network access. Within predetermined parameters, the script randomly generates temperature, humidity, and CO2 sensor data continually. 
A history log is used to store this data, guaranteeing five hours of information. 
The script publishes the sensor data to ThingSpeak on a regular basis via MQTT. It also prints the sensor readings that are generated to the console. 
The script continues the loop of creating, storing, and publishing data every 5 seconds indefinitely.
