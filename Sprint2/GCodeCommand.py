"""
Arduino output: ">"
Moves 2 Motor Gantry: 
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
            print(message)
            arduino.write(str.encode(message+"\n"))
            break
def move_x(xpos):
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M3 X{}\n".format(xpos)
            arduino.write(str.encode(message+"\n"))
            break
def set_pos(xpos, ypos):
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M5 X{} Y{}\n".format(xpos, ypos)
            arduino.write(str.encode(message+"\n"))
            break
            
def move_y(y_pos):
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M4 Y{}".format(y_pos)
            print(message)
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
    step_size = 2*math.pi/points
    step = 0
    for _ in range(points):
        round(math.cos(step) + radius, 2)
        x.append(round(math.cos(step) * radius, 2)) 
        y.append(round(math.sin(step) * radius, 2))
        step = step + step_size 
    return x, y
        
while(True):
    try:
        cmd_id = int(input("Please enter a command ID (1): ")) 
        if int(cmd_id) > 2 or int(cmd_id) < 0:
            print ("Values other than 1 and 2 are ignored.")
        # Square
        elif int(cmd_id) == 1: 
            move_x(100)
            move_y(100)
            move_x(50)
            move_y(50)
            break
        # Circle
        elif int(cmd_id) == 2: 
            radius = 30 #mm
            points = 50  
            x, y = make_circle(radius, points)
            move_line(80,80)
            set_pos(0,0)
            for i in range(len(x)):
                move_line(x[i],y[i])
            move_line(x[0],y[0])

            
    except ValueError:
        print ("You must enter integer value 1 or 2")