import pygame
from circleshape import CircleShape

# Class defining the shot object
class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Draws shot on screen    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), self.position, self.radius, width=2)

    # Updates object location
    def update(self, dt):
        self.position += self.velocity * dt