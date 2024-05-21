import pygame
import random
from constantes import *
from game_screen import *

def ganhou_screen(window):
    clock = pygame.time.Clock()
    font1 = pygame.font.SysFont(None, 75)
    font2 = pygame.font.SysFont(None, 65)
    font3 = pygame.font.SysFont(None, 45)
    text1 = font1.render('Você sobreviveu a um dia na firma!', True, (0, 0, 255))
    text2 = font2.render('Tá muito fácil a vida, né?', True, (0, 0, 255))
    text3 = font3.render('Pressione enter para acabar', True, (0, 0, 255))
    running = True
    while running==True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False

        window.fill((255, 255, 0))  # Preenche com a cor amarelo
        window.blit(text1, (130, 160))
        window.blit(text2, (330, 270))
        window.blit(text3, (380, 430))
        pygame.display.update()
    return 0