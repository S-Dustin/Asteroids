import pygame
import random
from circleshape import CircleShape
from constants import *

# Class for asteroid objects
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Displays asteroid on screen    
    def draw(self, screen):
        pygame.draw.circle(screen, (200, 200, 200), self.position, self.radius, width=2)

    # Updates position of asteroid
    def update(self, dt):
        self.position += self.velocity * dt

    # Method to split an asteroid into two if shot
    def split(self):
        self.kill()

        # Does not allow small asteroids to be split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Generates angle for new asteroids
        angle = random.uniform(20, 50)

        # Creates two smaller and faster asteroid objects using previous astroid's position and new angle
        for i in range(2):
            asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            if i == 0:
                asteroid.velocity = (self.velocity.rotate(angle)) * 2
            else:
                asteroid.velocity = (self.velocity.rotate(-angle)) * 2