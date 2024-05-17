import pygame
from constantes import *
import random 
class Cafe(pygame.sprite.Sprite):
    def __init__(self, assets, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['cafe']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.bottom = 400 #depende da altura do chao, mas o chao tbm é random
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy