"""
G-Code to make Rosetta latte design.
"""

from GCodeCommands import *
from Base import base_simple


def rosetta_easy(): 
    print("Rosetta Easy")
    angle = 40
    x_count = 0

    base_simple()   #make base
    move_controller(None,None,None,None,angle)  #tilt cup
    move_controller(None,None,31)               #move z up
    enable_solenoid()                           #open valve
    while angle > 5:
        angle-=1
        move_controller(None,-y,None,None,angle)
    while angle > 0:
        move_controller(None,None,31)
        move_controller(x)
        xcount += x
        angle -= 1
    if angle == 0:
        disable_solenoid()
        move_controller(None, None, 31)
        enable_solenoid()
        move_controller(95.25)

def test():
    x,y = make_sine(10,5,90,200)
    print(x,y)
    for i in range(len(x)):
        # move_XY(x[i],y[i])
        move_controller(x[i], y[i])


def rosetta_hard():
    print("Rosetta Hard")

test()