from mqtt import MQTTClient         # import MQTTClient class from mqtt.py file
from machine import Pin             # import Pin and  Class from machine module
from time import sleep              # import sleep class from time module
import config                       # import config module
import pysense_board                # import pysense_board module

pin=Pin('P10',mode=Pin.IN,pull=Pin.PULL_UP) # create a Pin instance using Pin class
recv=0                              # recv variable for data subscribe
def set_timeout(duration):
    pass

def sub_cb(topic,recv):
    print(recv)

# create client instance using MQTTClient class
#client=MQTTClient(client_id="lopy",server="test.mosquitto.org",port=1883,password=None,keepalive=0,ssl=False,ssl_params={})
# client=MQTTClient("client_id","io.adafruit.com",user="your_username",password="your_api_key",port=1883)
client=MQTTClient(config.CLIENT_ID,config.SERVER,user=config.USERNAME,password=config.PASSWORD,port=config.PORT)
client.set_timeout=set_timeout       # time out seeting for client
client.set_callback(sub_cb)          # subscribe callback msg for client

# Now connect to MQTT Borker
print("Connecting to MQTT Broker")   # msg for user
done=client.connect()                # connect to MQTT server
if done ==0:                         # check if Connected or not
    print("Connected!\n")            #Connection done msg
else:                                # if not connected
    pass                             # Retry
    print("Not Connected!!!\n")      # Not connected msg
client.publish(topic="mahmud021/feeds/text",msg=str("Pysense-Board")) # publish msg
print("Published!")                  # publish done msg
sleep(1)                            # delay 10 sec
client.subscribe(topic="mahmud021/feeds/onoff") # set subscribe topic
print("Subscribed!")                 # if subscribe, then show msg

count=0
while True:
    bat=apin()
    client.check_msg()            # check for any new subscribe
    if recv == 'OFF':
        print("LED OFF")
    elif recv == 'ON':
        print("LED ON")
    if pin() ==1:
        count+=1
        sleep(5)                      # delay 5 sec
        client.publish(topic="mahmud021/feeds/text",msg=str("Counter: ")+str(count))
        sleep(5)
        client.publish(topic="mahmud021/feeds/text",msg=str("X_Axis: ")+str(pysense_board.X_Axis)+str(" Y_Axis: ")+str(pysense_board.Y_Axis)+str(" Z_Axis: ")+str(pysense_board.Z_Axis))
        sleep(5)
        client.publish(topic="mahmud021/feeds/text",msg=str("Roll: ")+str(pysense_board.Roll)+str(" degrees"))
        sleep(5)
        client.publish(topic="mahmud021/feeds/text",msg=str("Pitch: ")+str(pysense_board.Pitch)+str(" degrees"))
        sleep(5)
        client.publish(topic="mahmud021/feeds/text",msg=str("Yaw: ")+str(pysense_board.Yaw)+str(" degrees"))
        sleep(5)
        client.publish(topic="mahmud021/feeds/text",msg=str("Temperature: ")+str(pysense_board.tempHum.temp())+str(" *C"))
        sleep(5)
        client.publish(topic="mahmud021/feeds/text",msg=str("Humidity: ")+str(pysense_board.Humidity)+str(" %RH"))
        sleep(5)
        client.publish(topic="mahmud021/feeds/text",msg=str("AmbientLight: ")+str(pysense_board.Light_Lux)+str(" Lux"))
        sleep(5)
        client.publish(topic="mahmud021/feeds/text",msg=str("Altitude: ")+str(pysense_board.Altitude)+str(" Meter"))
        sleep(5)
    else:                             # if interrupted by pin press
        break                         # restart
