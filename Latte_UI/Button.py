import pygame as pg

class Button(pg.sprite.Sprite):
    """
    Button sprite with functionality for choosing designs etc.

    Attributes:
        _type: The button's functionality type.
        _x: An integer representing the width of the image
        _y: An integer representing the height of the image
        _clicked: A boolean representing whether the button has been clicked or not.
        _rect: The hitbox of the button.

    """
    def __init__(self, type):

        self._type = type
        self._x = 0
        self._y = 0
        self._rect = 0

        self.clicked = True

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

        self._rect = self._surface.get_rect(topleft=(self._x,self._y))

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

    def display(self, surface):
        '''
        Displays the buttons on the UI screen.

        Args:
            screen: 
                The surface of the UI's background display.
        '''
        surface.blit(self._surface, (self._x, self._y))
    
    def click(self):
        '''
        Returns action = True if button has been pressed by the user.
        '''
        action = False
        if self._rect.collidepoint(pg.mouse.get_pos()):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            if pg.mouse.get_pressed()[0] == 0:
                self.clicked = False
        return action
