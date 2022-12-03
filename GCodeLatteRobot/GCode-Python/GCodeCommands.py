"""
List of G-Code Commands. Communicates with Adrino G-Code
"""
from serial import Serial
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