import pygame
from config import *


# WIDTH = 1000
# HEIGHT = 600

class Floor(pygame.sprite.Sprite):
    def __init__(self,groups, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['floor']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = 105
        self.rect.bottom = HEIGHT - 50
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets 
    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0