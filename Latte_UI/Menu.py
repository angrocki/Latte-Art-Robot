import pygame as pg
from Background import *
from DesignButton import *
from NavigationButton import *
import sys
# import random

sys.path.append('/home/allysonhur/Latte-Art-Robot/GCodeLatteRobot/GCode-Python')
# from Heart import heart
# from Rosetta import rosetta
# from Base import base

#----------------------------------------------------------------------------------
## SCREEN
#----------------------------------------------------------------------------------
screen = pg.display.set_mode((1280,720))

#----------------------------------------------------------------------------------
## NAVIGATION BUTTON OBJECTS
#----------------------------------------------------------------------------------
start_button = NavigationButton('Start')
start_button.setup()

home_button = NavigationButton('Home')
home_button.setup()

next_button = NavigationButton('Next')
next_button.setup()

begin_drawing_button = NavigationButton('Begin Drawing')
begin_drawing_button.setup()

back_to_home = NavigationButton('Back')
back_to_home.setup()

back_to_choose = NavigationButton('Back')
back_to_choose.setup()

#----------------------------------------------------------------------------------
## DESIGN BUTTON OBJECTS
#----------------------------------------------------------------------------------
heart_design = DesignButton('Heart')
heart_design.setup()
rosetta_design = DesignButton('Rosetta')
rosetta_design.setup()
random_design = DesignButton('Random')
random_design.setup()

heart_border = DesignButton('Heart Border')
heart_border.setup()
rosetta_border = DesignButton('Rosetta Border')
rosetta_border.setup()
random_border = DesignButton('Random Border')
random_border.setup()

milk_check = DesignButton('Milk Check')
milk_check.setup()
coffee_check = DesignButton('Coffee Check')
coffee_check.setup()
cup_check = DesignButton('Cup Check')
cup_check.setup()

#----------------------------------------------------------------------------------
## BACKGROUND OBJECTS 
#----------------------------------------------------------------------------------
home_screen = Background('Home')
choose_screen = Background('Choose')
checklist_screen = Background('Checklist')
waiting_screen = Background('Waiting')
done_screen = Background('Done')

#----------------------------------------------------------------------------------
## TEST INTEGRATION BETWEEN UI AND GCODE FUNCTION
#----------------------------------------------------------------------------------
def rosetta_test():
        print('hello')
        print('world')
        return True 

#----------------------------------------------------------------------------------
## MENU CLASS
#---------------------------------------------------------------------------------- 
class Menu():
    """
    Menu that can switch between pages if button objects are clicked.

    Attributes:
        state: A string representing one of the pages available in the menu.
        id: An integer representing the latte design the user has chosen.

    """
    def __init__(self):
        self.state = 'home'
        self.id = 0

#----------------------------------------------------------------------------------
## STATE MANAGER
#---------------------------------------------------------------------------------- 
    def state_manager(self):
        '''
        Runs the respective funtion depending on the state.

        '''
        if self.state == 'home':
            self.home()
        elif self.state == 'choose':
            self.choose()
        elif self.state == 'choose_heart':
            self.choose_heart()
        elif self.state == 'choose_rosetta':
            self.choose_rosetta()
        elif self.state == 'choose_random':
            self.choose_random()
        elif self.state == 'checklist':
            self.checklist()
        elif self.state == 'checklist_milk':
            self.checklist_milk()
        elif self.state == 'checklist_milk_coffee':
            self.checklist_milk_coffee()
        elif self.state == 'checklist_milk_coffee_cup':
            self.checklist_milk_coffee_cup()
        elif self.state == 'checklist_coffee':
            self.checklist_coffee()
        elif self.state == 'checklist_coffee_cup':
            self.checklist_coffee_cup()
        elif self.state == 'checklist_cup':
            self.checklist_cup()
        elif self.state == 'waiting':
            self.waiting()
        elif self.state == 'done':
            self.done()

