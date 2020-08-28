import sys, pygame

def main():
    pygame.init()
    size = width, height = 1024, 768
    speed = [2, 2]
    black = 255, 255, 255

    screen = pygame.display.set_mode(size)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        screen.fill(black)
        pygame.display.flip()

if __name__ == "__main__":
    # execute only if run as a script
    main()