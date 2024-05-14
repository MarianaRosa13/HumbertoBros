import pygame
from constantes import *
from assets import *
from tela_inicial import *
from game_screen import *
from class_Humberto import *
from class_Floor import *
from vc_passou import *
from vc_perdeu import *

pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Humberto Bros')


state = 0
while state != -1:
    if state == 0:
        state = init_screen(window)
    if state == 1:
        state = game_screen(window)
    if state == 2:
        state = passou_screen(window)
    if state == 3:
        state = perdeu_screen(window)
    else:
        state = DONE



    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador


pygame.quit()       