"""
List of G-Code Commands. Communicates with Adrino G-Code
"""
from serial import Serial
import time
import math
import numpy as np
#/dev/cu.usbmodem1101 AN
#COM16 Jacob
arduino = Serial(port = 'COM16', baudrate=115200, timeout=0)
time.sleep(2)
def go_home():
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "G27"
            print(message)
            arduino.write(str.encode(message+"\n"))
            break
def go_cup_origin():
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "G28"
            print(message)
            arduino.write(str.encode(message+"\n"))
            break
def move_XYZT(xpos, ypos, zpos, tilt):
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "G1 X{} Y{} Z{} T{}\n".format(xpos,ypos,zpos,tilt)
            print(message)
            arduino.write(str.encode(message+"\n"))
            break
def move_controller(xpos=None,ypos=None,zpos=None,angle=None):
    while True:
        message = "G1 "
        line = arduino.readline().decode().rstrip()

        if line == '>':
            if type(xpos) == int:
                message += f"X{xpos} "
            if type(ypos) == int:
                message += f"Y{ypos} "
            if type(zpos) == int:
                message += f"Z{zpos} "
            if type(angle) == int:
                message += f"T{angle}"

            message += "\n"
            print(message)
            arduino.write(str.encode(message+"\n"))
            break

def move_XYT(xpos, ypos, tilt):
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "G1 X{} Y{} T{}\n".format(xpos,ypos,tilt)
            print(message)
            arduino.write(str.encode(message+"\n"))
            break
def move_XY(xpos, ypos):
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "G1 X{} Y{}\n".format(xpos,ypos)
            print(message)
            arduino.write(str.encode(message+"\n"))
            break
def tilt(angle):
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "G1 T{}\n".format(angle)
            print(message)
            arduino.write(str.encode(message+"\n"))
            break 
def move_x(xpos):
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "G1 X{}\n".format(xpos)
            print(message)
            arduino.write(str.encode(message+"\n"))
            break
def set_pos(xpos, ypos):
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "G92 X{} Y{}\n".format(xpos, ypos)
            print(message)
            arduino.write(str.encode(message+"\n"))
            break
def set_speed(speed):
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M220 S{}\n".format(speed)
            print(message)
            arduino.write(str.encode(message+"\n"))
            break
def set_speed_T(speed):
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M222 S{}\n".format(speed)
            print(message)
            arduino.write(str.encode(message+"\n"))
            break
def set_speed_Z(speed):
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M221 S{}\n".format(speed)
            print(message)
            arduino.write(str.encode(message+"\n"))
            break
def move_y(y_pos):
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M1 Y{}".format(y_pos)
            print(message)
            arduino.write(str.encode(message+"\n"))
            break
def move_z(z_pos):
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "G1 Z{}".format(z_pos)
            print(message)
            arduino.write(str.encode(message+"\n"))
            break
def enable_solenoid():
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M380"
            print(message)
            arduino.write(str.encode(message+"\n"))
            break
def disable_solenoid():
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M381"
            print(message)
            arduino.write(str.encode(message+"\n"))
            break
def disable_Z():
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M11"
            print(message)
            arduino.write(str.encode(message+"\n"))
            break
def enable_Z():
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M10"
            print(message)
            arduino.write(str.encode(message+"\n"))
            break
def enable_T():
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M12"
            print(message)
            arduino.write(str.encode(message+"\n"))
            break
def disable_T():
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M13"
            print(message)
            arduino.write(str.encode(message+"\n"))
            break

def enable_X():
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M14"
            print(message)
            arduino.write(str.encode(message+"\n"))
            break
def disable_X():
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M15"
            print(message)
            arduino.write(str.encode(message+"\n"))
            break

def enable_Y():
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M16"
            print(message)
            arduino.write(str.encode(message+"\n"))
            break
def disable_Y():
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M17"
            print(message)
            arduino.write(str.encode(message+"\n"))
            break
def delay(ms):
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M6 S{}".format(ms)
            print(message)
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

def make_sine(amplitude, frequency, distance, points):
    x = []
    y = []

    x = np.linspace(0,distance,points)
    for i in range(0,len(x)):
        y.append(amplitude*math.sin(frequency*x[i]))
    return x, y
