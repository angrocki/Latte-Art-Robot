import pygame as pg
#from ext_ui_test import *
pg.init()

#----------------------------------------------------------------------------------
## SETUP 
#----------------------------------------------------------------------------------
timer = 0

# screen settings 
 
WIDTH, HEIGHT = 1280, 720
size = (WIDTH, HEIGHT)
screen = pg.display.set_mode(size)
home_background = pg.display.set_mode(size)
color = (250, 243, 235)
screen.fill(color)

pg.display.set_caption("Latte Art Display")         # name of window 

clock = pg.time.Clock()                             # set in frames per sec


# dt = clock(tick(60))

#----------------------------------------------------------------------------------
## SPRITE CLASSES (Temp location)
#----------------------------------------------------------------------------------

class Button(pg.sprite.Sprite):
    """
    Button sprite with functionality for choosing designs etc.

    Attributes:
        _type: The button's functionality type.
        _clicked: A boolean representing whether the button has been clicked or not.
        _rect: The hitbox of the button.

    """
    def __init__(self, type):

        self._type = type
        # sets the position
        self._x = 0
        self._y = 0

        self.clicked = True

        # self.clicked = False
        self.rect = 0

    def set_position(self, x, y):
        '''
        Sets the x and y values of the button's position on the screen.

        Args:
            x: 
                An integer representing the x position of the button on the screen.
            y: 
                An integer representing the y position of the button on the screen.
        '''
        self._x = x - self._surface.get_width()/2
        self._y = y - self._surface.get_height()/2

        self.rect = self._surface.get_rect(topleft=(self._x,self._y))

    # def set_rect(self, cen_x, cen_y):
    #     '''
    #     Sets the rectangular hitbox of the button.

    #     Args:
    #         cen_x: 
    #             An integer representing the center x coordinate of the button.
    #         cen_y: 
    #             An integer representing the center y coordinate of the button.
    #     '''
    #     self.rect = self._surface.get_rect(topleft=(cen_x,cen_y))

    def scale(self,x_scale,y_scale):
        '''
        Scales the size of the button.

        Args: 
            x_scale:
                An integer representing the x amount to scale your image by.
            y_scale:
                An integer representing the y amount to scale your image by.
        '''
        self._surface = pg.transform.smoothscale(self._surface, (x_scale, y_scale))

    def scale_gen(self, scale):

        width =  self._surface.get_width()
        height = self._surface.get_height()

        self._surface = pg.transform.scale(self._surface, (int((width*scale)), int(height*scale)))

    def display(self, screen):
        '''
        Displays the buttons on the UI screen.

        Args:
            screen: 
                The surface of the UI's background display.
        '''
        screen.blit(self._surface, (self._x, self._y))
    
    def draw(self):
        action = False
        if self.rect.collidepoint(pg.mouse.get_pos()):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            if pg.mouse.get_pressed()[0] == 0:
                self.clicked = False
        return action

class DesignButton(Button):
    '''
    A subclass of the Button class that initializes the Latte design buttons 
    on the screen.
    '''
    def __init__(self,type):
        '''
        Constructs all necessary attributes to initialize the button image.
        '''
        super().__init__(type)

        # Loads button display, depending on type of design
        if self._type == "Heart":
            self._surface = pg.image.load("UI_Images/buttons/Heart.png").convert_alpha()
        elif self._type == "Rosetta":
            self._surface = pg.image.load("UI_Images/buttons/rosetta.png").convert_alpha() ##*****make folder for button images****
        elif self._type == "Random":
            self._surface = pg.image.load("UI_Images/buttons/random.png").convert_alpha()
        if self._type == "Heart Border":
            self._surface = pg.image.load("UI_Images/buttons/Selection_Circle.png").convert_alpha()
        elif self._type == "Rosetta Border":
            self._surface = pg.image.load("UI_Images/buttons/Selection_Circle.png").convert_alpha()
        elif self._type == "Random Border":
            self._surface = pg.image.load("UI_Images/buttons/Selection_Circle.png").convert_alpha()
        # elif self._type == "Checkbox":
        #     self._surface = pg.image.load("UI_Images/buttons/checkbox.png").convert_alpha()
        # elif self._type == "Check":
        #     self._surface = pg.image.load("UI_Images/buttons/check.png").convert_alpha()
        
        # Loads selection circles
        

    def setup(self):
        '''
        Uses the parent class functions 'set_position' and 'scale' to prepare each
        button's position on the screen.
        '''
        if self._type == "Heart":
            self.set_position(800,875)
            self.scale(425,350)
        if self._type == "Rosetta":
            self.set_position(1225,850)
            self.scale(400,325)
        if self._type == "Random":
            self.set_position(1290,500)
            self.scale(525,385)
        if self._type == "Heart Border":
            self.set_position(525,590)
            self.scale(1400,900)
        if self._type == "Rosetta Border":
            self.set_position(920, 590)
            self.scale(1400,900)
        if self._type == "Random Border":
            self.set_position(1325, 590)
            self.scale(1400,900)

