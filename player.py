import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):
    def __init__(self, x: float, y:float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0
    
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt: float) -> None:
        self.rotation += dt * PLAYER_TURN_SPEED

    def update(self, dt: float) -> None:
        self.cooldown -= dt
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)
        
        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt) # - dt to add a coeff of -1 to the whole expression -> backwards movement

        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt: float) -> None:
        move_vector = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SPEED * dt
        self.position += move_vector

    def shoot(self):
        if self.cooldown <= 0:
            shot = Shot(self.position[0], self.position[1])
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS