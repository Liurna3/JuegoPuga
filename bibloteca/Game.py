import pygame, sys, time
from bibloteca.settings import *

from bibloteca.Control import Control
from bibloteca.Player import Player
from bibloteca.FoodFactory import FoodFactory
from bibloteca.BitmapText import BitmapText

class Game:
    TICK = pygame.USEREVENT + 1
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    pygame.display.set_caption('biblioteca')
    pygame.time.set_timer(TICK, 500)
    background_image = pygame.image.load("./res/fondo.jpg")
    eat_soud = pygame.mixer.Sound(
        "./res/mixkit-video-game-retro-click-237.wav")
    
    def __init__(self):
        # setup
        self.players = []

        self.display_surface = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT))

        p1 = Player(
            control_id=0,
            position=(CENTER_X - 300, CENTER_Y)
        )

        p1.control = Control(
            control_id=0,
            key_down=pygame.K_s,
            key_up=pygame.K_w,
            key_left=pygame.K_a,
            key_right=pygame.K_d,
            key_fire = pygame.K_z
        )
        
        p2 = Player(
            control_id=1,
            position=(CENTER_X + 300, CENTER_Y)
        )
        
        p2.control = Control(
            control_id=1,
            key_down=pygame.K_k,
            key_up=pygame.K_i,
            key_left=pygame.K_j,
            key_right=pygame.K_l,
            key_fire = pygame.K_b
        )

        self.players.append(p1)
        self.players.append(p2)

        self.food = FoodFactory()
        self.last_time = time.time()
        self.score = 0
        self.max_vidas = 25
        self.delay_tick = 10
        self.lock = True

    def players_update(self):
        for player in self.players:
            player.update()
    
    def players_draw(self):
        for player in self.players:
            player.draw(self.display_surface)

    def addPlayer(self, player):
        self.players.append(player)
    
    
    def loop(self):
        self.display_surface.blit(Game.background_image, (0, 0))

        # event loop
        for event in pygame.event.get():
            if event.type == Game.TICK and self.food.activeFood() < self.max_vidas:
                if self.delay_tick > 0:
                    self.delay_tick -= 1
                else:
                    self.food.create()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # game logic

        self.food.update()

        if self.delay_tick <= 0 and  self.food.activeFood() < self.max_vidas:
            self.players_update()

        self.food.draw(self.display_surface)
        self.players_draw()

        if (self.collide_food(self.players)):
            self.score += 1
            Game.eat_soud.play(0)

        self.draw_ui()

        pygame.display.update()





        
    def collide_food(self, players):
        for player in players:
            if pygame.sprite.spritecollide(player, self.food.group, True):
                return True 





    
    def draw_ui(self):
        nfood = self.food.activeFood()


        if (nfood >= self.max_vidas):
            BitmapText.title(
                self.display_surface,
                "GAME OVER  GAME OVER  GAME OVER",
                color=(255,0,0),
                cap=True
            )

        if self.delay_tick > 0:
            BitmapText.title(
                self.display_surface,
                "¿Preparados?",
                alpha=255/10*self.delay_tick,
                y=0
            )

        
        BitmapText.display(
            self.display_surface,
            "Score: " + str(self.score),
            20,
            20
        )

        height_100 = WINDOW_HEIGHT - 40
        delta = (height_100 / self.max_vidas) * nfood

        height = height_100 - delta
        top = 20 + delta

        pygame.draw.rect(
            surface=self.display_surface,
            border_radius=10,
            color=(0, 255, 0),
            rect=pygame.Rect(WINDOW_WIDTH - 80, top, 60, height),
            width=0
        )


    def run(self):
        # delta time
        while True:
            self.loop()
            pygame.time.Clock().tick(FRAMERATE)