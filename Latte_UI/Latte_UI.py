import pygame as pg
from Background import *
from Button import *
from Menu import *

pg.init()

#----------------------------------------------------------------------------------
## SETUP 
#----------------------------------------------------------------------------------
timer = 0

# screen settings 
 
# WIDTH, HEIGHT = 1280, 720
# size = (WIDTH, HEIGHT)
# screen = pg.display.set_mode(size)
# home_background = pg.display.set_mode(size)
# color = (250, 243, 235)
# screen.fill(color)

pg.display.set_caption("Latte Art Display")         # name of window 

clock = pg.time.Clock()                             # set in frames per sec

#----------------------------------------------------------------------------------
## SPRITE CLASSES (Temp location)
#----------------------------------------------------------------------------------

menu = Menu()

#----------------------------------------------------------------------------------
## UI LOOP
#----------------------------------------------------------------------------------
running = True
while running:
    menu.state_manager()
clock.tick(60)
    

