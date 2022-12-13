import pygame as pg
from Background import *
from Button import *
import sys
import random
sys.path.append('/home/allysonhur/Latte-Art-Robot/GCodeLatteRobot/GCode-Python')
from Heart import heart
from Rosetta import rosetta
from Base import base


screen = pg.display.set_mode((1280,720))
# naviation images 
start_button = NavigationButton("Start")
start_button.setup()

home_button = NavigationButton("Home")
home_button.setup()

next_button = NavigationButton("Next")
next_button.setup()

begin_drawing_button = NavigationButton("Begin Drawing")
begin_drawing_button.setup()

back_to_home = NavigationButton("Back")
back_to_home.setup()

back_to_choose = NavigationButton("Back")
back_to_choose.setup()


# startbut.display(screen)

# design images
heart_design = DesignButton("Heart")
heart_design.setup()
rosetta_design = DesignButton("Rosetta")
rosetta_design.setup()
random_design = DesignButton("Random")
random_design.setup()

heart_border = DesignButton("Heart Border")
heart_border.setup()
rosetta_border = DesignButton("Rosetta Border")
rosetta_border.setup()
random_border = DesignButton("Random Border")
random_border.setup()

milk_check = DesignButton("Milk Check")
milk_check.setup()
coffee_check = DesignButton("Coffee Check")
coffee_check.setup()
cup_check = DesignButton("Cup Check")
cup_check.setup()


# background images
home_screen = Background("Home")
choose_screen = Background("Choose")
checklist_screen = Background("Checklist")
waiting_screen = Background("Waiting")
done_screen = Background("Done")

def rosetta_test():
        print('hello')
        print('world')
        return True 

