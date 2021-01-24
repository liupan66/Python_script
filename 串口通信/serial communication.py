import serial
import binascii  
import struct 
import time

# 创建serial实例
serialport = serial.Serial()
serialport.port = 'COM14'
serialport.baudrate = 115200
serialport.parity = 'N'
serialport.bytesize = 8
serialport.stopbits = 1
serialport.timeout = 0.2

while 1:
    serialport.open()
    # 发送数据
    d=bytes.fromhex('0B 0B')
    serialport.write(d)
    #print (d)
    # 接收数据  
    str1 = serialport.read(10)
    data= binascii.b2a_hex(str1)
    print(data)
    time.sleep(0.5)
    serialport.close()