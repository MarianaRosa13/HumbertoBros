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
    all_atividades = pygame.sprite.Group()
    all_cafes = pygame.sprite.Group()
    INSTRUCOES=6
    DONE=5
    VC_PERDEU = 3
    state = INSTRUCOES
    score = 0
    total_ativ = 0
    running = True
    keys_down = {}
    cenario = cenarios[4]

    font1 = pygame.font.SysFont(None, 60)
    font2 = pygame.font.SysFont(None, 40)
    font3 = pygame.font.SysFont(None, 30)
    text1 = font1.render('Bem vindo!', True, (255, 0, 0))
    text2 = font2.render('Pegue a atividade e o café para começar o jogo', True, (255, 0, 0))
    text3 = font3.render('1. Aperte seta para direita para andar pra frente', True, (255, 0, 0))
    text4 = font3.render('2. Aperte seta para esquerda para andar pra trás', True, (255, 0, 0))
    text5 = font3.render('3. Aperte espaço para pular', True, (255, 0, 0))

    for l in range(len(cenario)):  #varre o cenário
        for c in range(len(cenario[l])):
            if cenario[l][c] == 'x':  #verifica se a posição tem chão
                isLeft = c == 0 or cenario[l][c-1] != 'x'  #verifica se o chão é o da esquerda
                isRight = c == len(cenario[l])-1 or cenario[l][c+1] != 'x'  #verifica se o chão é o da direita
                chao = Floor(groups, assets, (c)* BLOCK_WIDTH, (l+1)* BLOCK_HEIGHT, isLeft, isRight)
                all_sprites.add(chao)  #coloca o chão nos sprites
                all_floors.add(chao)
            if cenario[l][c] == 'a':  #verifica se a posição tem atividade
                ativ = Atividade(assets, (c) * BLOCK_WIDTH, (l+1)* BLOCK_HEIGHT)
                all_sprites.add(ativ)  #coloca a atividade nos sprites
                all_atividades.add(ativ)
                total_ativ+=1  #aumenta o total de atividades na tela
                print(total_ativ)
            if cenario[l][c] == 'c':  #verifica se a posição tem café
                cafe = Cafe(assets, (c) * BLOCK_WIDTH, (l+1)* BLOCK_HEIGHT)
                all_sprites.add(cafe)  #coloca o café nos sprites
                all_cafes.add(cafe)

    while state in [INSTRUCOES]:
        # assets["Trilha_sonora"].play()
        # assets['Trilha_sonora'].set_volume(0.5)
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
        
        hits_atividade = pygame.sprite.spritecollide(player, all_atividades, True)
        for ativ in hits_atividade:
            assets['coletando_exercicio'].play()
            assets['coletando_exercicio'].set_volume(10000000000)
            ativ.kill()
            score+=1
        
        hits_cafe = pygame.sprite.spritecollide(player, all_cafes, True)
        if len(hits_cafe) > 0:
            #assets['coletando_exercicio'].play()
            cafe.kill()
            if score == total_ativ:
                state = 1
            else:
                state = VC_PERDEU

        all_sprites.update()
        window.fill((0, 0, 0)) 
        window.blit(text1, (480, 50))
        window.blit(text2, (280, 120))
        window.blit(text3, (70, 170))
        window.blit(text4, (70, 220))
        window.blit(text5, (70, 270))
        all_sprites.draw(window)

        text_surface = assets['score_font'].render("score: {:02d}".format(score), True, (255, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.topleft = (10, 10)
        window.blit(text_surface, text_rect)

        pygame.display.update()             
   
    return 1