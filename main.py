import pygame
import sys



def main():
    print(pygame.__version__)

    screen = pygame.display.set_mode(size=(1280, 720))

    while True:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        # drawing
        pygame.draw.rect(screen, (50, 100, 150), pygame.Rect(10, 50, 200, 100))
        pygame.display.flip()



if __name__ == '__main__':
    main()
