import pygame
from config import *
from assets import *
from class_Humberto import *
from class_Floor import *
from class_Inimigos import *
from class_Atividade import *

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    assets = load_assets()
    #criando jogador
    all_sprites = pygame.sprite.Group()
    all_floors = pygame.sprite.Group()
    all_alunos = pygame.sprite.Group()
    all_atividades = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    player = Humberto(groups, assets, 100, 70)
    ativ = Atividade(assets)
    all_sprites.add(player)
    ini = 105
    n_blocos = 10
    for i in range(n_blocos):
        chao = Floor(groups, assets, ini + i * FLOOR_WIDTH, i == 0, i == n_blocos-1)
        all_sprites.add(chao)
        all_floors.add(chao)
    aluno = Inimigo(assets, random.randint(ini, (n_blocos-1)*FLOOR_WIDTH+ini), chao.rect.top + 1)
    all_alunos.add(aluno)
    all_sprites.add(aluno)
    all_atividades.add(ativ)
    all_sprites.add(ativ)
    DONE = 0
    PLAYING = 1
    VC_PASSOU = 2
    VC_PERDEU = 3
    state = PLAYING
    keys_down = {}


    score = 0
    # lives = 3



    #loop principal
    while state != DONE:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
            if state == PLAYING:
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    keys_down[event.key] = True
                    if event.key == pygame.K_SPACE and player.toca_chao == True:
                        print('pula')
                        player.speedy -= 15
                    if event.key == pygame.K_LEFT:
                        print('esquerda')
                        player.speedx -= 1
                    if event.key == pygame.K_RIGHT:
                        print('direita')
                        player.speedx += 1
                if event.type == pygame.KEYUP:
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_LEFT:
                            player.speedx += 1
                        if event.key == pygame.K_RIGHT:
                            player.speedx -= 1
                        

        all_sprites.update()


        player.toca_chao = False
        hits_floor = pygame.sprite.spritecollide(player, all_floors, False)
        for floor in hits_floor:
            player.toca_chao = True
            player.speedy = 0
            player.rect.bottom = floor.rect.top
            break        

        hits_aluno = pygame.sprite.spritecollide(player, all_alunos, False)
        if len(hits_aluno) > 0:
        #     sprite humberto acabado
            aluno.speedx = 0
            player.speedx = 0
            #state = VC_PERDEU #tela vc perdeu
            pass
        # if len(hits_aluno) > 0:
        #     aluno.kill()
        #     sprite humberto acabado
        #     tela vc perdeu

        hits_inimigos = pygame.sprite.groupcollide(all_alunos, all_floors, False, False)
        for aluno in hits_inimigos:
            floors = pygame.sprite.spritecollide(aluno, all_floors, False)
            for floor in floors:
                if floor.isLeft and aluno.speedx < 0 and aluno.rect.left <= floor.rect.left:
                    aluno.rect.left = floor.rect.left + 1
                    aluno.speedx = -aluno.speedx
                if floor.isRight and aluno.speedx > 0 and aluno.rect.right >= floor.rect.right:
                    aluno.rect.right = floor.rect.right - 1
                    aluno.speedx = -aluno.speedx
        
        hits_atividade = pygame.sprite.spritecollide(player, all_atividades, True)
        if len(hits_atividade) > 0:
        #     sprite humberto acabado
            ativ.kill()
            score+=1

        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(assets['background1'], (-200, -100))
        all_sprites.draw(window)
        
        pygame.display.update()

        #if keys_down[K_SPACE] == True:
         #   player.speedy += 1

    return -1