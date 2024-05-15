import pygame
from constantes import *


class Humberto(pygame.sprite.Sprite):
    def __init__(self,groups, assets, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['humberto']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedx = 0
        self.speedy = 20
        self.groups = groups
        self.assets = assets 
        self.pulando = True
        self.tempo = pygame.time.get_ticks()

    def update(self):
        #Atualização da posição do Humberto
        #tempo_pass = pygame.time.get_ticks()
        #temp_passado = tempo_pass - self.tempo
        if self.pulando:
           self.rect.y += self.speedy
           self.speedy += 1
        self.rect.x += self.speedx

    def pular(self):
        print('pulou')
        if not self.pulando:
            self.pulando = True
            self.speedy -= 20

    def tocou_chao(self):
        self.pulando = False
        self.speedy = 0
        self.rect.x += self.speedx
        self.rect.y += self.speedy