import sys, pygame

def main():
    pygame.init()
    size = width, height = (1024, 768)
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
    blackCell = pygame.transform.scale(blackCell, (10,10))
    screen.blit(blackCell, (10, 10))

if __name__ == "__main__":
    main()