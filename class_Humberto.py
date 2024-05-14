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
        self.speedy = 0
        self.groups = groups
        self.assets = assets 
        self.toca_chao = False
        self.tempo = pygame.time.get_ticks()
    def update(self):
        #Atualização da posição do Humberto
        tempo_pass = pygame.time.get_ticks()
        temp_passado = tempo_pass - self.tempo
        if (temp_passado >TEMP_VOO) and self.toca_chao == False:
            self.speedy +=0.5



        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        #Mantem o Humberto na tela
        # if self.rect.right > WIDTH:
        #     self.rect.right = WIDTH
        # if self.rect.left < 0:
        #     self.rect.left = 0