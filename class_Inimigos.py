import pygame
from config import *
import random 
class Inimigo(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['aluno']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(-100, WIDTH-ALUNO_WIDTH)
        self.rect.y = random.randint(-0, -ALUNO_HEIGHT)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(0, 0)

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(-100, WIDTH-ALUNO_WIDTH)
            self.rect.y = random.randint(0, -ALUNO_HEIGHT)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(0, 0)