""" LoPy LoRaWAN Nano Gateway configuration options """

import machine
import binascii

WIFI_MAC = binascii.hexlify(machine.unique_id()).lower()
# Set  the Gateway ID to be the first 3 bytes of MAC address + 'FFFE' + last 3 bytes of MAC address
# GATEWAY_ID = WIFI_MAC[:6] + "f0fc" + WIFI_MAC[6:12]
GATEWAY_ID='240ac4f0fcac400f'
SERVER = 'router.eu.thethings.network'#'router.eu.thethings.network'
PORT = 1700

NTP = "pool.ntp.org"
NTP_PERIOD_S = 3600

WIFI_SSID = 'wifi_ssid'
WIFI_PASS = '**********'

LORA_FREQUENCY = 868100000
LORA_DR = "SF7BW125" # DR_5