class Menu():
    def __init__(self):
        self.state = 'home'
        self.id = 0

    def state_manager(self):
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
    
    def home(self):
        '''
        Home Page
        '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if start_button.rect.collidepoint(pg.mouse.get_pos()):
                    self.state = 'choose' 
        pg.display.update()
        home_screen.draw(screen)
        start_button.display(screen)

    def choose(self):
        '''
        Choose page
        '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if heart_design.draw():
                self.state = 'choose_heart'
            if rosetta_design.draw():
                self.state = 'choose_rosetta'
            if random_design.draw():
                self.state = 'choose_random'
            if back_to_home.draw():
                self.state = 'home'
        pg.display.update()
        choose_screen.draw(screen)
        heart_design.display(screen)
        rosetta_design.display(screen)
        random_design.display(screen)
        back_to_home.display(screen)

    def choose_heart(self):
        '''
        Choose page with heart selected
        '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if heart_design.draw():
                self.state = 'choose_heart'
            if rosetta_design.draw():
                self.state = 'choose_rosetta'
            if random_design.draw():
                self.state = 'choose_random'
            if next_button.draw():
                self.state = 'checklist'
                self.id = 1
            if back_to_home.draw():
                self.state = 'home'
        pg.display.update()
        choose_screen.draw(screen)
        heart_design.display(screen)
        heart_border.display(screen)
        rosetta_design.display(screen)
        random_design.display(screen)
        next_button.display(screen)
        back_to_home.display(screen)
        
            
    def choose_rosetta(self):
        '''
        Choose page with rosetta selected
        '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if heart_design.draw():
                self.state = 'choose_heart'
            if rosetta_design.draw():
                self.state = 'choose_rosetta'
            if random_design.draw():
                self.state = 'choose_random'
            if next_button.draw():
                self.state = 'checklist'
                self.id = 2
            if back_to_home.draw():
                self.state = 'home'
        pg.display.update()
        choose_screen.draw(screen)
        heart_design.display(screen)
        rosetta_design.display(screen)
        rosetta_border.display(screen)
        random_design.display(screen)
        next_button.display(screen)
        back_to_home.display(screen)

    def choose_random(self):
        '''
        Choose page with random selected
        '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if heart_design.draw():
                self.state = 'choose_heart'
            if rosetta_design.draw():
                self.state = 'choose_rosetta'
            if random_design.draw():
                self.state = 'choose_random'
            if next_button.draw():
                self.state = 'checklist'
                self.id = 3
            if back_to_home.draw():
                self.state = 'home'
        pg.display.update()
        choose_screen.draw(screen)
        heart_design.display(screen)
        rosetta_design.display(screen)
        random_design.display(screen)
        random_border.display(screen)
        next_button.display(screen)
        back_to_home.display(screen)
        
    def checklist(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if milk_check.draw():
                self.state = 'checklist_milk'
            if coffee_check.draw():
                self.state = 'checklist_coffee'
            if cup_check.draw():
                self.state = 'checklist_cup'
            if back_to_choose.draw():
                self.state = 'choose'
            
        pg.display.update()
        checklist_screen.draw(screen)
        back_to_choose.display(screen)
    
    def checklist_milk(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if milk_check.draw():
                self.state = 'checklist'
            if coffee_check.draw():
                self.state = 'checklist_milk_coffee'
            if cup_check.draw():
                self.state = 'checklist_milk_cup'  
            if back_to_choose.draw():
                self.state = 'choose'
        pg.display.update()
        checklist_screen.draw(screen)
        milk_check.display(screen)
        back_to_choose.display(screen)

    def checklist_coffee(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if milk_check.draw():
                self.state = 'checklist_milk_coffee'
            if coffee_check.draw():
                self.state = 'checklist'
            if cup_check.draw():
                self.state = 'checklist_coffee_cup'  
            if back_to_choose.draw():
                self.state = 'choose'
        pg.display.update()
        checklist_screen.draw(screen)
        coffee_check.display(screen)
        back_to_choose.display(screen)
    
    def checklist_cup(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if milk_check.draw():
                self.state = 'checklist_milk_cup'
            if coffee_check.draw():
                self.state = 'checklist_coffee_cup'
            if cup_check.draw():
                self.state = 'checklist'
            if back_to_choose.draw():
                self.state = 'choose'
        pg.display.update()
        checklist_screen.draw(screen)
        cup_check.display(screen)
        back_to_choose.display(screen)
        
    def checklist_milk_coffee(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if milk_check.draw():
                self.state = 'checklist_coffee'
            if coffee_check.draw():
                self.state = 'checklist_milk'
            if cup_check.draw():
                self.state = 'checklist_milk_coffee_cup'
            if back_to_choose.draw():
                self.state = 'choose'
        pg.display.update()
        checklist_screen.draw(screen)
        milk_check.display(screen)
        coffee_check.display(screen)
        back_to_choose.display(screen)

    def checklist_milk_coffee_cup(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if milk_check.draw():
                self.state = 'checklist_coffee_cup'
            if coffee_check.draw():
                self.state = 'checklist_milk_cup'
            if cup_check.draw():
                self.state = 'checklist_milk_coffee'
            if back_to_choose.draw():
                self.state = 'choose'
            if begin_drawing_button.draw():
                self.state = 'waiting'
        pg.display.update()
        checklist_screen.draw(screen)
        begin_drawing_button.display(screen)
        milk_check.display(screen)
        coffee_check.display(screen)
        cup_check.display(screen)
        back_to_choose.display(screen)
    
    def checklist_coffee_cup(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if milk_check.draw():
                self.state = 'checklist_milk_coffee_cup'
            if coffee_check.draw():
                self.state = 'checklist_cup'
            if cup_check.draw():
                self.state = 'checklist_coffee'
            if back_to_choose.draw():
                self.state = 'choose'
        pg.display.update()
        checklist_screen.draw(screen)
        coffee_check.display(screen)
        cup_check.display(screen)
        back_to_choose.display(screen)

    def waiting(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if self.id == 1:
                print('Drawing heart')
                base()
                if heart():
                    self.state = 'done'
                self.id = 0
            if self.id == 2:
                print('Drawing rosetta')
                base()
                if rosetta():
                    self.state = 'done'
                self.id = 0
            if self.id == 3:
                print('Drawing random')
                self.id = random.randint(1,2)
                self.id = 0
        pg.display.update()
        waiting_screen.draw(screen)

    def done(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if home_button.draw():
                self.state = 'home'
        pg.display.update()
        done_screen.draw(screen)
        home_button.display(screen)


