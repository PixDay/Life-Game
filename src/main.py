##
## 30/08/2020 Fontainebleau
## main.py
## File creator:
## Adrien Colombier
##

import sys, pygame
import math 
import os

from game import *

windowSize = 900
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (30, 50)

def main():
    pygame.init()
    size = width, height = (windowSize, windowSize)
    screen = pygame.display.set_mode(size)

    gameLoop(screen)

def readMap():
    mapData = pygame.image.load(sys.argv[len(sys.argv) - 1]) # loading image
    datas = pygame.image.tostring(mapData, "RGBA")
    squareSize = (int)(math.sqrt((int)(len(datas) / 4)))
    res = [[0 for i in range(squareSize)] for i in range(squareSize)]
    x = 0
    y = 0
    cell = 0

    for i in range(len(datas)):
        if (i % 4 == 0):  
            if (datas[i] == 0 and datas[i + 1] == 0 and datas[i + 2] == 0):
                cell = 1
            i += 4
            res[y][x] = cell
            x += 1
            if (x == squareSize):
                x = 0
                y += 1
            cell = 0
    return res

if __name__ == "__main__":
    main()