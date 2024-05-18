import pygame
import random
from constantes import *
from game_screen import *

#pygame.init()

# assets["derrotado"]=pygame.mixer.Sound("assets/sdx/derrotado.wav")

DONE = 5
PLAYING = 1

def perdeu_screen(window):
    clock = pygame.time.Clock()
    font1 = pygame.font.SysFont(None, 80)
    font2 = pygame.font.SysFont(None, 60)
    font3 = pygame.font.SysFont(None, 40)
    text1 = font1.render('Você perdeu!', True, (255, 0, 0))
    text2 = font2.render('Tenta de novo semestre que vem!', True, (255, 0, 0))
    text3 = font3.render('Pressione enter para recomeçar', True, (255, 0, 0))
    #inicial = pygame.image.load('assets/img/Fachada-do-Insper-2.png').convert()
    #Processa os eventos (mouse, teclado, botão, etc)
    running = True
    while running==True:
        #Ajusta a velocidade do jogo.
        #clock.tick(FPS)
        #Processa os eventos (mouse, teclado, botão, etc)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #state = DONE
                running = False
            if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_KP_ENTER:
                #state = PLAYING
                fase='1' #antes
                running = False
        # assets["derrotado"].play()
        # assets["derrotado"].set_volume(10)
        window.fill((0, 0, 0))  # Preenche com a cor preto
        window.blit(text1, (380, 170))
        window.blit(text2, (230, 280))
        window.blit(text3, (350, 430))
        pygame.display.update()
    return 1