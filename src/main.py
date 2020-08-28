import sys, pygame

array = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]

def main():
    pygame.init()
    size = width, height = (900, 900)
    screen = pygame.display.set_mode(size)

    gameLoop(screen)

def gameLoop(screen):
    white = (255, 255, 255)
    blackCell = pygame.image.load("../img/black.png")
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        screen.fill(white)
        drawComponents(screen, blackCell)
        pygame.display.flip()

def drawComponents(screen, blackCell):
    blackCell = pygame.transform.scale(blackCell, (300, 300))
    positionX = 0
    positionY = 0

    for subArray in array:
        for cell in subArray:
            if (cell == 1):
                screen.blit(blackCell, (positionX, positionY))
            positionX += 300
        positionX = 0
        positionY += 300

if __name__ == "__main__":
    main()