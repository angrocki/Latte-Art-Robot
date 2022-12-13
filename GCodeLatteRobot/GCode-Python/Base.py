"""
G-Code to make latte base.
"""
from GCodeCommands import *

def base(): 
    '''
    A function with the list of G-Code commands to make a latte base.
    '''
    enable_X()
    enable_Y()
    enable_Z()
    go_home()
    disable_Z()
    go_cup_origin()
    diameter = 30 ##mm
    radius = diameter/2
    points = 50
    x, y = make_circle(radius, points)
    circles = 2
    move_controller(x[0],y[0])
    set_speed(70)
    enable_solenoid()
    for i in range(circles):
        for i in range(len(x)):
            move_controller(x[i,y[i]])
    disable_solenoid()
    set_speed(10)
    move_controller(0,0)

