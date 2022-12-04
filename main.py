import pygame

pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.display.set_caption('test')

from Game import Game
from Title import Title

if __name__ == '__main__':
    game = Game()
    title = Title()
    
    title.run()

    if not title.scene_active:
        game.run()
