import pygame
from constantes import *
from assets import *
from class_Humberto import *
from class_Floor import *
from class_Inimigos import *
from class_Atividade import *
from class_cafe import *
from cenarios import *

def game_screen(window, fase):
    #Ajuste de velocidade
    clock = pygame.time.Clock()
    assets = load_assets()
    #cria grupos
    all_sprites = pygame.sprite.Group()
    all_floors = pygame.sprite.Group()
    all_alunos = pygame.sprite.Group()
    all_atividades = pygame.sprite.Group()
    all_cafes = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    #cria player
    player = Humberto(groups, assets, 100, 100)
    all_sprites.add(player)
    #define variáveis que serão usadas
    score = 0
    total_ativ = 0

    cenario = cenarios[fase]

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
            if cenario[l][c] == 'I':  #verifica se a posição tem inimigo
                aluno = Inimigo(assets, (c) * BLOCK_WIDTH, (l+1)* BLOCK_HEIGHT + 1)
                all_sprites.add(aluno)  #coloca o inimigo nos sprites
                all_alunos.add(aluno)

    #cria as variáveis de estados do jogo
    DONE = 5
    PLAYING = 1
    VC_PASSOU = 9
    VC_PERDEU = 3
    VC_GANHOU = 2
    state = PLAYING
    keys_down = {}
    #cria Surface mapa
    #mapa = pygame.Surface((3000, 1500))

    pygame.mixer.music.play(-1) #toca a trilha sonora enquanto estiver jogando
    #loop principal
    while state in [PLAYING]:
        
        #assets['Trilha_sonora'].set_volume(0.5)
        clock.tick(60)

        for event in pygame.event.get():  #varre os eventos do jogo
            if event.type == pygame.QUIT:  #verifica se apertou o botão de sair
                state = DONE
            if state == PLAYING:
                if event.type == pygame.KEYDOWN:
                    keys_down[event.key] = True
                    if event.key == pygame.K_SPACE:  #verifica se pressionou espaço
                        print('pula')
                        player.pular()  #função que faz o player pular
                        assets["pulo"].play()  #executa o som de pulo
                        assets["pulo"].set_volume(10)
                    if event.key == pygame.K_LEFT:  #verifica se pressionou seta para a esquerda
                        print('esquerda')
                        player.image = assets['humb_esq']  #sprite do humberto virado para a esquerda
                        player.speedx -= 2
                    if event.key == pygame.K_RIGHT:  #verifica se pressionou seta para a direita
                        print('direita')
                        player.image = assets['humb_dir']   #sprite do humberto virado para a direita
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

        if player.rect.bottom > HEIGHT +40:
            pygame.time.delay(TEMP_CAIR)
            state = VC_PERDEU

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

        hits_aluno = pygame.sprite.spritecollide(player, all_alunos, False, pygame.sprite.collide_mask)
        if len(hits_aluno) > 0:
            aluno.speedx = 0
            player.speedx = 0
            player.rect.bottom +=40
            player.image = assets['humberto_morrendo']
            pygame.time.delay(TEMP_MORRE)
            assets["derrotado"].play()
            assets["derrotado"].set_volume(10)
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
        

        hits_atividade = pygame.sprite.spritecollide(player, all_atividades, True)
        for ativ in hits_atividade:
            assets['coletando_exercicio'].play()
            assets['coletando_exercicio'].set_volume(10000000000)
            ativ.kill()
            score+=1
        
        hits_cafe = pygame.sprite.spritecollide(player, all_cafes, True)
        if len(hits_cafe) > 0:
            #assets['coletando_exercicio'].play()
            if fase==3:
                cafe.kill()
                if score == total_ativ:
                    state = VC_GANHOU
                else:
                    state = VC_PERDEU
            else:
                cafe.kill()
                if score == total_ativ:
                    state = VC_PASSOU
                else:
                    state = VC_PERDEU

        pygame.display.update()

        window.fill((255,255,255))
        if fase == 1:
            window.blit(assets['background1'], (0, 0))
        elif fase == 2:
            window.blit(assets['background2'], (0, 0))
        elif fase == 3:
            window.blit(assets['background3'], (0, 0))



        # mapa.fill((0, 0, 0))  # Preenche com a cor branca
        # #camera 
        # poscamera = pygame.Rect(player.rect.centerx - WIDTH/2, player.rect.centery - HEIGHT/2,WIDTH,HEIGHT)
        # mapa.blit(assets['background1'], (poscamera[0]-100,poscamera[1] -100))
        all_sprites.draw(window)

        # pygame.Surface.blit(window, mapa, (0,0), poscamera)

        #print('score comeca aqui')
        text_surface = assets['score_font'].render("score: {:02d}".format(score), True, (255, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.topleft = (10, 10)
        window.blit(text_surface, text_rect)

        #mapa.blit(text_surface, text_rect)

    return state