import pygame, sys, time
from bibloteca.settings import *

from bibloteca.Control import Control
from bibloteca.BitmapText import BitmapText

class Title:

    title_image = "./res/title.png"
    background_image = pygame.image.load("./res/fondoInicio.jpg")
    
    def __init__(self):
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.title = pygame.image.load(Title.title_image).convert_alpha()

        self.image_rect = self.title.get_rect()
        self.image_rect.centerx = self.window.get_rect().centerx
        self.image_rect.centery = self.window.get_rect().centery-200

        self.control = Control(
            control_id=0,
            key_down=pygame.K_s,
            key_up=pygame.K_w,
            key_left=pygame.K_a,
            key_right=pygame.K_d,
            key_fire=pygame.K_z,
        )
        
        self.dificultad_text = [
            "  Fácil  >",
            "< Normal >",
            "< Difícil "
        ]
        self.vidasdDificultad = [25, 15, 8]

        self.max_dificultad = len(self.dificultad_text) - 1
        self.dificultad = 0

        self.lock = True
        
        self.scene_active = True
        self.signal = "Hola"
        

    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if self.control.get(Control.RIGHT) and self.dificultad < self.max_dificultad and self.lock:
            self.dificultad += 1
            self.lock = False
            
        if self.control.get(Control.LEFT) and self.dificultad > 0 and self.lock:
            self.dificultad -= 1
            self.lock = False

        if not( self.control.get(Control.LEFT) or self.control.get(Control.RIGHT)):
            self.lock = True

        if self.control.get(Control.FIRE):
            self.scene_active = False
            
        self.window.blit(Title.background_image, (0, 0))
        self.window.blit(self.title,self.image_rect )

        BitmapText.title(
            self.window,
            self.get_dificultadText(),
            font=BitmapText.DEFAULT,
            cap=True
        )
        
        pygame.display.update()

    def get_dificultadText(self):
        return self.dificultad_text[self.dificultad]
    
    def getDificultad(self):
        return self.vidasdDificultad[self.dificultad];
    
    def run(self):
        while self.scene_active:
            self.loop()
            
        return self.signal
    
