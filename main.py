import pygame

pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.display.set_caption('test')

from Game import Game

if __name__ == '__main__':
    game = Game()
    game.run()
