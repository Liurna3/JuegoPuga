import pygame, sys, time
from settings import *

from lib.Player import Player


class Game:
    def __init__(self):
        
        # setup
        pygame.init()
        self.display_surface = pygame.display.set_mode(
            (WINDOW_WIDTH,WINDOW_HEIGHT)
        )
        
        pygame.display.set_caption('test')
        self.clock = pygame.time.Clock()
 
    def run(self):
        last_time = time.time()
        all_sprites = pygame.sprite.Group()
        player = Player( (100, 100), "./res/white-blood-cell-100x100.png" )

        all_sprites.add(player)
        
        
        while True:
            
            # delta time
            dt = time.time() - last_time
            last_time = time.time()
 
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                        
            # game logic
            all_sprites.update()
            all_sprites.draw(self.display_surface)
            pygame.display.update()
            self.clock.tick(FRAMERATE)





            
if __name__ == '__main__':
    game = Game()
    game.run()
