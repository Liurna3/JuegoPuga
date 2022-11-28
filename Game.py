import pygame, sys, time
from settings import *

from bibloteca.Player import Player
from bibloteca.FoodFactory import FoodFactory


class Game:

    BG = pygame.image.load("./res/bg.png")
    
    def __init__(self):
        # setup
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

        self.p1 = Player( position=(100,100), control_id = 0 )

        self.food = FoodFactory();
        self.food.add()
        
        # self.all_sprites.add(Player( control_id = 1 ))
        self.last_time = time.time()

    def loop(self):
        self.display_surface.blit(Game.BG,(0,0))
        
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()        

        # game logic

        self.food.update()
        self.food.draw(self.display_surface)
        
        self.p1.update()
        self.p1.draw(self.display_surface)

        pygame.sprite.spritecollide(self.p1.hitbox, self.food.group, True)
        
        pygame.display.update()

        
    def run(self):
        # delta time
        while True:
            # dt = time.time() - self.last_time
            # last_time = time.time()
            self.loop()
            pygame.time.Clock().tick(FRAMERATE)
            
            
