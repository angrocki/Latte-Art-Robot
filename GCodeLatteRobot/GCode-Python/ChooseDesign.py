'''
Chose Design based on keyboard input. 
Functions are imported from different files. 
'''
from Heart import heart_easy, heart_hard
from Base import base_simple,  base_complicated
from Rosetta import rosetta_easy, rosetta_hard 

while(True):
    try:
        cmd_id = int(input("Please enter a command ID for Different Patterns(1-2: base, 3-4: heart, 5-6 rosetta): ")) 
        if int(cmd_id) < 0 or int(cmd_id) > 6:
            print ("Values other than 1 and 2 are ignored.")
        # Base1
        elif int(cmd_id) == 1: 
            base_simple()
        elif int(cmd_id) == 2:  
            base_complicated()
        # Heart
        elif int(cmd_id) == 3: 
            heart_easy()
        elif int(cmd_id) == 4:  
            heart_hard()
        # Rosetta
        elif int(cmd_id) == 5: 
            rosetta_easy()
        elif int(cmd_id) == 6:  
            rosetta_hard()
    except ValueError:
        print ("You must enter integer value 1")
