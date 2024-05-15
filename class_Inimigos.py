import pygame
from constantes import *
import random 
class Inimigo(pygame.sprite.Sprite):
    def __init__(self, assets, x, bottom):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['aluno']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = bottom
        self.speedx = 1
        self.speedy = 0
        self.assets = assets

    def update(self):
        self.rect.x += self.speedx
        #self.rect.y += self.speedy
        if self.rect.right < 0 or self.rect.left > WIDTH: #mantem o aluno na tela, tirar??
            self.rect.x -= self.speedx
            #self.rect.x = random.randint(-100, WIDTH-ALUNO_WIDTH)
            self.speedx = random.randint(-1, 1)
        if self.speedx > 0:
            self.image = self.assets['aluno_d']
        else:
            self.image = self.assets['aluno']
