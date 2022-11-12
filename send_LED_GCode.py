"""
Arduino output: ">"
Blink 4 LEDS: 
"""

from serial import Serial, SerialException
import time

arduino = Serial(port = '/dev/cu.usbmodem1101', baudrate=115200, timeout=0)

def blink_xyze(xpos, ypos, zpos, epos):
    while True:
        bytes = arduino.readline()
        decoded = bytes[0:len(bytes)-2].decode("utf-8")
        if decoded == '>':
            destination = "G01 X{} Y{} Z{} E{}\n".format(xpos, ypos, zpos, epos)
            arduino.write(str.encode(destination))
            break
            
def speed(s):
    while True:
        bytes = arduino.readline()
        decoded = bytes[0:len(bytes)-2].decode("utf-8")
        if decoded == '>':
            message = "M3 S{}".format(s)
            arduino.write(str.encode(message))
            break
def enable_led(): 
    bytes = arduino.readline()
    decoded = bytes[0:len(bytes)].decode("utf-8")
    if decoded == '>':
        message = "M1"
        arduino.write(str.encode(message))
      
        
def disable_led():
    while True:
        bytes = arduino.readline()
        decoded = bytes[0:len(bytes)-2].decode("utf-8")
        if decoded == '>':
            message = "M2"
            arduino.write(str.encode(message))
            break
        
def delay(s):
    while True:
        bytes = arduino.readline()
        decoded = bytes[0:len(bytes)].decode("utf-8")
        if decoded == '>':
            message = "M3 S{}".format(s)
            arduino.write(str.encode(message))
            break
while(True):
    try:
        cmd_id = int(input("Please enter a command ID (1): ")) 
        if int(cmd_id)!= 1:
            print ("Values other than 1 are ignored.")
        else:
            enable_led()
            print(1)
            delay(2000)
            print(2)
            disable_led()
            print(3)
            delay(2000)
            print(4)
            blink_xyze(3,4,5,6)
            print(5)
            speed(200)
            print(6)
            blink_xyze(4,4,4,4)
            print(7)
            break
    except ValueError:
        print ("You must enter integer value 1")