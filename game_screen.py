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
    groups = {}
    groups['all_sprites'] = all_sprites
    player = Humberto(groups, assets, 100, 70)
    all_sprites.add(player)
    chao = Floor(groups, assets)
    all_sprites.add(chao)
    all_floors.add(chao)
    

    DONE = 0
    PLAYING = 1
    #EXPLODING = 2
    state = PLAYING
    keys_down = {}
    #loop principal
    while state != DONE:
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            if state == PLAYING:
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    keys_down[event.key] = True
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 8
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 8
                    if event.key == pygame.K_SPACE:
                        player.speedy += 5
                        #wait
                        #logo depois: player.speedy -= 5
                if event.type == pygame.KEYUP:
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_LEFT:
                            player.speedx += 8
                        if event.key == pygame.K_RIGHT:
                            player.speedx -= 8 

        all_sprites.update()

        hits = pygame.sprite.spritecollide(player, all_floors, False)
        if len(hits) > 0:
            player.speedy = 0

        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(assets['background1'], (-200, -100))
        all_sprites.draw(window)
        
        pygame.display.update()
    return -1
