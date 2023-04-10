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



if __name__ == '__main__':
    main()
    