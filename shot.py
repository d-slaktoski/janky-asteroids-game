from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, PLAYER_SHOOT_SPEED)

    def draw(self, surface):
        pygame.draw.circle(surface, "yellow", (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        self.position += self.velocity * dt