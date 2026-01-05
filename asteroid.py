import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        
        log_event("asteroid_split")
        
        angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(angle) * 1.2
        v2 = self.velocity.rotate(-angle) * 1.2
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        for v in (v1, v2):
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = v
