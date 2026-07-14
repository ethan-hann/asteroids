import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
import player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    
    # game entities
    main_player = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #update game objects here
        main_player.update(dt)
        #-----------------------
        screen.fill("black")
        
        # draw game objects here
        main_player.draw(screen)
        #-----------------------
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    
    
if __name__ == "__main__":
    main()
