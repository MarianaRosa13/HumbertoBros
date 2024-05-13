import pygame
from config import *
from assets import *
from class_Humberto import *
from class_Floor import *

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    assets = load_assets()
    #criando jogador
    all_sprites = pygame.sprite.Group()
    all_floors = pygame.sprite.Group()
    all_alunos = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    player = Humberto(groups, assets, 100, 70)
    all_sprites.add(player)
    chao = Floor(groups, assets)
    #aluno = Alunos(groups, assets)
    all_sprites.add(chao)
    all_floors.add(chao)
    #all_alunos.add(aluno)
    DONE = 0
    PLAYING = 1
    state = PLAYING
    keys_down = {}


    # score = 0
    # lives = 3








    #loop principal
    while state != DONE:
        clock.tick(60)
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            if state == PLAYING:
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    keys_down[event.key] = True
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 1
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 1
                    if event.key == pygame.K_SPACE and player.toca_chao == True:
                        player.speedy -= 15
                        #clock.tick(TEMP_VOO)
                        #delay=1
                        #pygame.display.flip()
                        #pygame.event.pump()
                        #pygame.time.delay(delay * 1000) # 1 second == 1000 milliseconds
                        #player.speedy += 1
                if event.type == pygame.KEYUP:
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_LEFT:
                            player.speedx += 1
                        if event.key == pygame.K_RIGHT:
                            player.speedx -= 1
                        

        all_sprites.update()

        
        # if keys_down[K_SPACE] == True:
        #     player.speedy += 1


        hits_floor = pygame.sprite.spritecollide(player, all_floors, False)
        if len(hits_floor) > 0:
            player.toca_chao = True
            player.speedy = 0
        else:
            player.toca_chao = False
        

        hits_aluno = pygame.sprite.spritecollide(player, all_alunos, True)
        # if len(hits_aluno) > 0:
        #     aluno.kill()
        #     sprite humberto acabado
        #     tela vc perdeu

        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(assets['background1'], (-200, -100))
        all_sprites.draw(window)
        
        pygame.display.update()

        #if keys_down[K_SPACE] == True:
         #   player.speedy += 1

    return -1