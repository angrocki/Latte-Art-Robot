"""
G-Code to make Rosetta latte design.
"""

from GCode_Python.GCodeCommands import *

def rosetta(): 
    """
    A function with the list of G-Code commands to make a latte rosetta,
    and returns a string "Done" when the commands are completed.
    """
    x_count = 0
    enable_T()
    enable_X()
    enable_Y()
    go_cup_origin()
    enable_Z()
    
    set_speed_Z(80)
    move_controller(None,None,65,None)
    set_speed_T(10)
    set_speed(80)
    angle = -40
    angle_step = round(40/50,1)
    move_controller(None,None,None,angle)
    enable_solenoid()                           #open valve
    while angle <= -15:
        x,y = make_sine(10,5,30,50)
        for i in range(len(x)):
            if angle > -15:
                break
            move_controller(None,y[i],None,None)
            angle = round(angle + angle_step,1)
            move_controller(None, None, None, angle)
    while angle < 0:
        x,y = make_sine(15,1,50,50)
        for i in range(len(x)):
            if angle == 0:
                break
            move_controller(x[i]*-1, y[i])
            angle = round(angle + angle_step,1)
            move_controller(None, None, None, angle)    
    if angle == 0:
        disable_solenoid()
        move_controller(None, None, 31, None)
        enable_solenoid()
        move_controller(30)
    disable_T()
    go_home()
    disable_solenoid()
    disable_X()
    disable_Y()
    disable_Z()
    
    
    return True

def test():
    """
    A function with the list of G-Code commands that test the sin function.
    """
    go_home()
    enable_X()
    enable_Y()
    disable_Z()
    disable_T()

    go_cup_origin()
    x,y = make_sine(10,5,90,200)
    for i in range(len(x)):
        move_controller(x[i], y[i])
        print(x[i],y[i])