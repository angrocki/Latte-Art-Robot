import pygame as pg
import random

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

        # Loads latte button display, depending on type of design
        if self._type == "Heart":
            self._surface = pg.image.load("UI_Images/buttons/Heart.png").convert_alpha()
        elif self._type == "Rosetta":
            self._surface = pg.image.load("UI_Images/buttons/rosetta.png").convert_alpha() ##*****make folder for button images****
        elif self._type == "Random":
            self._surface = pg.image.load("UI_Images/buttons/random.png").convert_alpha()
        
        # Loads latte border around latter button, depending on user selection
        if self._type == "Heart Border":
            self._surface = pg.image.load("UI_Images/buttons/Selection_Circle.png").convert_alpha()
        elif self._type == "Rosetta Border":
            self._surface = pg.image.load("UI_Images/buttons/Selection_Circle.png").convert_alpha()
        elif self._type == "Random Border":
            self._surface = pg.image.load("UI_Images/buttons/Selection_Circle.png").convert_alpha()
        
        # Loads check buttons
        elif self._type == "Milk Check":
            self._surface = pg.image.load("UI_Images/buttons/check.png").convert_alpha()
        elif self._type == "Coffee Check":
            self._surface = pg.image.load("UI_Images/buttons/check.png").convert_alpha()
        elif self._type == "Cup Check":
            self._surface = pg.image.load("UI_Images/buttons/check.png").convert_alpha()
        
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
        # Latte button setup
        if self._type == "Heart":
            self.set_position(800,875)
            self.scale(425,350)
        if self._type == "Rosetta":
            self.set_position(1225,850)
            self.scale(400,325)
        if self._type == "Random":
            self.set_position(1290,500)
            self.scale(525,385)
        
        # Latte border button setup
        if self._type == "Heart Border":
            self.set_position(525,590)
            self.scale(1400,900)
        if self._type == "Rosetta Border":
            self.set_position(920, 590)
            self.scale(1400,900)
        if self._type == "Random Border":
            self.set_position(1325, 590)
            self.scale(1400,900)

        # Check button setup
        if self._type == "Milk Check":
            self.set_position(890,825)
            self.scale(700,400)
        if self._type == "Coffee Check":
            self.set_position(890,950)
            self.scale(700,400)
        if self._type == "Cup Check":
            self.set_position(890,1070)
            self.scale(700,400)
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
            self.set_position(640,650)
        if self._type == "Home":
            self.set_position(640,625)
        if self._type == "Next":
            self.set_position(1100,650)
        if self._type == "Begin Drawing":
            self.set_position(1100,650)
        if self._type == "Back":
            self.set_position(175,650)