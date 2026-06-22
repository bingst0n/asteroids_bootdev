import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen: pygame.Surface) -> None:
        # must override
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        pass

    def split(self) -> None:
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            newangle = random.uniform(20, 50)
            newvel1 = self.velocity.rotate(newangle) * 1.2
            newvel2 = self.velocity.rotate(-newangle) * 1.2
            newrad = self.radius - ASTEROID_MIN_RADIUS
            newast1, newast2 = Asteroid(self.position[0], self.position[1], newrad), Asteroid(self.position[0], self.position[1], newrad)
            newast1.velocity, newast2.velocity = newvel1, newvel2