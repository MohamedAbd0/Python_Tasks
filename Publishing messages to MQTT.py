"""
Created on Wed Oct 17 19:56:12 2018

@author: mohamed abdo elnashar

The objective of this post is to explain how to connect to a MQTT broker and post some messages 
to a topic, using Python.
"""

import paho.mqtt.client as mqttClient

# this data from (Instance info) cloudmqtt  -- https://customer.cloudmqtt.com/
broker_address= "m15.cloudmqtt.com"
port = 15318
user = "yuuiyxmb"
password = "Ua_a3EQR4Wpm"

Connected = True   
client = mqttClient.Client("Mohamed")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= Connected                      #attach function to callback
client.connect(broker_address, port=port)          #connect to broker

msg="hakona matata"
client.publish("python/test",msg)
client.disconnect()
client.loop_stop()
