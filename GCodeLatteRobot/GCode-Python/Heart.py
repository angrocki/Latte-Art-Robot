"""
G-Code to make heart latte design.
"""
from GCodeCommands import *
"""
Pour Straight no squickly 
"""
def heart_easy(): 
    enable_T()
    enable_X()
    enable_Y()
    go_cup_origin()
    enable_Z()
    set_speed_Z(80)
    move_z(65)
    set_speed_T(10)
    angle = -40
    tilt(angle)
    #Move distance center function
    #Move to above the cup
    enable_solenoid()
    set_speed_T(1)
    tilt(0)
    set_speed_Z(250)
    set_speed(70)
    move_controller(30, None, 40, None)
    #move_z(0)
    #move_x(5)
    #move_xz(-10, 0)
    disable_solenoid()
    disable_T()
    go_home()
    disable_X()
    disable_Y()
    disable_Z()
    
    


    
def heart_hard():
    enable_solenoid()
    
