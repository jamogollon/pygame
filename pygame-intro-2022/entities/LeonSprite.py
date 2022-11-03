import pygame
from pygame.sprite import Sprite


class LeonSprite(Sprite): #Extiende de la clase Sprite

    def __init__(self, screen):
        super().__init__() # Llama al constructor de Screen
        self.screen = screen

        self.image = pygame.image.load('assets/lion01.png')
        # redimensionar imagen
        self.image = pygame.transform.scale(self.image, (60,60))  # TODO trasladar tamaño a settings

        # generar rect
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # posicionar la imagen
        self.rect.x = self.screen_rect.top
        self.rect.y = self.screen_rect.left

        #Calculamos un valor para el centro
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def update(self):
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blit(self):
        self.screen.blit(self.image, self.rect)