##
## 05/09/2020 Fontainebleau
## menu.py
## File creator:
## Adrien Colombier
##

import sys, pygame
from game import *

fps = 60

def menuLoop(screen):
    clock = pygame.time.Clock()
    white = (255, 255, 255)
    menu = 1
    mousePosition = pygame.mouse.get_pos()
    clicked = 0

    while menu:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        screen.fill(white)
        mousePosition = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == 0:
            clicked = 1
        elif event.type != pygame.MOUSEBUTTONDOWN:
            clicked = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu = 0
        pygame.display.update()
