"""
Arduino output: ">"
Blink 4 LEDS: 
"""
# hello

from serial import Serial, SerialException
import time

arduino = Serial(port = '/dev/cu.usbmodem1101', baudrate=115200, timeout=0)
time.sleep(2)
def move_x(xpos):
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M3 X{}\n".format(xpos)
            arduino.write(str.encode(message+"\n"))
            break
            
def move_y(y_pos):
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M4 Y{}".format(y_pos)
            arduino.write(str.encode(message+"\n"))
            break
def rotate_x(): 
    while True: 
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M1"
            arduino.write(str.encode(message+"\n"))
            break
      
        
def rotate_y():
    while True: 
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M2"
            arduino.write(str.encode(message+"\n"))
            break
        
while(True):
    try:
        cmd_id = int(input("Please enter a command ID (1): ")) 
        if int(cmd_id)!= 1:
            print ("Values other than 1 are ignored.")
        else: 
            move_x(100)
            move_y(100)
            move_x(50)
            move_y(50)
            break
    except ValueError:
        print ("You must enter integer value 1")