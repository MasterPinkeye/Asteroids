import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for drawing in drawable:
            drawing.draw(screen)
        updatable.update(dt)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
