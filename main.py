import pygame
from Game import Game

pygame.init()
pygame.font.init()
pygame.display.set_caption('test')

if __name__ == '__main__':
    game = Game()
    game.run()
