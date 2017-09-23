# Pysense is packed with a number of sensors and hardware. Here is the details of sensors
# USB Serial Converter
# 3-Axis Accelerometer (LIS2HH12)
# Battery Charger (BQ24040 with JST connector)
# Humidity and Temperature Sensor (Si7006-A20)
# Digital Ambient Light Sensor (LTR-329ALS-01)
# Barometric Pressure Sensor with Altimeter (MPL3115A2)
# MicroSD Card Reader
# All of the included sensors are connected to the Pycom device via the I2C interface. These pins are located at P22 (SDA) and P21 (SCL)

from pysense import Pysense                   # import pysense class from Pysense module
from LIS2HH12 import LIS2HH12                 # import 3 axis Accelerometer LIS2HH12 class from LIS2HH12 module
from SI7006A20 import SI7006A20               # import Humidity and Temperature sensor class from SI7006A20 module
from LTR329ALS01 import LTR329ALS01           # import Digital Ambient Light Sensor Class from LTR329ALS01 module
from MPL3115A2 import MPL3115A2               # import Barometric Pressure Sensor with Altimeter Class from MPL3115A2 module

py = Pysense()                                # create pysense instance
acc = LIS2HH12(py)                            # create Accelerometer instance
tempHum = SI7006A20(py)                       # create tempHum insatnce
ambientLight = LTR329ALS01(py)                # create ambientLight instance
pressure = MPL3115A2(py)                      # create pressure insatnce

# Read all the sensor  data/information from 3 axis Accelerometer
Axis=acc.read()                               # read the XYZ coordinates from the 3 axis Accelerometer as a tuple
X_Axis=Axis[0]                                # stored in X axis variable
Y_Axis=Axis[1]                                # stored in Y axis variable
Z_Axis=Axis[2]                                # stored in Z axis variable
Roll=acc.roll()                               # read the cuurent roll from the 3 axis Accelerometer in degrees
Pitch=acc.pitch()                             # read the cuurent pitch from the 3 axis Accelerometer in degrees
Yaw=acc.yaw()                                 # read the cuurent yaw from the 3 axis Accelerometer in degrees

# Read all the sensor  data/information from Humidity and Temperature Sensor
Temperature=tempHum.temp()                    # read the current Temperature from Humidity and Temperature sensor
Humidity=tempHum.humidity()                   # read the current Humidity from Humidity and Temperature sensor

# Read all the sensor  data/information from Digital Ambient Light Sensor
L=ambientLight.lux()                  # read the current positional light in lux as a tuple
Light_Lux=int(L[0])+int(L[1])/10      # convert it a single float value from a tuple
# Read all the sensor  data/information from pressure from Barometric Pressure sensor
Altitude=pressure.alt()               # read the current Altitude in meter
