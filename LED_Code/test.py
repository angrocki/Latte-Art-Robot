# -*- coding: utf-8 -*-
from serial import Serial, SerialException
import time

arduino = Serial(port = '/dev/cu.usbmodem1101', baudrate=115200, timeout=0)
time.sleep(2)
while True:
    line = arduino.readline().decode().rstrip()
    print(line)
    # decoded = bytes[0:len(bytes)].decode("utf-8")
    # print(decoded)
    if line == '>':
        message = "M1"
        # arduino.write(str.encode(">"+message))
        arduino.write(str.encode(message+"\n"))