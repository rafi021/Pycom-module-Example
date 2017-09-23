from PZEM_04 import pzem

sen=pzem(uart_id=1,baudrate=9600)
sen.isReady()

while 1:
    v=sen.readVoltage()
    i=sen.readCurrent()
    p=sen.readPower()
    e=sen.readEnergy()
    print("Voltage:{:0.2f} Current:{:0.2f} Power:{:0.2f} Energy:{:0.2f}",v,i,p,e)
    sleep(1)
