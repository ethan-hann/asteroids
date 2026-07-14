import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    
    # game entities
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    
    main_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #update game objects here
        updatable.update(dt)
        for item in asteroids:
            if main_player.collides_with(item):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        #-----------------------
        screen.fill("black")
        
        # draw game objects here
        for item in drawable:
            item.draw(screen)
        #-----------------------
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    
    
if __name__ == "__main__":
    main()
