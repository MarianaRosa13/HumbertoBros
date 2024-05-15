import pygame
from constantes import *
from assets import *
from class_Humberto import *
from class_Floor import *
from class_Inimigos import *
from class_Atividade import *

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    assets = load_assets()
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
    aluno = Inimigo(assets, random.randint(ini+5, (n_blocos-1)*FLOOR_WIDTH+ini), chao.rect.top + 1)
    # for i in range(WIDTH):
    #     chao = Floor(groups, assets, ini + i * FLOOR_WIDTH, i == 0, i ==(WIDTH-1))
    #     all_sprites.add(chao)
    #     all_floors.add(chao)
    # for i in range(-HEIGHT):
    #     profundidade= Floor(groups, assets, -ini - i * FLOOR_HEIGHT, i == 0, i ==(-HEIGHT+1))
    #     all_sprites.add(profundidade)
    #     all_floors.add(profundidade)    
    #aluno = Inimigo(assets, random.randint(ini, (HEIGHT-1)*FLOOR_HEIGHT+ini), chao.rect.top + 1)
    all_alunos.add(aluno)
    all_sprites.add(aluno)
    all_atividades.add(ativ)
    all_sprites.add(ativ)
    DONE = 5
    INI = 0
    PLAYING = 1
    VC_PASSOU = 2
    VC_PERDEU = 3
    state = PLAYING
    keys_down = {}
    #cria Surface mapa
    mapa = pygame.Surface((3000, 1500))

    score = 0
    # Desenhando o score
    # text_surface = assets['score_font'].render("score: {:02d}".format(score), True, (255, 255, 0))
    # text_rect = text_surface.get_rect()
    # text_rect.midtop = (500, 400)    #(WIDTH / 2,  10)
    # window.blit(text_surface, text_rect)

    #font1 = pygame.font.SysFont(None, 60)
    #score_text = font1.render(score, True, (255, 0, 0))

    # lives = 3

    #loop principal
    while state in [PLAYING]:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
            if state == PLAYING:
                if event.type == pygame.KEYDOWN:
                    keys_down[event.key] = True
                    if event.key == pygame.K_SPACE:
                        print('pula')
                        player.pular()
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
                        

        all_sprites.update()

        if player.rect.bottom > HEIGHT - 50:  #chao.rect.bottom:
            pygame.time.delay(TEMP_CAIR)
            state = VC_PERDEU

        player.toca_chao = False
        hits_floor = pygame.sprite.spritecollide(player, all_floors, False)
        for floor in hits_floor:
            player.tocou_chao()
            player.rect.bottom = floor.rect.top
            break

        hits_aluno = pygame.sprite.spritecollide(player, all_alunos, False)
        if len(hits_aluno) > 0:
            aluno.speedx = 0
            player.speedx = 0
            player.rect.bottom +=40
            player.image = assets['humberto_morrendo']
            ######################não faz o abaixo
            pygame.time.delay(TEMP_MORRE)
            print('aquiiiiiii')
            state = VC_PERDEU #tela vc perdeu
            

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
        
        #print('score comeca aqui')
        text_surface = assets['score_font'].render("score: {:02d}".format(score), True, (255, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (400, 300)    #(WIDTH / 2,  10)
        window.blit(text_surface, text_rect)

        hits_atividade = pygame.sprite.spritecollide(player, all_atividades, True)
        if len(hits_atividade) > 0:
            assets['coletando_exercicio'].play()
            ativ.kill()
            score+=1

        mapa.fill((0, 0, 0))  # Preenche com a cor branca
        #camera 
        poscamera = pygame.Rect(player.rect.centerx - WIDTH/2, player.rect.centery - HEIGHT/2,WIDTH,HEIGHT)
        mapa.blit(assets['background1'], (poscamera[0]-200,poscamera[1] -100))
        all_sprites.draw(mapa)
        window.fill((0,0,0))
        pygame.Surface.blit(window, mapa, (0,0), poscamera)
        #window.blit(score_text, (400, 150))

        #mapa.blit(text_surface, text_rect)
        pygame.display.update()

    return state