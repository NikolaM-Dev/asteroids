import sys

import pygame

from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player


def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0  # Delta Time in seconds

    asteroids = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)

        for group in drawable:
            group.draw(screen)

        for asteroid in asteroids:
            if asteroid.are_colliding(player):
                print("Game over!")
                sys.exit()

        pygame.display.flip()
        dt = clock.tick(FPS) / SECOND_IN_MS


if __name__ == "__main__":
    main()
