import pygame

pygame.font.init()

class BitmapText:
    """"""

    # estilos del texto
    TITLE = pygame.font.SysFont('Consolas', 25)
    NORMAL = pygame.font.SysFont('Consolas', 100)

    def __init__(self):
        pass

    @classmethod
    def display(cls, surface, text, x, y, color=(255,255,255), font=None):
        if (font is None): font = BitmapText.NORMAL
        text_surface = font.render(text, False, color)
        surface.blit(text_surface, pygame.math.Vector2(x, y))
