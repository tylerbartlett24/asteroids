import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    
    
    clock = pygame.time.Clock()
    dt = 0
    
    
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for member in updatable:
            member.update(dt)
            
        for rock in asteroids:
            if rock.collision_detect(player):
                print("Game Over!")
                sys.exit()           
        screen.fill("black")
        
        for object in drawable:
            object.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()