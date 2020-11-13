import paho.mqtt.client as mqtt
import time
from time import gmtime, strftime
import sqlite3
import datetime
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SOLAR.settings")
django.setup()
from coreApp.models import SocDoc
listen_Topic = "SOLAR/SocDoc_Update"

dbFile = 'db.sqlite3'

#these functions are for MQTT
#should process the received message
#message format is stateOfCharge/

def on_message(client, userdata, msg):
    if msg.topic == listen_Topic:
        print(msg.topic+ " " + str(msg.payload))
        m1 = str(msg.payload)

        #divide the string using split method
        first_1 = m1.split('/')
        stateOC = first_1[0]
        depthOC = first_1[1]
        loadsConnec = first_1[2]

         #add date
        date1 = datetime.datetime.now().time()
        print(date1)
        print("Saving")

        data_saving = SocDoc(stateOfCharge = stateOC, depthOfCharge = depthOC, loadsConnected = loadsConnec, timeStamp = date1)
        data_saving.save()

def on_log(client, userdata, level, buf):
    print("Log: "+buf)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected")
        client.subscribe(listen_Topic)
       # client.publish(the_topic, '653434')
       # client.subscribe(the_topic)
    else:
        print("Bad connection")


def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected Client. Result code" +str(rc))



client = mqtt.Client("FirstTest", clean_session=True)
client.on_connect = on_connect
client.on_log = on_log
client.on_disconnect = on_disconnect
client.on_message = on_message
username = "qxthyopl"
password = "VcMajZtxlQVJ"
url = "tailor.cloudmqtt.com"#urlparse.urlparse(url_str)
client.username_pw_set(username, password)
client.connect(url, 12702)
client.subscribe(listen_Topic,1)
#client.publish("house/sensor1", "my_ first message")
client.loop_forever()