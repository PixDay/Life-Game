##
## 30/08/2020 Fontainebleau
## main.py
## File creator:
## Adrien Colombier
##

import sys, pygame
import os

from game import *

windowSize = 900
fps = 60
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (30, 50)

def main():
    pygame.init()
    size = width, height = (windowSize, windowSize)
    screen = pygame.display.set_mode(size)

    gameLoop(screen)

if __name__ == "__main__":
    main()