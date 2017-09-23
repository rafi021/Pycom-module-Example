from machine import I2C
from pycom import *
import color
from time import sleep
from gesture import Gesture
i2c=I2C(0,I2C.MASTER)
g=Gesture(i2c)
heartbeat(False)
# 	0:nothing  ->Black
# 	1:Forward  -> Red
# 	2:Backward -> Green
# 	3:Right    -> Yellow
# 	4:Left     -> Blue
# 	5:Up       -> White
# 	6:Down     -> Aqua
# 	7:Clockwise -> Magenta
# 	8:anti-clockwise -> Mix Green|Red
# 	9:wave           -> Mix Green| Blue
while 1:
    #g.print_gesture()
    value=g.return_gesture()
    print(value)
    if value==0:
        rgbled(color.Black)   # nothing
    if value==1:
        rgbled(color.Green)   # Forward
    if value==2:
        rgbled(color.Red)     # Backward
    if value==3:
        rgbled(color.Yellow)  # Right
    if value==4:
        rgbled(color.Blue)    # Left
    if value==5:
        rgbled(color.White)   # Up
    if value==6:
        rgbled(color.Aqua)    # Down
    if value==7:
        rgbled(color.Magenta) # Clockwise
    if value==8:
        rgbled(color.Green|color.Red) # anti-clockwise
    if value==9:
        rgbled(color.Green|color.Blue) # Wave
    sleep(1)