#----------------------------------------------------------------------------------
## HOME SCREEN
#---------------------------------------------------------------------------------- 
    def home(self):
        '''
        Displays the home page if the state == 'home'.
        '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if start_button.click():
                self.state = 'choose'
        pg.display.update()
        home_screen.display(screen)
        start_button.display(screen)

#----------------------------------------------------------------------------------
## CHOOSE SCREENS
#---------------------------------------------------------------------------------- 
    def choose(self):
        '''
        Displays the choose page if the state == 'choose'.
        '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if heart_design.click():
                self.state = 'choose_heart'
            if rosetta_design.click():
                self.state = 'choose_rosetta'
            if random_design.click():
                self.state = 'choose_random'
            if back_to_home.click():
                self.state = 'home'
        pg.display.update()
        choose_screen.display(screen)
        heart_design.display(screen)
        rosetta_design.display(screen)
        random_design.display(screen)
        back_to_home.display(screen)

    def choose_heart(self):
        '''
        Displays the choose page with the heart latte design selected if state == 'choose_heart'.
        '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if heart_design.click():
                self.state = 'choose_heart'
            if rosetta_design.click():
                self.state = 'choose_rosetta'
            if random_design.click():
                self.state = 'choose_random'
            if next_button.click():
                self.state = 'checklist'
                self.id = 1
            if back_to_home.click():
                self.state = 'home'
        pg.display.update()
        choose_screen.display(screen)
        heart_design.display(screen)
        heart_border.display(screen)
        rosetta_design.display(screen)
        random_design.display(screen)
        next_button.display(screen)
        back_to_home.display(screen)
        
            
    def choose_rosetta(self):
        '''
        Displays the choose page with the rosetta latte design selected if state == 'choose_rosetta'.
        '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if heart_design.click():
                self.state = 'choose_heart'
            if rosetta_design.click():
                self.state = 'choose_rosetta'
            if random_design.click():
                self.state = 'choose_random'
            if next_button.click():
                self.state = 'checklist'
                self.id = 2
            if back_to_home.click():
                self.state = 'home'
        pg.display.update()
        choose_screen.display(screen)
        heart_design.display(screen)
        rosetta_design.display(screen)
        rosetta_border.display(screen)
        random_design.display(screen)
        next_button.display(screen)
        back_to_home.display(screen)

    def choose_random(self):
        '''
        Displays the choose page with the random latte design selected if state == 'choose_random'.
        '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if heart_design.click():
                self.state = 'choose_heart'
            if rosetta_design.click():
                self.state = 'choose_rosetta'
            if random_design.click():
                self.state = 'choose_random'
            if next_button.click():
                self.state = 'checklist'
                self.id = 3
            if back_to_home.click():
                self.state = 'home'
        pg.display.update()
        choose_screen.display(screen)
        heart_design.display(screen)
        rosetta_design.display(screen)
        random_design.display(screen)
        random_border.display(screen)
        next_button.display(screen)
        back_to_home.display(screen)

#----------------------------------------------------------------------------------
## CHECKLIST SCREENS
#----------------------------------------------------------------------------------    
    def checklist(self):
        '''
        Displays the checklist page if state == 'checklist'
        '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if milk_check.click():
                self.state = 'checklist_milk'
            if coffee_check.click():
                self.state = 'checklist_coffee'
            if cup_check.click():
                self.state = 'checklist_cup'
            if back_to_choose.click():
                self.state = 'choose'
            
        pg.display.update()
        checklist_screen.display(screen)
        back_to_choose.display(screen)
    
    def checklist_milk(self):
        '''
        Displays the checklist page with milk checked off if state == 'checklist_milk'
        '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if milk_check.click():
                self.state = 'checklist'
            if coffee_check.click():
                self.state = 'checklist_milk_coffee'
            if cup_check.click():
                self.state = 'checklist_milk_cup'  
            if back_to_choose.click():
                self.state = 'choose'
        pg.display.update()
        checklist_screen.display(screen)
        milk_check.display(screen)
        back_to_choose.display(screen)

    def checklist_coffee(self):
        '''
        Displays the checklist page with coffee checked off if state == 'checklist_coffee'
        '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if milk_check.click():
                self.state = 'checklist_milk_coffee'
            if coffee_check.click():
                self.state = 'checklist'
            if cup_check.click():
                self.state = 'checklist_coffee_cup'  
            if back_to_choose.click():
                self.state = 'choose'
        pg.display.update()
        checklist_screen.display(screen)
        coffee_check.display(screen)
        back_to_choose.display(screen)
    
    def checklist_cup(self):
        '''
        Displays the checklsit page with cup checked off if state == 'checklist_cup'
        '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if milk_check.click():
                self.state = 'checklist_milk_cup'
            if coffee_check.click():
                self.state = 'checklist_coffee_cup'
            if cup_check.click():
                self.state = 'checklist'
            if back_to_choose.click():
                self.state = 'choose'
        pg.display.update()
        checklist_screen.display(screen)
        cup_check.display(screen)
        back_to_choose.display(screen)
        
    def checklist_milk_coffee(self):
        '''
        Displays the checklist page with milk and coffee checked off if state == 'checklist_milk_coffee'
        '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if milk_check.click():
                self.state = 'checklist_coffee'
            if coffee_check.click():
                self.state = 'checklist_milk'
            if cup_check.click():
                self.state = 'checklist_milk_coffee_cup'
            if back_to_choose.click():
                self.state = 'choose'
        pg.display.update()
        checklist_screen.display(screen)
        milk_check.display(screen)
        coffee_check.display(screen)
        back_to_choose.display(screen)

    def checklist_milk_coffee_cup(self):
        '''
        Displays the checklist page with milk and coffee and cup checked off if state == 'checklist_milk_coffee_cup'
        '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if milk_check.click():
                self.state = 'checklist_coffee_cup'
            if coffee_check.click():
                self.state = 'checklist_milk_cup'
            if cup_check.click():
                self.state = 'checklist_milk_coffee'
            if back_to_choose.click():
                self.state = 'choose'
            if begin_drawing_button.click():
                self.state = 'waiting'
        pg.display.update()
        checklist_screen.display(screen)
        begin_drawing_button.display(screen)
        milk_check.display(screen)
        coffee_check.display(screen)
        cup_check.display(screen)
        back_to_choose.display(screen)
    
    def checklist_coffee_cup(self):
        '''
        Displays the checklist page with coffee and cup checked off if state == 'checklist_coffee_cup'
        '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if milk_check.click():
                self.state = 'checklist_milk_coffee_cup'
            if coffee_check.click():
                self.state = 'checklist_cup'
            if cup_check.click():
                self.state = 'checklist_coffee'
            if back_to_choose.click():
                self.state = 'choose'
        pg.display.update()
        checklist_screen.display(screen)
        coffee_check.display(screen)
        cup_check.display(screen)
        back_to_choose.display(screen)

#----------------------------------------------------------------------------------
## WAITING SCREEN
#---------------------------------------------------------------------------------- 
    def waiting(self):
        '''
        Displays the waiting page if state == 'waiting'
        '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if self.id == 1:
                print('Drawing heart')
                # base()
                # if heart():
                #     self.state = 'done'
                if rosetta_test():
                    self.state = 'done'
                self.id = 0
            if self.id == 2:
                print('Drawing rosetta')
                # base()
                # if rosetta():
                #     self.state = 'done'
                if rosetta_test():
                    self.state = 'done'
                self.id = 0
            if self.id == 3:
                print('Drawing random')
                self.id = random.randint(1,2)
                self.id = 0
        pg.display.update()
        waiting_screen.display(screen)

#----------------------------------------------------------------------------------
## DONE SCREEN
#---------------------------------------------------------------------------------- 
    def done(self):
        '''
        Displays the done page if state == 'done'
        '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if home_button.click():
                self.state = 'home'
        pg.display.update()
        done_screen.display(screen)
        home_button.display(screen)


