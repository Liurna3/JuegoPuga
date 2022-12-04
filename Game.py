import pygame, sys, time
from settings import *

from bibloteca.Control import Control
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

        self.food = FoodFactory()

        self.p1 = Player(
            control_id=0,
            position=(CENTER_X - 300, CENTER_Y)
        )

        self.p1.control = Control(
            control_id=0,
            key_down=pygame.K_s,
            key_up=pygame.K_w,
            key_left=pygame.K_a,
            key_right=pygame.K_d,
            key_fire = pygame.K_z
        )
        
        self.p2 = Player(
            control_id=1,
            position=(CENTER_X + 300, CENTER_Y)
        )
        
        self.p2.control = Control(
            control_id=1,
            key_down=pygame.K_k,
            key_up=pygame.K_i,
            key_left=pygame.K_j,
            key_right=pygame.K_l,
            key_fire = pygame.K_b
        )


        self.last_time = time.time()
        self.score = 0
        self.max_vidas = 3
        self.delay_tick = 10
        self.exit_delay = 0
        self.lock = True
        self.scene_active = True
        self.exiting = False


    def reset(self):
        self.p1.set_position((CENTER_X - 300, CENTER_Y))
        self.p2.set_position((CENTER_X + 300, CENTER_Y))
        
        self.food.group.empty()
        self.food.active = False
        
        self.score = 0
        self.max_vidas = 25
        self.delay_tick = 10
        self.exit_delay = 0
        self.lock = True
        self.scene_active = True
        self.exiting = False


        
    def loop(self):

        # event loop
        for event in pygame.event.get():
            if event.type == Game.TICK:
                self.food.create()
                
                if self.delay_tick > 0:
                    self.delay_tick -= 1
                    
                if self.exit_delay > 0:
                    print(self.exit_delay)
                    self.exit_delay -= 1

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # game logic



        if self.exiting and self.exit_delay == 0:
            self.scene_active = False

        if self.food.activeFood() >= self.max_vidas and not self.exiting:
            self.food.active = False 
            self.exit_delay = 3
            self.exiting = True
        
        if self.delay_tick == 0 and self.exit_delay == 0:
            self.food.active = True
            self.food.update()
            self.p1.update()
            self.p2.update()

        if (self.collide_food(self.p1) or self.collide_food(self.p2)):
            self.score += 1
            Game.eat_soud.play(0)

        self.display_surface.blit(Game.background_image, (0, 0))
        self.food.draw(self.display_surface)
        self.p1.draw(self.display_surface)
        self.p2.draw(self.display_surface)
        self.draw_ui()

        pygame.display.update()





        
    def collide_food(self, player):
        return pygame.sprite.spritecollide(
            player.hitbox,
            self.food.group,
            True
        )





    
    def draw_ui(self):
        nfood = self.food.activeFood()


        if self.exiting:
            BitmapText.title(
                self.display_surface,
                "GAME OVER  GAME OVER  GAME OVER",
                color=(255,0,0),
                cap=True
            )

        if self.delay_tick != 0:
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
        while self.scene_active:
            self.loop()
            pygame.time.Clock().tick(FRAMERATE)
