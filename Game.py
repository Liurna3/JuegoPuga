import pygame, sys, time
from settings import *

from bibloteca.Player import Player


class Game:
    def __init__(self):
        # setup
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

        self.background = pygame.image.load("./res/bg.png")
        

    def run(self):
        last_time = time.time()
        all_sprites = pygame.sprite.Group()
    
        all_sprites.add(Player( (100, 100), 0 ))
        all_sprites.add(Player( (100, 100), 1 ))


        while True:
            self.display_surface.blit(self.background,(0,0))

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


