import pygame, sys, time
from settings import *

from bibloteca.Player import Player
from bibloteca.FoodFactory import FoodFactory


class Game:

    TICK = pygame.USEREVENT + 1
    BG = pygame.image.load("./res/fondo.jpg")

    def __init__(self):
        # setup
        pygame.time.set_timer(Game.TICK, 500)
        
        self.display_surface = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT))

        self.p1 = Player(position=(100, 100), control_id=0)
        self.p2 = Player(position=(100, 100), control_id=1)

        self.food = FoodFactory()
        self.food.create()

        # self.all_sprites.add(Player( control_id = 1 ))
        self.last_time = time.time()
        self.score = 0

    def loop(self):
        self.display_surface.blit(Game.BG, (0, 0))

        # event loop
        for event in pygame.event.get():
            if event.type == Game.TICK:
                self.food.create()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # game logic

        self.food.update()
        self.food.draw(self.display_surface)

        self.p1.update()
        self.p1.draw(self.display_surface)

        self.p2.update()
        self.p2.draw(self.display_surface)

        if (pygame.sprite.spritecollide(self.p1.hitbox, self.food.group, True)
                or pygame.sprite.spritecollide(self.p2.hitbox, self.food.group,
                                               True)):
            self.score += 1
            print(self.score)

        pygame.display.update()

    def run(self):
        # delta time
        while True:
            # dt = time.time() - self.last_time
            # last_time = time.time()
            self.loop()
            pygame.time.Clock().tick(FRAMERATE)
