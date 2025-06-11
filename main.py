import pygame

from constants import *
from player import Player


def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0  # Delta Time in seconds

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    Player.containers = (updatable, drawable)
    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)

        for group in drawable:
            group.draw(screen)

        pygame.display.flip()
        dt = clock.tick(FPS) / SECOND_IN_MS


if __name__ == "__main__":
    main()
