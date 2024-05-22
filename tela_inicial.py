import pygame
import random
from constantes import *
from game_screen import *

def init_screen(window):
    font1 = pygame.font.Font('assets/PressStart2P-Regular.ttf', 30)
    font2 = pygame.font.Font('assets/PressStart2P-Regular.ttf', 60)
    font3 = pygame.font.Font('assets/PressStart2P-Regular.ttf', 20)
    text1 = font1.render('Bem vindo!', True, (0, 0, 255))
    text2 = font2.render('Humberto Bros', True, (255, 0, 0))
    text3 = font3.render('Pressione enter para começar', True, (255, 0, 0))
    text4 = font3.render('Pressione seta para direita para instruções', True, (255, 0, 0))
    inicial = pygame.image.load('assets/img/Fachada-do-Insper-2.png').convert()
    backgroud_init = pygame.transform.scale(inicial, (BACK_INI_WIDTH, BACK_INI_HEIGHT))
    running = True
    keys_down = {}
    INIT=0 
    state = INIT
    DONE = 5
    while running==True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return DONE
                    running = False
                if event.type == pygame.KEYDOWN:
                    keys_down[event.key] = True
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
        window.blit(text1, (450, 150))
        window.blit(text2, (215, 250))
        window.blit(text3, (300, 400))
        window.blit(text4, (185, 450))
        pygame.display.update()
    return 0