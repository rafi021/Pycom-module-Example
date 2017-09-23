from machine import I2C, Pin
from time import sleep
import ssd1306
from bmp180 import BMP180

i2c=I2C(0,I2C.MASTER)
d=ssd1306.SSD1306_I2C(128,64,i2c)
sen=BMP180(i2c)
d.fill(0)
d.show()
while 1:
    d.text("P:{:.2f} bar".format(sen.pressure/1000),0,0)
    d.text("T:{:.2f} *C".format(sen.temperature),0,12)
    d.text("A:{:.2f} m".format(sen.altitude),0,24)
    d.show()
    sleep(2)
    d.fill(0)
