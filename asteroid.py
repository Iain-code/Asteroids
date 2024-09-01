import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
         pygame.draw.circle(screen, "orange", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            random_angle2 = random.uniform(20, 50)
            vector1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
            vector2 = pygame.math.Vector2.rotate(self.velocity, random_angle2)
            new_asteroid = self.radius - ASTEROID_MIN_RADIUS
            new_ast = Asteroid(self.position.x, self.position.y, new_asteroid)
            new_ast1 = Asteroid(self.position.x, self.position.y, new_asteroid)
            

            #shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            new_ast1.velocity = vector1 * 1.2
            new_ast.velocity = vector2 * 1.2




            