class NavigationButton(Button):
    '''
    A subclass of the Button class that initializes the navigation
    buttons for the UI screen.
    '''
    def __init__(self,type):
        '''
        Constructs all necessary attributes to initialize the button
        image.
        '''
        super().__init__(type)

        # Loads button display, depending on type of navigation button
        if self._type == "Start":
            self._surface = pg.image.load("UI_Images/buttons/start_button.png").convert_alpha()
        elif self._type == "Home":
            self._surface = pg.image.load("UI_Images/buttons/home_button.png").convert_alpha()
        elif self._type == "Next":
            self._surface = pg.image.load("UI_Images/buttons/next_button.png").convert_alpha()
        elif self._type == "Begin Drawing":
            self._surface = pg.image.load("UI_Images/buttons/start_button.png").convert_alpha()
        elif self._type == "Back":
            self._surface = pg.image.load("UI_Images/buttons/back_button.png").convert_alpha()

    def setup(self):
        '''
        Uses the parent class functions 'set_position' and 'scale' to
        prepare each button's position on the screen.
        '''
        if self._type == "Start":
            self.set_position(640,625)
        if self._type == "Home":
            self.set_position(640,625)
        if self._type == "Next":
            self.set_position(1100,625)
        if self._type == "Begin Drawing":
            self.set_position(1100,625)
        if self._type == "Back":
            self.set_position(640,625)

class ChecklistButton(Button):
    def __init__(self,type):
        super().__init__(type)
        if self._type == "Milk Checkbox":
            self._surface = pg.image.load("UI_Images/buttons/checkbox.png").convert_alpha()
        elif self._type == "Coffee Checkbox":
            self._surface = pg.image.load("UI_Images/buttons/checkbox.png").convert_alpha()
        elif self._type == "Cup Checkbox":
            self._surface = pg.image.load("UI_Images/buttons/checkbox.png").convert_alpha()
        elif self._type == "Milk Check":
            self._surface = pg.image.load("UI_Images/buttons/check.png").convert_alpha()
        elif self._type == "Coffee Check":
            self._surface = pg.image.load("UI_Images/buttons/check.png").convert_alpha()
        elif self._type == "Cup Check":
            self._surface = pg.image.load("UI_Images/buttons/check.png").convert_alpha()
        
    def setup(self):
        if self._type == "Milk Checkbox":
            self.scale(800,500)
            self.set_position(500,325)
        if self._type == "Coffee Checkbox":
            self.scale(800,500)
            self.set_position(500,450)      
        if self._type == "Cup Checkbox":
            self.scale(800,500)
            self.set_position(500,575)
            
        if self._type == "Milk Check":
            self.set_position(830,705)
            self.scale(900,700)
        if self._type == "Coffee Check":
            self.set_position(830,830)
            self.scale(900,700)
        if self._type == "Cup Check":
            self.set_position(830,955)
            self.scale(900,700)

      


# naviation images 
start_button = NavigationButton("Start")
start_button.setup()

home_button = NavigationButton("Home")
home_button.setup()

next_button = NavigationButton("Next")
next_button.setup()

begin_drawing_button = NavigationButton("Begin Drawing")
begin_drawing_button.setup()

back_button = NavigationButton("Back")
back_button.setup()

# startbut.display(screen)

# design images
heart = DesignButton("Heart")
heart.setup()
rosetta = DesignButton("Rosetta")
rosetta.setup()
random = DesignButton("Random")
random.setup()

