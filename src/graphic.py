##
## 30/08/2020 Fontainebleau
## graphic.py
## File creator:
## Adrien Colombier
##

import sys, pygame
from main import *

def drawComponents(screen, blackCell, array, turn):
    blackCell = pygame.transform.scale(blackCell, ((int)(windowSize / len(array)), (int)(windowSize / len(array))))
    font = pygame.font.Font('freesansbold.ttf', 24)
    text = font.render('Turn : ' + str(turn), True, (0, 255, 0)) 
    positionX = 0
    positionY = 0

    for subArray in array:
        for cell in subArray:
            if (cell == 1):
                screen.blit(blackCell, (positionX, positionY))
            positionX += (int)(windowSize / len(array))
        positionX = 0
        positionY += (int)(windowSize / len(array))
    screen.blit(text, (10, 10))