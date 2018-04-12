import paho.mqtt.client as mqtt

# This is the Publisher

client = mqtt.Client()
client.connect("192.168.1.3",1883,60)
text = str(input())
while text != 'quit':
    client.publish("topic/test", text);
    text = input();
client.disconnect();
