import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

# Main game function
def main():
    # Initializes the game instance
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Initializes object groups
    asteroids = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Initializes object containers
    Asteroid.containers = (asteroids, updateable, drawable)
    Player.containers = (updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)

    # Initializes field at which asteroids can spawn
    asteroid_field = AsteroidField()

    # Initializes player object, 'ship'
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Creates game loop
    while True:
        screen.fill(BACKGROUND)

        # Draws game objects on screen each 'tick'
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # Ends game loop if session is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateable.update(dt)

        # Checks if asteroid has collided with a non asteroid object
        for asteroid in asteroids:

            # Ends game if asteroid collides with player
            if asteroid.checkCollision(player):
                print("Game Over!")
                exit()

            # Splits or kills asteroid if collided with shot
            for shot in shots:
                if asteroid.checkCollision(shot):
                    shot.kill()
                    asteroid.split()

        # Sets game ticket rate / fps to 60
        clock.tick(60)
        dt = clock.get_time() / 1000

# Calls main
if __name__ == "__main__":
    main()
