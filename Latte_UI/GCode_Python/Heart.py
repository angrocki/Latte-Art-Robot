"""
G-Code to make heart latte design.
"""
from GCode_Python.GCodeCommands import *

def heart(): 
    """
    A function with the list of G-Code commands to make a latte heart
    and returns a string "done" when commands are completed. 
    """
    enable_T()
    enable_X()
    enable_Y()
    go_cup_origin()
    enable_Z()
    set_speed_Z(80)
    move_controller(None,None,60,None)
    set_speed_T(10)
    angle = -40
    move_controller(None,None,None,angle)
    enable_solenoid()
    set_speed_T(10)
    for i in range(40):
        angle = angle +1 
        move_controller(None,None,None,angle)
        time.sleep(.2)
    print("test")
    set_speed_Z(120)
    set_speed(70)
    move_controller(30, None, 40, None)
    disable_solenoid()
    disable_T()
    time.sleep(1.5)
    go_home()
    disable_X()
    disable_Y()
    disable_Z()
    return True
    
