import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # Containers to store groups of game objects
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    # Returns collison as True if distance is less than each object's combined radius    
    def checkCollision(self, ship):
        distance = pygame.math.Vector2.distance_to(self.position, ship.position)
        return distance < self.radius + ship.radius