import pygame
from config import *


class Humberto(pygame.sprite.Sprite):
    def __init__(self,groups, assets, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['humberto']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedx = 0
        self.speedy = 2
        self.groups = groups
        self.assets = assets 
    def update(self):
        #Atualização da posição do Humberto
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        #Mantem o HUmberto na tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0