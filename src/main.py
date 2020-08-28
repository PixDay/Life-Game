import sys, pygame

def main():
    pygame.init()
    size = width, height = (900, 900)
    screen = pygame.display.set_mode(size)

    gameLoop(screen)

def gameLoop(screen):
    white = (255, 255, 255)
    blackCell = pygame.image.load("../img/black.png")

    #imageData = pygame.image.load("../map/3x3.png") # loading image
    #datas = pygame.image.tostring(imageData, "RGBA")
    #print(datas)
    #print(len(datas) / 4)
    array = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
    futureArray = [[]]
    turn = 1

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        screen.fill(white)
        drawComponents(screen, blackCell, array, turn)
        pygame.display.update() 

def drawComponents(screen, blackCell, array, turn):
    blackCell = pygame.transform.scale(blackCell, (300, 300))
    positionX = 0
    positionY = 0
    font = pygame.font.Font('freesansbold.ttf', 16)
    text = font.render('Turn : ' + str(turn), True, (0, 255, 0)) 

    for subArray in array:
        for cell in subArray:
            if (cell == 1):
                screen.blit(blackCell, (positionX, positionY))
            positionX += 300
        positionX = 0
        positionY += 300
    screen.blit(text, (10, 10))

if __name__ == "__main__":
    main()