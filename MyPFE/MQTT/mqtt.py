
import json
from .models import Post

import paho.mqtt.client as mqtt
from django.conf import settings
from map.models import nodes

def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully')
        mqtt_client.subscribe('v3/loraatest02@ttn/devices/eui-70b3d57ed005a5c4/up')
        # mqtt_client.subscribe('#')

    else:
        print('Bad connection. Code:', rc)

def on_message(mqtt_client, userdata, msg):
    # Decode the incoming message
    payload_dict = json.loads(msg.payload)

   
    # node_id = payload_dict['node_id']

    
    # node = nodes.objects.get(id=node_id)

    # Get temperature and humidity values from payload
    temperature = payload_dict['uplink_message']['decoded_payload']['temperature']
    humidity = payload_dict['uplink_message']['decoded_payload']['humidity']

    # Create a new Post object and save it to the database
    post = Post(temperature=temperature, humidity=humidity)
    # , po=node
    post.save()


# def on_message(mqtt_client, userdata, msg):
#     # Decode the incoming message
#     payload_dict =json.loads(msg.payload)
#    # print(f'Received message on topic: {msg.topic} with payload: {msg.payload}')
#     projec_instance =nodes.objects.get(id=id)
#     # Get temperature and humidity values from payload
#     temperature = payload_dict['uplink_message']['decoded_payload']['temperature']
#     humidity = payload_dict['uplink_message']['decoded_payload']['humidity']
#     print('temperature :', temperature, 'humidity :', humidity,'\n')

#     # Create a new Post object and save it to the database
    
#     post = Post(temperature=temperature, humidity=humidity, po=projec_instance)
    
    
#     #  projec_instance = nodes.objects.get(id=id)
#     # postt_list = post.objects.filter(po=projec_instance).first
#     # post = Post.objects.order_by('-id').first()
#     post.save()
# all_post = Post.objects.all()



def start_mqtt_client():
    # Create a new MQTT client instance
    client = mqtt.Client()

    # Set the client's connection and message handling functions
    client.on_connect = on_connect
    client.on_message = on_message

    # Set the client's username and password
    client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)

    # Connect to the MQTT broker
    client.connect(
        host=settings.MQTT_SERVER,
        port=settings.MQTT_PORT,
        keepalive=settings.MQTT_KEEPALIVE
    )

    # Start the MQTT loop (this function blocks and waits for incoming messages)
    client.loop_forever()