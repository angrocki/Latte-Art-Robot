'''
Chose a latte design based on keyboard input. 
Functions are imported from different files. 
'''
from Heart import heart
from Base import base
from Rosetta import rosetta,test
from GCodeCommands import *

while(True):
    try:
        cmd_id = int(input("Please enter a command ID for Different Patterns(1: base, 2: heart, 3: rosetta, 4: test, 6-7:solenoid on/off): ")) 
        print(cmd_id)
        if int(cmd_id) < 0 or int(cmd_id) > 7:
            print ("Values other than 1-6 are ignored.")
        # Base1
        elif int(cmd_id) == 1: 
            base()
        elif int(cmd_id) == 2: 
            heart()
        # Rosetta
        elif int(cmd_id) == 3: 
            rosetta()
        elif int(cmd_id) == 4:
            test()
        elif int(cmd_id) == 5:
            enable_solenoid()
        elif int(cmd_id) == 6:
            disable_solenoid()
    except ValueError:
        print ("You must enter integer value within the range of 1-6")
