import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        velocity_vector1 = self.velocity.rotate(random_angle)
        velocity_vector2 = self.velocity.rotate(-random_angle)

        new_radious = self.radius - ASTEROID_MIN_RADIUS

        x, y = self.position[0], self.position[1]
        asteroid1 = Asteroid(x, y, new_radious)
        asteroid2 = Asteroid(x, y, new_radious)

        VELOCITY_BOOST = 1.2
        asteroid1.velocity = velocity_vector1 * VELOCITY_BOOST
        asteroid2.velocity = velocity_vector2 * VELOCITY_BOOST
