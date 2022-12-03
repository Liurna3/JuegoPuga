import pygame, sys, time
from settings import *

from bibloteca.Player import Player
from bibloteca.FoodFactory import FoodFactory
from bibloteca.BitmapText import BitmapText


class Game:

    TICK = pygame.USEREVENT + 1
    background_image = pygame.image.load("./res/fondo.jpg")
    eat_soud = pygame.mixer.Sound(
        "./res/mixkit-video-game-retro-click-237.wav")

    def __init__(self):
        # setup
        pygame.time.set_timer(Game.TICK, 500)

        self.display_surface = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT))

        self.p1 = Player(position=(CENTER_X - 300, CENTER_Y), control_id=0)
        self.p2 = Player(position=(CENTER_X + 300, CENTER_Y), control_id=1)

        self.food = FoodFactory()

        self.last_time = time.time()
        self.score = 0

        self.max_vidas = 25

        self.delay_tick = 10

    def loop(self):
        self.display_surface.blit(Game.background_image, (0, 0))

        # event loop
        for event in pygame.event.get():
            if event.type == Game.TICK:
                if self.delay_tick > 0:
                    self.delay_tick -= 1
                else:
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

        if (self.collide_food(self.p1) or self.collide_food(self.p2)):
            self.score += 1
            Game.eat_soud.play(0)
            print(self.score)

        self.draw_ui()

        pygame.display.update()

    def collide_food(self, player):
        return pygame.sprite.spritecollide(player.hitbox, self.food.group,
                                           True)

    def draw_ui(self):
        nfood = self.food.activeFood()

        if (nfood > self.max_vidas):
            BitmapText.display(self.display_surface,
                               "Perdiste",
                               CENTER_X - 270,
                               CENTER_Y - 120,
                               font=BitmapText.TITLE)

        if self.delay_tick > 0:
            BitmapText.display(self.display_surface,
                               "¿Listos?",
                               CENTER_X - 270,
                               CENTER_Y - 120,
                               font=BitmapText.TITLE)
            BitmapText.display(self.display_surface,
                               str(self.delay_tick),
                               CENTER_X - 50,
                               CENTER_Y - 25,
                               font=BitmapText.TITLE)

        BitmapText.display(self.display_surface, "Score: " + str(self.score),
                           20, 20)

        height_100 = WINDOW_HEIGHT - 40
        delta = (height_100 / self.max_vidas) * nfood

        height = height_100 - delta
        top = 20 + delta

        # top_0 = height_100
        # top = top_0 + nfood - self.vidas

        pygame.draw.rect(surface=self.display_surface,
                         border_radius=10,
                         color=(0, 150, 0),
                         rect=pygame.Rect(WINDOW_WIDTH - 80, top, 60, height),
                         width=0)

    def run(self):
        # delta time
        while True:
            # dt = time.time() - self.last_time
            # last_time = time.time()
            self.loop()
            pygame.time.Clock().tick(FRAMERATE)
