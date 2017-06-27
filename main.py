from pycom import *            # import pycom module
from time import *             # import time module
import color
heartbeat(False)               # stop heartbeat pulse
while 1:       # stop after 10 cycles
    rgbled(color.Black)
    sleep(0.05)
    rgbled(color.White)
    sleep(0.05)
    rgbled(color.Red)
    sleep(0.05)
    rgbled(color.Green)
    sleep(0.05)
    rgbled(color.Blue)
    sleep(0.05)
    rgbled(color.Yellow)
    sleep(0.05)
    rgbled(color.Aqua)
    sleep(0.05)
    rgbled(color.Magenta)
    sleep(0.05)
