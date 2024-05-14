import pygame
from constantes import *
#import random

# WIDTH = 1000
# HEIGHT = 600

class Floor(pygame.sprite.Sprite):
    def __init__(self,groups, assets, x, isLeft, isRight):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['floor']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.bottom = HEIGHT - 50
        # for i in range(20):
        #     self.rect.centerx = i
        #     self.rect.bottom = HEIGHT - 50
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets
        self.isLeft = isLeft
        self.isRight = isRight



        # self.rect.x = random.randint(0, WIDTH-FLOOR_WIDTH)
        # self.rect.y = random.randint(-100, -FLOOR_HEIGHT)
        # self.speedx = random.randint(-3, 3)
        # self.speedy = random.randint(2, 9)


    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0