"""
G-Code to make latte base.
"""
from GCodeCommands import *
import matplotlib.pyplot as plt
"""
Base_Simple
No Tilt, no changing Height, only circles until a certain time/circles/height
"""
def base_simple(): 
    go_home()
    disable_Z()
    go_cup_origin()
    diameter = 30 ##mm
    radius = diameter/2
    points = 50
    x, y = make_circle(radius, points)
    circles = 3
    move_XY(x[0],y[0])
    set_speed(75)
    enable_solenoid()
    for i in range(circles):
        for i in range(len(x)):
            move_XY(x[i],y[i])
    disable_solenoid()
    set_speed(10)
    move_XY(0,0)
"""
Base_tilt
No Tilt, no changing Height, only circles until a certain time/circles/height
"""
def base_tilt(): 
    #go_home()
    #go_cup_origin()
    diameter = 30 ##mm
    radius = diameter/2
    points = 2000
    x, y = make_circle(radius, points)
    circles = 3
    move_XY(x[0],y[0])
    set_speed(75)
    #enable_solenoid()
    for i in range(circles):
        for i in range(len(x)):
            move_XY(x[i],y[i])
        move_XY(x[0],y[0])
    #disable_solenoid()
    set_speed(10)
    move_XY(0,0)

def base_complicated():
    print("Complicated Base")
def check_circle():
    radius = 15
    points =  1000
    x, y = make_circle(radius, points)
    plt.plot(x,y)
    plt.show()