heart_border = DesignButton("Heart Border")
heart_border.setup()
rosetta_border = DesignButton("Rosetta Border")
rosetta_border.setup()
random_border = DesignButton("Random Border")
random_border.setup()

# checklist images
milk_box = ChecklistButton("Milk Checkbox")
milk_box.setup()
coffee_box = ChecklistButton("Coffee Checkbox")
coffee_box.setup()
cup_box = ChecklistButton("Cup Checkbox")
cup_box.setup()
milk_check = ChecklistButton("Milk Check")
milk_check.setup()
coffee_check = ChecklistButton("Coffee Check")
coffee_check.setup()
cup_check = ChecklistButton("Cup Check")
cup_check.setup()

class Background():
    def __init__(self, type):

        self._type = type
        
        if self._type == "Home":
            self._surface = pg.image.load("UI_Images/background/homepage.png").convert_alpha()
            self._surface = pg.transform.scale(self._surface, size)
        elif self._type == "Choose":
            self._surface = pg.image.load("UI_Images/background/choosePattern.png").convert_alpha()
            self._surface = pg.transform.scale(self._surface, size)
        elif self._type == "Checklist":
            self._surface = pg.image.load("UI_Images/background/check_list.png").convert_alpha()
            self._surface = pg.transform.scale(self._surface, size)
        elif self._type == "Waiting":
            self._surface = pg.image.load("UI_Images/background/waiting.png").convert_alpha()
            self._surface = pg.transform.scale(self._surface, size)
        elif self._type == "Done":
            self._surface = pg.image.load("UI_Images/background/done.png").convert_alpha()
            self._surface = pg.transform.scale(self._surface, size)
    def draw(self,surface):
        surface.blit(self._surface, (0,0))



# background images
home_screen = Background("Home")
choose_screen = Background("Choose")
checklist_screen = Background("Checklist")
waiting_screen = Background("Waiting")
done_screen = Background("Done")


