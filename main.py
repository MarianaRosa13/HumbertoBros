import pygame
from config import *
from assets import *
from tela_inicial import *
from game_screen import *

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



# while state==0:
#     # ----- Trata eventos
#     for event in pygame.event.get():
#         # ----- Verifica consequências
#         if event.type == pygame.QUIT:
#             game = False


#     # ----- Atualiza estado do jogo
#     pygame.display.update()  # Mostra o novo frame para o jogador


pygame.quit()       