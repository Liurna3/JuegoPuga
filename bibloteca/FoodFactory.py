import pygame
import random

from settings import *

class Food(pygame.sprite.Sprite):

    image_path = "./res/cancer.png"

    def __init__(self, position = (0,0)):
        pygame.sprite.Sprite.__init__(self)

        self.surface = pygame.image.load(Food.image_path).convert_alpha()
        self.image = self.surface
        self.rect = self.image.get_rect(center=position)
        

class FoodFactory():
    def __init__(self):
        self.group = pygame.sprite.Group()

    def create(self):
        self.group.add(Food(
            position=(random.randint(0+70, WINDOW_WIDTH-70),random.randint(0+70, WINDOW_HEIGHT-70))
        ))
        
    def update(self):
        self.group.update()        
        pass

    def draw(self, surface):
        self.group.draw(surface)
        pass
        
        
