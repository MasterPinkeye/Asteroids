import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
from player import *


class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        ang1 = self.velocity.rotate(random.uniform(20, 50))
        ang2 = self.velocity.rotate(random.uniform(-20, -50))
        rad = self.radius = (self.radius - ASTEROID_MIN_RADIUS)
        ast1 = Asteroid(self.position.x, self.position.y , rad)
        ast2 = Asteroid(self.position.x, self.position.y, rad)
        ast1.velocity = ang1 * 1.2
        ast2.velocity = ang2 * 1.2
