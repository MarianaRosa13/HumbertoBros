import pygame
import random
from constantes import *
from game_screen import *

def passou_screen(window):
    clock = pygame.time.Clock()
    font1 = pygame.font.SysFont(None, 75)
    font2 = pygame.font.SysFont(None, 65)
    font3 = pygame.font.SysFont(None, 45)
    text1 = font1.render('Você passou para a próxima fase!', True, (255, 255, 0))
    text2 = font2.render('Tá fácil a vida, né?', True, (255, 255, 0))
    text3 = font3.render('Pressione enter para continuar', True, (255, 255, 0))
    running = True
    while running==True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False

        window.fill((0, 0, 255))  # Preenche com a cor azul
        window.blit(text1, (150, 160))
        window.blit(text2, (360, 270))
        window.blit(text3, (350, 430))
        pygame.display.update()
    return 1