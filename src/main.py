import sys, pygame

blackCell = pygame.image.load("../img/black.png")

def main():
    pygame.init()
    size = width, height = 1024, 768
    screen = pygame.display.set_mode(size)

    gameLoop(screen)

def gameLoop(screen):
    white = 255, 255, 255
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        screen.fill(white)
        #drawComponents(screen)
        pygame.display.flip()

def drawComponents(screen):
    print("drawComponents function")

if __name__ == "__main__":
    main()