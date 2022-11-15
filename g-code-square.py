"""
Arduino output: ">"
Blink 4 LEDS: 
"""
# hello

from serial import Serial, SerialException
import time
import math

arduino = Serial(port = '/dev/cu.usbmodem1101', baudrate=115200, timeout=0)
time.sleep(2)
def move_line(xpos, ypos):
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "G1 X{} Y{}\n".format(xpos,ypos)
            arduino.write(str.encode(message+"\n"))
            break
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
def make_circle(radius, points): 
    # origin is 0
    x = []
    y = []
    i = 0
    step = 0
    for i in range(points):
        x[i] = math.cos(step) + radius 
        y[i] = math.sin(step) + radius 
        step = step + math.pi / points /2 
    return x, y



        
while(True):
    try:
        cmd_id = int(input("Please enter a command ID (1): ")) 
        if int(cmd_id)!= 1 or int(cmd_id)!= 2:
            print ("Values other than 1 are ignored.")
        # Square
        elif int(cmd_id) == 1: 
            move_x(100)
            move_y(100)
            move_x(50)
            move_y(50)
            break
        # Circle
        elif int(cmd_id) == 2: 
            radius = 50 #mm
            points = 10  
            x, y = make_circle(radius, points)
            for i in range(len(x)):
                move_line(x[i],y[i])
            move_line(x[0],y[0])
            #IF serial doesnt work copy past
            """
            for i in range(len(x)):
                message = "G1 X{} Y{}\n".format(x[i],y[i])
                print(message)
            message = "G1 X{} Y{}\n".format(x[0],y[0])
            print(message)
            """
            
    except ValueError:
        print ("You must enter integer value 1")