import pygame as pg

class Background():
    """
    Displays a background image for the different pages
    """
    def __init__(self, type):

        self._type = type
        size = (1280,720)
        
        if self._type == "Home":
            self._surface = pg.image.load("UI_Images/background/homepage.png").convert_alpha()
            self._surface = pg.transform.scale(self._surface, size)
        elif self._type == "Choose":
            self._surface = pg.image.load("UI_Images/background/choosePattern.png").convert_alpha()
            self._surface = pg.transform.scale(self._surface, size)
        elif self._type == "Checklist":
            self._surface = pg.image.load("UI_Images/background/checkboxes.png").convert_alpha()
            self._surface = pg.transform.scale(self._surface, size)
        elif self._type == "Waiting":
            self._surface = pg.image.load("UI_Images/background/waiting.png").convert_alpha()
            self._surface = pg.transform.scale(self._surface, size)
        elif self._type == "Done":
            self._surface = pg.image.load("UI_Images/background/done.png").convert_alpha()
            self._surface = pg.transform.scale(self._surface, size)
    def display(self,surface):
        '''
        Displays the background on the UI screen
        '''
        surface.blit(self._surface, (0,0))