import sys, pygame
import math 

windowSize = 900

def main():
    pygame.init()
    size = width, height = (windowSize, windowSize)
    screen = pygame.display.set_mode(size)

    gameLoop(screen)

def gameLoop(screen):
    white = (255, 255, 255)
    blackCell = pygame.image.load("../img/black.png")
    array = readMap()
    futureArray = readMap()
    turn = 1
    aliveCell = 1

    while aliveCell:
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
        pygame.time.delay(700)

def readMap():
    mapData = pygame.image.load(sys.argv[len(sys.argv) - 1]) # loading image
    datas = pygame.image.tostring(mapData, "RGBA")
    squareSize = (int)(len(datas) / 4)
    res = [[0 for i in range(squareSize)] for i in range(squareSize)]
    x = 0
    y = 0
    cell = 0

    for i in range(len(datas)):
        res[x][y] = cell
        x += 1
        if (x == squareSize):
            x = 0
            y += 1
        cell = 0
    return res

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

def updateCells(array, futureArray):
    for line in range(len(array)):
        for column in range(len(array)):
            neighbour = getNeighbour(array, line, column)
            if (array[line][column] == 1):
                if (neighbour == 2):
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

if __name__ == "__main__":
    main()