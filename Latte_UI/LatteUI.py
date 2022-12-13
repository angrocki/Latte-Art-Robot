import pygame as pg
from Background import *
from Button import *
from Menu import *

#----------------------------------------------------------------------------------
## SETUP 
#----------------------------------------------------------------------------------
pg.init()
pg.display.set_caption("BaristaBot User Interface")         # name of window 
clock = pg.time.Clock()                             # set in frames per sec

#----------------------------------------------------------------------------------
## OBJECTS
#----------------------------------------------------------------------------------
menu = Menu()

#----------------------------------------------------------------------------------
## UI LOOP
#----------------------------------------------------------------------------------
running = True
while running:
    menu.state_manager()
clock.tick(60)
    

