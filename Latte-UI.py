import pygame as pg

pg.init()

#----------------------------------------------------------------------------------
## SETUP 
#----------------------------------------------------------------------------------
timer = 0

# screen settings 
 
WIDTH, HEIGHT = 1280, 720
size = (WIDTH, HEIGHT)
screen = pg.display.set_mode(size)


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
        _surface: An image of the button.
        _type: The button's functionality type.

    """
    def __init__(self, type):

        self._type = type
        # sets the position
        self._x = 0
        self._y = 0

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

    def scale(self,x_scale,y_scale):
        '''
        Scales the size of the button.

        Args: 
            x_scale:
                An integer representing the x amount to scale your
                image by.
            y_scale:
                An integer representing the y amount to scale your
                image by.
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
    A subclass of the Button class that initializes the Latte design
    buttons on the screen.
    '''
    def __init__(self, x, y, type):
        '''
        Constructs all necessary attributes to initialize the button
        image.
        '''
        super().__init__(x, y, type)

        # Loads button display, depending on type of design
        if self._type == "Heart":
            self._surface = pg.image.load("").convert_alpha()
        elif self._type == "Rosetta":
            self._surface = pg.image.load("").convert_alpha() ##*****make folder for button images****

    def setup(self):
        '''
        Uses the parent class functions 'set_position' and 'scale' to
        prepare each button's position on the screen.
        '''
        if self._type == "Heart":
            self.set_position(100,20)
            startbut.scale(95,95)
        if self._type == "Rosetta":
            self.set_position(100,20)
            startbut.scale(95,95)


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
        elif self._type == "Next Drink":
            self._surface = pg.image.load("").convert_alpha()

    def setup(self):
        '''
        Uses the parent class functions 'set_position' and 'scale' to
        prepare each button's position on the screen.
        '''
        if self._type == "Start":
            self.set_position(900,30)
            startbut.scale(95,95)
        if self._type == "Home":
            self.set_position(900,30)
            startbut.scale(95,95)
        if self._type == "Begin Drawing":
            self.set_position(900,30)
            startbut.scale(95,95)
        if self._type == "Next Drink":
            self.set_position(900,30)
            startbut.scale(95,95)
        

# temp images 
startbut = NavigationButton("Start")
startbut.setup()
startbut.display(screen)

#----------------------------------------------------------------------------------
## UI LOOP
#----------------------------------------------------------------------------------
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.display.update()
