from machine import UART
from time import sleep

setAddrBytes 		=	[0xB4,0xC0,0xA8,0x01,0x01,0x00,0x1E]
readVoltageBytes 	= 	[0xB0,0xC0,0xA8,0x01,0x01,0x00,0x1A]
readCurrentBytes 	= 	[0XB1,0xC0,0xA8,0x01,0x01,0x00,0x1B]
readPowerBytes 		= 	[0XB2,0xC0,0xA8,0x01,0x01,0x00,0x1C]
readEnergyBytes 	= 	[0XB3,0xC0,0xA8,0x01,0x01,0x00,0x1D]

class pzem:

    def __init__(self,uart_id,baudrate):
        self.uart_id=uart_id
        self.baudrate=baudrate
        self.uart=UART(self.uart_id,baudrate=self.baudrate)

    def isReady(self):
        self.uart.write(bytearray(setAddrBytes))
        rcv=self.uart.read(7)
        sleep(0.1)
        if rcv[0]==0xA4:
            print("PZEM-04T is Ready to Communicate")
        else:
            print("Check connection!!")

    def readVoltage(self):
        self.uart.write(bytearray(readVoltageBytes))
        rcv=self.uart.read(7)
        sleep(0.1)
        if rcv[0]==0xA0:
            return rcv[2]+rcv[3]/10
        else:
            return 0.0

    def readCurrent(self):
        self.uart.write(bytearray(readCurrentBytes))
        rcv=self.uart.read(7)
        sleep(0.1)
        if rcv[0]==0xA1:
            return rcv[2]+rcv[3]/10
        else:
            return 0.0
    def readPower(self):
        self.uart.write(bytearray(readPowerBytes))
        rcv=self.uart.read(7)
        sleep(0.1)
        if rcv[0]==0xA2:
            return rcv[2]+rcv[3]/10
        else:
            return 0.0
    def readEnergy(self):
        self.uart.write(bytearray(readEnergyBytes))
        rcv=self.uart.read(7)
        sleep(0.1)
        if rcv[0]==0xA3:
            return rcv[2]+rcv[3]/10
        else:
            return 0.0
