'''
Chose Design based on UI input. 
Functions are imported from different files. 
'''
from Heart import heart_easy, heart_hard
from Base import base_simple,  base_complicated
from Rosetta import rosetta_easy, rosetta_hard,test
import random
while(True):
    try:
        cmd_id = int(input("Please enter a command ID for Different Patterns(1: heart, 2: rosetta, 3: random): ")) 
        if int(cmd_id) == 1: 
            print("1")
            #heart_easy()
        if int(cmd_id) == 2:  
            print("2")
            #rosetta_easy()
        if int(cmd_id) == 3:
            print("3")
            #cmd_id = random.randint(1,2)

    except ValueError:
        print ("You must enter integer value 1")
