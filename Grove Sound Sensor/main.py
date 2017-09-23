from machine import ADC, Pin   # Import ADC and Pin module from machine library
from time import sleep
adc=ADC()                      # crete an ADC instance
sound=adc.channel(pin='P13',attn=ADC.ATTN_11DB)   # create an adc channel on Pin P13
value=0

while 1:
    for i in range(32):  # create an average function
        value+=sound()
    value>>=5       # give average value
    print(value)          # print the value
    sleep(1)              # delay 1 sec
