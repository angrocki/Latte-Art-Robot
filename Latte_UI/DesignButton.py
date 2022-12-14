import pygame as pg
from Button import *

class DesignButton(Button):
    """
    A subclass of the Button class that initializes the Latte design buttons on the screen.
    """
    def __init__(self,type):
        '''
        Constructs all necessary attributes to initialize the button image.
        '''
        super().__init__(type)

        # Loads latte button display, depending on type of design
        if self._type == 'Heart':
            self._surface = pg.image.load('UI_Images/buttons/Heart.png').convert_alpha()
        elif self._type == 'Rosetta':
            self._surface = pg.image.load('UI_Images/buttons/rosetta.png').convert_alpha()
        elif self._type == 'Random':
            self._surface = pg.image.load('UI_Images/buttons/random.png').convert_alpha()
        
        # Loads latte border around latter button, depending on user selection
        if self._type == 'Heart Border':
            self._surface = pg.image.load('UI_Images/buttons/Selection_Circle.png').convert_alpha()
        elif self._type == 'Rosetta Border':
            self._surface = pg.image.load('UI_Images/buttons/Selection_Circle.png').convert_alpha()
        elif self._type == 'Random Border':
            self._surface = pg.image.load('UI_Images/buttons/Selection_Circle.png').convert_alpha()
        
        # Loads check buttons
        elif self._type == 'Milk Check':
            self._surface = pg.image.load('UI_Images/buttons/check.png').convert_alpha()
        elif self._type == 'Coffee Check':
            self._surface = pg.image.load('UI_Images/buttons/check.png').convert_alpha()
        elif self._type == 'Cup Check':
            self._surface = pg.image.load('UI_Images/buttons/check.png').convert_alpha()

    def setup(self):
        '''
        Uses the parent class functions 'set_position' and 'scale' to prepare each
        button's position on the screen.
        '''
        # Latte button setup
        if self._type == 'Heart':
            self.set_position(800,875)
            self.scale(425,350)
        if self._type == 'Rosetta':
            self.set_position(1225,850)
            self.scale(400,325)
        if self._type == 'Random':
            self.set_position(1290,500)
            self.scale(525,385)
        
        # Latte border button setup
        if self._type == 'Heart Border':
            self.set_position(525,590)
            self.scale(1400,900)
        if self._type == 'Rosetta Border':
            self.set_position(920, 590)
            self.scale(1400,900)
        if self._type == 'Random Border':
            self.set_position(1325, 590)
            self.scale(1400,900)

        # Check button setup
        if self._type == 'Milk Check':
            self.set_position(290,317)
            self.scale(75,75)
        if self._type == 'Coffee Check':
            self.set_position(290,440)
            self.scale(75,75)
        if self._type == 'Cup Check':
            self.set_position(290,565)
            self.scale(75,75)
