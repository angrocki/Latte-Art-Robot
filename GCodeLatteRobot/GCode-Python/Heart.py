"""
G-Code to make heart latte design.
"""
from GCodeCommands import *
"""
Pour Straight no squickly 
"""
def heart_easy(): 
    angle = 40
    move_tilt(angle)
    #Move distance center function
    #Move to above the cup
    move_z(31)
    enable_solenoid
    while angle > 0:
        tilt(angle)
        angle = angle -1
    disable_solenoid()
    move_z(0)
    move_x(5)
    #move_xz(-10, 0)
    set_speed(75)
    enable_solenoid()
    move_x(-10)
    
    


    
def heart_hard():
    print("Heart Hard")