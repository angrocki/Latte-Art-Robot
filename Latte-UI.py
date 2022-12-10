import pygame as pg
from ext_ui_test import *
pg.init()

#----------------------------------------------------------------------------------
## SETUP 
#----------------------------------------------------------------------------------
timer = 0

# screen settings 
 
WIDTH, HEIGHT = 1280, 720
size = (WIDTH, HEIGHT)
screen = pg.display.set_mode(size)
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
        self._x = x
        self._y = y

        self.rect = self._surface.get_rect(topleft=(x,y))

    def set_rect(self, cen_x, cen_y):
        '''
        Sets the rectangular hitbox of the button.

        Args:
            cen_x: 
                An integer representing the center x coordinate of the button.
            cen_y: 
                An integer representing the center y coordinate of the button.
        '''
        self.rect = self._surface.get_rect(topleft=(cen_x,cen_y))

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

    def display(self, screen):
        '''
        Displays the buttons on the UI screen.

        Args:
            screen: 
                The surface of the UI's background display.
        '''
        screen.blit(self._surface, (self._x, self._y))


class DesignButton(Button):
    '''
    A subclass of the Button class that initializes the Latte design buttons 
    on the screen.
    '''
    def __init__(self, x, y, type):
        '''
        Constructs all necessary attributes to initialize the button image.
        '''
        super().__init__(x, y, type)

        # Loads button display, depending on type of design
        if self._type == "Heart":
            self._surface = pg.image.load("").convert_alpha()
        elif self._type == "Rosetta":
            self._surface = pg.image.load("").convert_alpha() ##*****make folder for button images****

    def setup(self):
        '''
        Uses the parent class functions 'set_position' and 'scale' to prepare each
        button's position on the screen.
        '''
        if self._type == "Heart":
            self.set_position(100,20)
            self.scale(95,95)
            self.set_rect()
            
        if self._type == "Rosetta":
            self.set_position(100,20)
            self.scale(95,95)
            self.set_rect()


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
        super(NavigationButton, self).__init__(type)

        # Loads button display, depending on type of navigation button
        if self._type == "Start":
            self._surface = pg.image.load("button_temp.png").convert_alpha()
        elif self._type == "Home":
            self._surface = pg.image.load("").convert_alpha()
        elif self._type == "Begin Drawing":
            self._surface = pg.image.load("").convert_alpha()
        elif self._type == "Back":
            self._surface = pg.image.load("button_temp.png").convert_alpha()

    def setup(self):
        '''
        Uses the parent class functions 'set_position' and 'scale' to
        prepare each button's position on the screen.
        '''
        if self._type == "Start":
            self.set_position(540,400)
            self.scale(200,200)
            self.set_rect(540,400)
        if self._type == "Home":
            self.set_position(900,30)
            self.scale(95,95)
        if self._type == "Begin Drawing":
            self.set_position(900,30)
            self.scale(95,95)
        if self._type == "Back":
            self.set_position(900,30)
            self.scale(95,95)


# temp images 
startbut = NavigationButton("Start")
startbut.setup()
# startbut.display(screen)
backbut = NavigationButton("Back")   
backbut.setup() 
homebut = NavigationButton("home")
homebut.setup()  

class Menu():
    def __init__(self):
        self.state = 'home'

    def state_manager(self):
        if self.state == 'home':
            self.home()
        elif self.state == 'choose':
            self.choose()
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
                if startbut.rect.collidepoint(pg.mouse.get_pos()):
                    self.state = 'choose' 
        
        pg.display.update()
        startbut.display(screen)

    def choose(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if startbut.rect.collidepoint(pg.mouse.get_pos()):
                    self.state = 'choose' 
        
        pg.display.update()
        startbut.display(screen)

    def waiting():
        pass

    def done():
        pass

menu = Menu()

#----------------------------------------------------------------------------------
## UI LOOP
#----------------------------------------------------------------------------------
running = True
while running:
    menu.state_manager()
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
    