class Menu():
    def __init__(self):
        self.state = 'home'

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
            # if event.type == pg.MOUSEBUTTONDOWN:
            #     if heart.rect.collidepoint(pg.mouse.get_pos()):
            #         self.state = 'choose_heart'
            #     if rosetta.rect.collidepoint(pg.mouse.get_pos()):
            #         self.state = 'choose_rosetta'
            #     if random.rect.collidepoint(pg.mouse.get_pos()):
            #         self.state = 'choose_random'
            if heart.draw():
                self.state = 'choose_heart'
            if rosetta.draw():
                self.state = 'choose_rosetta'
            if random.draw():
                self.state = 'choose_random'
        pg.display.update()
        choose_screen.draw(screen)
        heart.display(screen)
        rosetta.display(screen)
        random.display(screen)

    def choose_heart(self):
        '''
        Choose page with heart selected
        '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if heart.draw():
                self.state = 'choose_heart'
            if rosetta.draw():
                self.state = 'choose_rosetta'
            if random.draw():
                self.state = 'choose_random'
            if next_button.draw():
                self.state = 'checklist'
        pg.display.update()
        choose_screen.draw(screen)
        heart.display(screen)
        heart_border.display(screen)
        rosetta.display(screen)
        random.display(screen)
        next_button.display(screen)
        
            
    def choose_rosetta(self):
        '''
        Choose page with rosetta selected
        '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if heart.draw():
                self.state = 'choose_heart'
            if rosetta.draw():
                self.state = 'choose_rosetta'
            if random.draw():
                self.state = 'choose_random'
            if next_button.draw():
                self.state = 'checklist'
        pg.display.update()
        choose_screen.draw(screen)
        heart.display(screen)
        rosetta.display(screen)
        rosetta_border.display(screen)
        random.display(screen)
        next_button.display(screen)

    def choose_random(self):
        '''
        Choose page with random selected
        '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if heart.draw():
                self.state = 'choose_heart'
            if rosetta.draw():
                self.state = 'choose_rosetta'
            if random.draw():
                self.state = 'choose_random'
            if next_button.draw():
                self.state = 'checklist'
        pg.display.update()
        choose_screen.draw(screen)
        heart.display(screen)
        rosetta.display(screen)
        random.display(screen)
        random_border.display(screen)
        next_button.display(screen)
        
    def checklist(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if milk_box.draw():
                self.state = 'checklist_milk'
            if coffee_box.draw():
                self.state = 'checklist_coffee'
            if cup_box.draw():
                self.state = 'checklist_cup'
        pg.display.update()
        checklist_screen.draw(screen)
        milk_box.display(screen)
        coffee_box.display(screen)
        cup_box.display(screen)
    
    def checklist_milk(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if milk_box.draw():
                self.state = 'checklist'
            if coffee_box.draw():
                self.state = 'checklist_milk_coffee'
            if cup_box.draw():
                self.state = 'checklist_milk_cup'  
        pg.display.update()
        checklist_screen.draw(screen)
        milk_box.display(screen)
        coffee_box.display(screen)
        cup_box.display(screen)
        milk_check.display(screen)

    def checklist_coffee(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if milk_box.draw():
                self.state = 'checklist_milk_coffee'
            if coffee_box.draw():
                self.state = 'checklist'
            if cup_box.draw():
                self.state = 'checklist_coffee_cup'  
        pg.display.update()
        checklist_screen.draw(screen)
        milk_box.display(screen)
        coffee_box.display(screen)
        cup_box.display(screen)
        coffee_check.display(screen)
    
    def checklist_cup(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if milk_box.draw():
                self.state = 'checklist_milk_cup'
            if coffee_box.draw():
                self.state = 'checklist_coffee_cup'
            if cup_box.draw():
                self.state = 'checklist'
        pg.display.update()
        checklist_screen.draw(screen)
        milk_box.display(screen)
        coffee_box.display(screen)
        cup_box.display(screen)
        cup_check.display(screen)
        
    def checklist_milk_coffee(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if milk_box.draw():
                self.state = 'checklist_coffee'
            if coffee_box.draw():
                self.state = 'checklist_milk'
            if cup_box.draw():
                self.state = 'checklist_milk_coffee_cup'
        pg.display.update()
        checklist_screen.draw(screen)
        milk_box.display(screen)
        coffee_box.display(screen)
        cup_box.display(screen)
        milk_check.display(screen)
        coffee_check.display(screen)

    def checklist_milk_coffee_cup(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if begin_drawing_button.draw():
                self.state = 'waiting'
            if milk_box.draw():
                self.state = 'checklist_coffee_cup'
            if coffee_box.draw():
                self.state = 'checklist_milk_cup'
            if cup_box.draw():
                self.state = 'checklist_milk_coffee'
        pg.display.update()
        checklist_screen.draw(screen)
        begin_drawing_button.display(screen)
        milk_box.display(screen)
        coffee_box.display(screen)
        cup_box.display(screen)
        milk_check.display(screen)
        coffee_check.display(screen)
        cup_check.display(screen)
    
    def checklist_coffee_cup(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if milk_box.draw():
                self.state = 'checklist_milk_coffee_cup'
            if coffee_box.draw():
                self.state = 'checklist_cup'
            if cup_box.draw():
                self.state = 'checklist_coffee'
        pg.display.update()
        checklist_screen.draw(screen)
        milk_box.display(screen)
        coffee_box.display(screen)
        cup_box.display(screen)
        coffee_check.display(screen)
        cup_check.display(screen)

    def waiting(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if start_button.rect.collidepoint(pg.mouse.get_pos()):
                    self.state = 'waiting' 
        pg.display.update()
        waiting_screen.draw(screen)

    def done(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if start_button.rect.collidepoint(pg.mouse.get_pos()):
                    self.state = 'done' 

menu = Menu()


#----------------------------------------------------------------------------------
## UI LOOP
#----------------------------------------------------------------------------------
running = True
while running:
    menu.state_manager()
    clock.tick(60)
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             running = False
#         if event.type == pg.MOUSEBUTTONDOWN:
#             if startbut.rect.collidepoint(pg.mouse.get_pos()):
#                 startbut.clicked = False
#                 print(startbut.clicked)
#                 testmeui()
            

#     pg.display.flip()
#     print(startbut.clicked)
#     # startbut.display(screen)
#     if startbut.clicked is True:
#         startbut.display(screen)
#         print("if")
    

