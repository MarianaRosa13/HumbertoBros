import pygame
import random
from constantes import *
from game_screen import *

def init_screen(window):
    clock = pygame.time.Clock()
    font1 = pygame.font.SysFont(None, 60)
    font2 = pygame.font.SysFont(None, 80)
    font3 = pygame.font.SysFont(None, 40)
    text1 = font1.render('Bem vindo!', True, (255, 0, 0))
    text2 = font2.render('Humberto Bros', True, (255, 0, 0))
    text3 = font3.render('Pressione enter para começar', True, (255, 0, 0))
    inicial = pygame.image.load('assets/img/Fachada-do-Insper-2.png').convert()
    backgroud_init = pygame.transform.scale(inicial, (BACK_INI_WIDTH, BACK_INI_HEIGHT))
    running = True
    keys_down = {}
    while running==True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                running = False
                if event.key == pygame.K_RETURN:
                    fase = 1
                    running = False
                    return 1
                elif event.key == pygame.K_RIGHT:
                    print('direita')
                    fase= 6
                    running = False
                    return 6
               

                    

        window.fill((255, 255, 255))  # Preenche com a cor branco
        window.blit(backgroud_init, (0, -50))
        window.blit(text1, (480, 150))
        window.blit(text2, (400, 250))
        window.blit(text3, (400, 400))
        pygame.display.update()
    return 0