from machine import Pin,I2C
from time import sleep
from sh1106 import SH1106_I2C
from bmp180 import BMP180
from machine import RTC

datetime=[] # Create a list
hour=0
minitue=0
rtc=RTC()   # Create a RTC instance
rtc.ntp_sync('bd.pool.ntp.org')  # sync ntp data from bd ntp server
while rtc.synced()!=True:          # wait until ntp server is synced
    print(rtc.now())

sda=Pin('P9')
scl=Pin('P10')
i2c=I2C(0,I2C.MASTER,pins=(sda,scl)) # Create an I2C instance
print("I2C scan devices:",i2c.scan())
bmp=BMP180(i2c)                     # Create a bmp180 instance
bmp.oversample_sett=2
bmp.baseline=101325.0
display=SH1106_I2C(128,64,i2c,None,0x3c)
display.sleep(False)  # Disable SH1106 OLED sleep
display.fill(0)       # Clear display
display.show()        # show the content in OLED display

while 1:
    datetime=list(rtc.now())
    date=str(datetime[2])+str('/')+str(datetime[1])+str('/')+str(datetime[0]-2000)
    hour=datetime[3]-6
    minitue=datetime[4]
    if hour>11 and hour<24:
        am_pm='AM'
    else:
        am_pm='PM'
    if hour>12:
        hour=hour-12
    else:
        hour=hour
    time=str(hour)+str(':')+str(minitue)+str(am_pm)
    t=bmp.temperature    # get the temperature
    p=bmp.pressure/100   # get the pressure
    a=bmp.altitude       # get the altitude
    # display temperature, pressure and altitude value in OLED display
    display.text("Temp:{:0.2f} *C".format(t),0,0,1)
    display.text("Pres:{:0.1f} mbar".format(p),0,10,1)
    display.text("Alt:{:0.2f} m".format(a),0,20,1)
    display.text(date,0,30,1)
    display.text(time,70,30,1)
    display.show()
    sleep(1)
    print(date,time,"Temp:{:0.2f} *C, Pressure:{:0.2f} mbar, Altitude:{:0.2f} m".format(t,p,a))
    display.fill(0)
    display.show()
