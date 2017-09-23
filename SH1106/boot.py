'''from machine import UART
from network import WLAN
import os , time
import config
uart = UART(0, 115200)
os.dupterm(uart)
wlan = WLAN(mode=WLAN.STA)
wlan.connect(ssid=config.WIFI_SSID, auth=(WLAN.WPA2,config.WIFI_PASS),timeout=5000)
while not wlan.isconnected():
    pass
    print("wifi is not connected! Please wait")
    time.sleep(1)
print(wlan.ifconfig()) # prints out local IP to allow for easy connection via Pymakr Plugin or FTP Client
'''
import config

known_nets = [(config.Home_SSID,config.Home_PASS),(config.Office_SSID,config.Office_PASS),(config.Office_SSID2,config.Office_PASS2)] # change this line to match your WiFi settings

import machine
import os
from time import sleep
uart = machine.UART(0, 115200) # disable these two lines if you don't want serial access
os.dupterm(uart)

#sd=machine.SD()
#os.mount(sd,'/sd')
if machine.reset_cause() != machine.SOFT_RESET: # needed to avoid losing connection after a soft reboot
    from network import WLAN
    wl = WLAN()

    # save the default ssid and auth
    original_ssid = wl.ssid()
    original_auth = wl.auth()

    wl.mode(WLAN.STA)

    available_nets = wl.scan()
    nets = frozenset([e.ssid for e in available_nets])

    known_nets_names = frozenset([e[0] for e in known_nets])
    net_to_use = list(nets & known_nets_names)

    try:
        net_to_use = net_to_use[0]
        pwd = dict(known_nets)[net_to_use]
        sec = [e.sec for e in available_nets if e.ssid == net_to_use][0]
        wl.connect(net_to_use, (sec, pwd), timeout=10000)
    except:
        wl.init(mode=WLAN.AP, ssid=original_ssid, auth=original_auth, channel=6, antenna=WLAN.INT_ANT)

sleep(10) # wait some time 10 sec
print("\n")
print("wifi is connected with "+ str(net_to_use))
print("wifi setting: "+ str(wl.ifconfig()))
