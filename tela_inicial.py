import pygame
import random
from main import * 


def init_screen(screen):
    clock = pygame.time.Clock()
    font1 = pygame.font.SysFont(None, 60)
    font2 = pygame.font.SysFont(None, 80)
    font3 = pygame.font.SysFont(None, 40)
    text1 = font1.render('Bem vindo!', True, (255, 0, 0))
    text2 = font2.render('Humberto Bros', True, (255, 0, 0))
    text3 = font3.render('Pressione enter para começar', True, (255, 0, 0))
    backgroud_init = pygame.image.load('assets/img/Fachada-do-Insper-2.png').convert()
    window.fill((255, 255, 255))  # Preenche com a cor branco
    window.blit(backgroud_init, (0, -50))
    window.blit(text1, (250, 120))
    window.blit(text2, (170, 200))
    window.blit(text3, (170, 320))
    return screen
tela_ini = init_screen(window)