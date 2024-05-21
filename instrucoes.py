import pygame
import random
from constantes import *
from game_screen import * 
from assets import *
from class_Humberto import *
from class_Floor import *
from cenarios import *



def instrucoes_screen(window):
    clock = pygame.time.Clock()
    assets = load_assets()
    all_sprites = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    player = Humberto(groups, assets, 100, 70)
    all_sprites.add(player)
    all_floors = pygame.sprite.Group()
    PLAYING = 1
    INSTRUCOES=6
    DONE=5
    state = INSTRUCOES
    tela=(0,0,0)
    #Processa os eventos (mouse, teclado, botão, etc)
    running = True
    keys_down = {}
    mapa = pygame.Surface((3000, 1500))
    running = True
    cenario = cenarios[4]

    font1 = pygame.font.SysFont(None, 60)
    text1 = font1.render('Bem vindo!', True, (255, 0, 0))

    for l in range(len(cenario)):  #varre o cenário
        for c in range(len(cenario[l])):
            if cenario[l][c] == 'x':  #verifica se a posição tem chão
                isLeft = c == 0 or cenario[l][c-1] != 'x'  #verifica se o chão é o da esquerda
                isRight = c == len(cenario[l])-1 or cenario[l][c+1] != 'x'  #verifica se o chão é o da direita
                chao = Floor(groups, assets, (c)* BLOCK_WIDTH, (l+1)* BLOCK_HEIGHT, isLeft, isRight)
                all_sprites.add(chao)  #coloca o chão nos sprites
                all_floors.add(chao)

    while state in [INSTRUCOES]:
        assets["Trilha_sonora"].play()
        assets['Trilha_sonora'].set_volume(0.5)
        clock.tick(60)
        for event in pygame.event.get():
            if state == INSTRUCOES:
                if event.type == pygame.QUIT:
                    state = DONE
                    running = False
                if event.type == pygame.KEYDOWN:
                    keys_down[event.key] = True
                    if event.key == pygame.K_SPACE:
                        print('pula')
                        player.pular()
                        assets["pulo"].play()
                        assets["pulo"].set_volume(10)
                    if event.key == pygame.K_LEFT:
                        print('esquerda')
                        player.image = assets['humb_esq']
                        player.speedx -= 2
                    if event.key == pygame.K_RIGHT:
                        print('direita')
                        player.image = assets['humb_dir']
                        player.speedx += 2
                if event.type == pygame.KEYUP:
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_LEFT:
                            player.speedx = 0
                            player.image = assets['humberto']
                        if event.key == pygame.K_RIGHT:
                            player.speedx = 0
                            player.image = assets['humberto']
                if player.rect.bottom > WIDTH+40:
                    fase='1'
                    running = False
        hits_floor = pygame.sprite.spritecollide(player, all_floors, False, pygame.sprite.collide_mask)
        for floor in hits_floor:
            player.tocou_chao()
            player.rect.bottom = floor.rect.top
            break
        print('chao:')
        print(len(hits_floor))
        if len(hits_floor) == 0 and not player.pulando and player.speedy == 0:
            player.pulando = False
            player.speedy = 10

        all_sprites.update()
        window.fill((0, 0, 0)) 
        window.blit(text1, (480, 150))  
        all_sprites.draw(window)
        pygame.display.update()             
   
    return 1