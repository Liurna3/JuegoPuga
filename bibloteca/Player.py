import pygame
from bibloteca.Control import Control


class Player(pygame.sprite.Sprite):
    """"""

    image_path = "./res/white-blood-cell-100x100.png"
    
    def __init__(self, position, control_id = -1):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # self.surface = pygame.transform.smoothscale(
        #     pygame.image.load(image).convert(), (100, 100))

        self.surface = pygame.image.load(Player.image_path).convert_alpha()
        self.image = self.surface
        self.rect = self.image.get_rect(center=position)

        self.direction = pygame.math.Vector2(0, -1)
        self.speed = 5

        self.angle = 0
        self.rotation_speed = 5

        self.control = Control(control_id=control_id,
                               key_down=pygame.K_s,
                               key_up=pygame.K_w,
                               key_left=pygame.K_a,
                               key_right=pygame.K_d)

    def acelerar(self):
        print(self.direction.x)
        self.rect.move_ip(self.direction * self.speed)

    def rotate(self, delta_angle):
        self.image = pygame.transform.rotate(self.surface, self.angle)
        self.direction.rotate_ip(-delta_angle)
        self.angle = (self.angle + delta_angle) % 360
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):

        self.control.update()

        if self.control.get(Control.LEFT):
            self.rotate(self.rotation_speed)

        if self.control.get(Control.RIGHT):
            self.rotate(-self.rotation_speed)

        if self.control.get(Control.UP):
            self.acelerar()
