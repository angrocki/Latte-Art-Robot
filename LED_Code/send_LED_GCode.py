"""
Arduino output: ">"
Blink 4 LEDS: 
"""
# hello

from serial import Serial, SerialException
import time

arduino = Serial(port = '/dev/cu.usbmodem1101', baudrate=115200, timeout=0)
time.sleep(2)
def blink_xyze(xpos, ypos, zpos, epos):
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "G01 X{} Y{} Z{} E{}\n".format(xpos, ypos, zpos, epos)
            arduino.write(str.encode(message+"\n"))
            break
            
def speed(s):
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M3 S{}".format(s)
            arduino.write(str.encode(message+"\n"))
            break
def enable_led(): 
    while True: 
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M1"
            arduino.write(str.encode(message+"\n"))
            break
      
        
def disable_led():
    while True: 
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M2"
            arduino.write(str.encode(message+"\n"))
            break
        
def delay(s):
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M4 S{}".format(s)
            arduino.write(str.encode(message+"\n"))
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