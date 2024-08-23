import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        radius = self.radius
        self.kill()
        x, y = self.position.x, self.position.y
        
        if radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            radius = self.radius
            x, y = self.position.x, self.position.y
            angle = random.uniform(20.0, 50.0)
            new_v1 = self.velocity.rotate(angle) * 1.2
            new_v2 = self.velocity.rotate(-angle) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            self.kill()
            rock1 = Asteroid(x, y, new_radius)
            rock2 = Asteroid(x, y, new_radius)
            rock1.velocity = new_v1
            rock2.velocity = new_v2
            

            