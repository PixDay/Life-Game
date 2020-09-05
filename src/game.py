##
## 30/08/2020 Fontainebleau
## game.py
## File creator:
## Adrien Colombier
##

import sys, pygame
from main import *
from graphic import *
from data import *

def gameLoop(screen):
    clock = pygame.time.Clock()
    speed = 1
    white = (255, 255, 255)
    blackCell = pygame.image.load("img/black.png")
    array = readMap()
    futureArray = readMap()
    turn = 1
    aliveCell = 1

    while aliveCell:
        clock.tick(fps * speed)
        aliveCell = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        screen.fill(white)
        drawComponents(screen, blackCell, array, turn)
        updateCells(array, futureArray)
        turn += 1
        pygame.display.update() 
        for subArray in array:
            for cell in subArray:
                if (cell == 1):
                    aliveCell = 1
                    
def updateCells(array, futureArray):
    for line in range(len(array)):
        for column in range(len(array)):
            neighbour = getNeighbour(array, line, column)
            if (array[line][column] == 1):
                if (neighbour == 2 or neighbour == 3):
                    futureArray[line][column] = 1
                else:
                    futureArray[line][column] = 0
            else:
                if (neighbour == 3):
                    futureArray[line][column] = 1
                else:
                    futureArray[line][column] = 0
    for line in range(len(array)):
        for column in range(len(array)):
            array[line][column] = futureArray[line][column]
            futureArray[line][column] = 0

def getNeighbour(array, line, column):
    squareSize = len(array)
    neighbour = 0
    
    #check uper line
    if (line != 0):
        if (array[line - 1][column] == 1):
            neighbour += 1
        #check left
        if (column != 0 and array[line - 1][column - 1] == 1):
            neighbour += 1
        #check right
        if (column != (squareSize - 1) and array[line - 1][column + 1] == 1):
            neighbour += 1
    #check left
    if (column != 0):
        if (array[line][column - 1] == 1):
            neighbour += 1
    #check right
    if (column != (squareSize - 1)):
        if (array[line][column + 1] == 1):
            neighbour += 1
    #check bottom line
    if (line != (squareSize - 1)):
        if (array[line + 1][column] == 1):
            neighbour += 1
        #check left
        if (column != 0 and array[line + 1][column - 1] == 1):
            neighbour += 1
        #check right
        if (column != (squareSize - 1) and array[line + 1][column + 1] == 1):
            neighbour += 1
    return neighbour