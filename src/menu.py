##
## 05/09/2020 Fontainebleau
## menu.py
## File creator:
## Adrien Colombier
##

import sys, pygame
from main import *
from graphic import *
from data import *

def menuLoop(screen):
    clock = pygame.time.Clock()
    menu = 1

    while menu:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
