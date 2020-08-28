import sys, pygame
import math 

#imageData = pygame.image.load("../map/3x3.png") # loading image
#datas = pygame.image.tostring(imageData, "RGBA")
#print(datas)
#print(len(datas) / 4)


def main():
    pygame.init()
    size = width, height = (900, 900)
    screen = pygame.display.set_mode(size)

    gameLoop(screen)

def gameLoop(screen):
    white = (255, 255, 255)
    blackCell = pygame.image.load("../img/black.png")
    array = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
    futureArray = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
    turn = 1

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        screen.fill(white)
        drawComponents(screen, blackCell, array, turn)
        updateCells(array, futureArray)
        turn += 1
        pygame.display.update() 
        pygame.time.delay(700)

def drawComponents(screen, blackCell, array, turn):
    blackCell = pygame.transform.scale(blackCell, (300, 300))
    font = pygame.font.Font('freesansbold.ttf', 16)
    text = font.render('Turn : ' + str(turn), True, (0, 255, 0)) 
    positionX = 0
    positionY = 0

    for subArray in array:
        for cell in subArray:
            if (cell == 1):
                screen.blit(blackCell, (positionX, positionY))
            positionX += 300
        positionX = 0
        positionY += 300
    screen.blit(text, (10, 10))

def updateCells(array, futureArray):
    for line in range(3):
        for column in range(3):
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
    for line in range(3):
        for column in range(3):
            array[line][column] = futureArray[line][column]

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