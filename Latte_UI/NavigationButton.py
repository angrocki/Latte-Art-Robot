import pygame as pg
from Button import *

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

        # Loads button display depending on type of navigation button
        if self._type == 'Start':
            self._surface = pg.image.load('UI_Images/buttons/start_button.png').convert_alpha()
        elif self._type == 'Home':
            self._surface = pg.image.load('UI_Images/buttons/home_button.png').convert_alpha()
        elif self._type == 'Next':
            self._surface = pg.image.load('UI_Images/buttons/next_button.png').convert_alpha()
        elif self._type == 'Begin Drawing':
            self._surface = pg.image.load('UI_Images/buttons/start_button.png').convert_alpha()
        elif self._type == 'Back':
            self._surface = pg.image.load('UI_Images/buttons/back_button.png').convert_alpha()

    def setup(self):
        '''
        Uses the parent class functions 'set_position' and 'scale' to
        prepare each button's position on the screen.
        '''
        if self._type == 'Start':
            self.set_position(640,650)
        if self._type == 'Home':
            self.set_position(640,625)
        if self._type == 'Next':
            self.set_position(1100,650)
        if self._type == 'Begin Drawing':
            self.set_position(1100,650)
        if self._type == 'Back':
            self.set_position(175,650)