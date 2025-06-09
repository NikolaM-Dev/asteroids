import pygame
from constants import *


def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0  # Delta Time in seconds

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        dt = clock.tick(FPS) / SECOND_IN_MS
        pygame.display.flip()


if __name__ == "__main__":
    main()
