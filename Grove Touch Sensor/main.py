from machine import Pin   # Import Pin module from machine Class
touch=Pin('P12',mode=Pin.IN) # create a Pin instance as input Pin

while 1:
    if touch()==0:
        print("Not Detected")
    elif touch()==1:
        print("Detected")
