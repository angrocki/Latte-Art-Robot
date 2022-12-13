"""
List of G-Code Commands. Communicates with Adrino G-Code
"""
from serial import Serial
import time
import math
import numpy as np
#/dev/cu.usbmodem1101 An
#COM16 Jacob
#/dev/ttyACM0 Allyson
arduino = Serial(port = '/dev/cu.usbmodem1101', baudrate=115200, timeout=0)
time.sleep(2)

def go_home():
    '''
    A function that gives the robot the G-Code command to "zero" itself by
    moving all the motors to hit the limit switches.
    '''
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "G27"
            print(message)
            arduino.write(str.encode(message+"\n"))
            break

def go_cup_origin():
    '''
    A function that gives the robot the G-Code command to move to the center
    of the coffee cup.
    '''
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "G28"
            print(message)
            arduino.write(str.encode(message+"\n"))
            break

def move_controller(xpos=None,ypos=None,zpos=None,angle=None):
    '''
    A function that gives the robot a G-Code command to move to a given position
    on the global axis. Each parameter is default set to None.

    Args:
    xpos: An integer representing the x-coordinate the robot should move to.
    ypos: An integer representing the y-coordinate the robot should move to.
    zpos: An integer representing the z-coordinate the robot should move to.
    tilt: An integer representing the tilt angle the robot should move to.
    '''
    while True:
        message = "G1 "
        line = arduino.readline().decode().rstrip()

        if line == '>':
            if type(xpos) == float:
                message += f"X{xpos} "
            if type(ypos) == float:
                message += f"Y{ypos} "
            if type(zpos) == float:
                message += f"Z{zpos} "
            if type(angle) == float:
                message += f"T{angle}"

            message += "\n"
            print(message)
            arduino.write(str.encode(message+"\n"))
            break

def set_speed(speed):
    '''
    A function that gives the robot a G-Code command to change the speed of the
    x and y axis motors.

    Args:
        speed: An integer representing the desired speed of the motors in RPM.
    '''
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M220 S{}\n".format(speed)
            print(message)
            arduino.write(str.encode(message+"\n"))
            break
def set_speed_T(speed):
    '''
    A function that gives the robot a G-Code command to change the speed of the
    tilt motor.

    Args:
        speed: An integer representing the desired speed of the motors in RPM.
    '''
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M222 S{}\n".format(speed)
            print(message)
            arduino.write(str.encode(message+"\n"))
            break

def set_speed_Z(speed):
    '''
    A function that gives the robot a G-Code command to change the speed of the
    z-axis motor.

    Args:
        speed: An integer representing the desired speed of the motors in RPM.
    '''
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M221 S{}\n".format(speed)
            print(message)
            arduino.write(str.encode(message+"\n"))
            break

def enable_solenoid():
    '''
    A function that gives the robot a G-Code command to enable the solenoid valve
    (in other words, to open the valve).
    '''
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M380"
            print(message)
            arduino.write(str.encode(message+"\n"))
            break
def disable_solenoid():
    '''
    A function that gives the robot a G-Code command to disable the solenoid valve
    (in other words, to close the valve).
    '''
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M381"
            print(message)
            arduino.write(str.encode(message+"\n"))
            break

def disable_Z():
    '''
    A function that gives the robot a G-Code command to disable the z-axis motor.
    '''
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M11"
            print(message)
            arduino.write(str.encode(message+"\n"))
            break

def enable_Z():
    '''
    A function that gives the robot a G-Code command to enable the z-axis motor.
    '''
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M10"
            print(message)
            arduino.write(str.encode(message+"\n"))
            break

def enable_T():
    '''
    A function that gives the robot a G-Code command to enable the tilt motor.
    '''
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M12"
            print(message)
            arduino.write(str.encode(message+"\n"))
            break

def disable_T():
    '''
    A function that gives the robot a G-Code command to disable the tilt motor.
    '''
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M13"
            print(message)
            arduino.write(str.encode(message+"\n"))
            break

def enable_X():
    '''
    A function that gives the robot a G-Code command to enable the x-axis motor.
    '''
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M14"
            print(message)
            arduino.write(str.encode(message+"\n"))
            break

def disable_X():
    '''
    A function that gives the robot a G-Code command to disable the x-axis motor.
    '''
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M15"
            print(message)
            arduino.write(str.encode(message+"\n"))
            break

def enable_Y():
    '''
    A function that gives the robot a G-Code command to enable the y-axis motor.
    '''
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M16"
            print(message)
            arduino.write(str.encode(message+"\n"))
            break

def disable_Y():
    '''
    A function that gives the robot a G-Code command to disable the y-axis motor.
    '''
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M17"
            print(message)
            arduino.write(str.encode(message+"\n"))
            break

def delay(ms):
    '''
    A function that gives the robot a G-Code command to pause its movements by a
    given amount.

    Args:
        ms: An integer representing the desired delay time in milliseconds.
    '''
    while True:
        line = arduino.readline().decode().rstrip()
        if line == '>':
            message = "M6 S{}".format(ms)
            print(message)
            arduino.write(str.encode(message+"\n"))
            break

def make_circle(radius, points): 
    '''
    A function that calculates and returns the x and y coordinates necessary in
    order to create a circle of a given radius, and of a certain amount of points.
    The x and y coordinates are calculated using the Pythagorean Identity:
    cos^2 + sin^2 = 1.

    Args:
        radius: An integer representing the desired radius of the circle in mm.
        points: An integer representing the desired amount of coordinates.

    Returns:
        x: 
            An array containing rounded integers representing the global x
            coordinates for creating a circle.
        y: 
            An array containing rounded integers representing the global y
            coordinates for creating a circle.
    '''
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
    '''
    A function that calculates and returns the x and y coordinates necessary in
    order to create a sin wave of a given amplitude, frequency, x-distance, and
    amount of points. The x & y coordinates are calculated using the sin function:
    y = A*sin(B*x) where A is the amplitude and B is the frequency.

    Args:
        amplitude: An integer representing the desired amplitude of the wave in mm.
        frequency: An integer representing the desired frequency of the wave in mm.
        distance: An integer representing the desired distance travelled in the x
                  direction in mm.
        points: An integer representing the desired amount of coordinates.

    Returns:
        x: 
            An array containing rounded integers representing the global x
            coordinates for creating a sin wave.
        y: 
            An array containing rounded integers representing the global y
            coordinates for creating a sin wave.
    '''
    x = []
    y = []
    x = np.linspace(0,distance,points)
    x = x.tolist()
    for i in range(0,len(x)):
        y.append(round(amplitude*math.sin(frequency*x[i]),1))
        x[i]=round(x[i],1)
    return x, y


