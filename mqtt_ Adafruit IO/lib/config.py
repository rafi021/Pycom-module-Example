import machine
import binascii

WIFI_MAC = binascii.hexlify(machine.unique_id()).upper()
# Set  the Gateway ID to be the first 3 bytes of MAC address + 'FFFE' + last 3 bytes of MAC address
GATEWAY_ID = WIFI_MAC[:6] + "FFFE" + WIFI_MAC[6:12]

SERVER = 'io.adafruit.com'
PORT = 1883

#NTP = "pool.ntp.org"
#NTP_PERIOD_S = 3600

Home_SSID    = '************'
Home_PASS    = '************'
Office_SSID  = '************'
Office_PASS  = '************'
Office_SSID2  = '***********'
Office_PASS2  = '***********'


#LORA_FREQUENCY = 915000000
#LORA_DR = "SF7BW125" # DR_5

#adafruit io details
CLIENT_ID="user_id"
USERNAME="user_id"
PASSWORD="ebfef4112b6647afb377fc0931d0e342"
