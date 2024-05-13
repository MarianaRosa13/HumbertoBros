import pygame
from config import *
import random 
class Inimigo(pygame.sprite.Sprite):
    def __init__(self, assets, x, bottom):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['aluno']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = bottom
        self.speedx = random.randint(0, 1)*2-1
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        #self.rect.y += self.speedy
        if self.rect.right < 0 or self.rect.left > WIDTH: #or self.rect.right<tam chao or self.rect.left>tam chao
            self.rect.x -= self.speedx
            #self.rect.x = random.randint(-100, WIDTH-ALUNO_WIDTH)
            self.speedx = random.randint(-1, 1)