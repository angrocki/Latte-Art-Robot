"""
G-Code to make heart latte design.
"""
from GCodeCommands import *
"""
Pour Straight no squickly 
"""
def heart_easy(): 
    enable_T()
    set_speed_T(10)
    angle = 40
    tilt(angle)
    #Move distance center function
    #Move to above the cup
    enable_Z()
    move_z(31)
    enable_solenoid()
    while angle > 0:
        tilt(angle)
        angle = angle -1
        delay(100)
    disable_solenoid()
    move_z(0)
    move_x(5)
    #move_xz(-10, 0)
    set_speed(75)
    enable_solenoid()
    move_x(-10)
    disable_solenoid()
    disable_T()
    disable_X()
    disable_Y()
    disable_Z()
    
    


    
def heart_hard():
    print("Heart Hard")