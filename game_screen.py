import pygame
from constantes import *
from assets import *
from class_Humberto import *
from class_Floor import *
from class_Inimigos import *
from class_Atividade import *
from class_cafe import *
from cenarios import *

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    assets = load_assets()
    all_sprites = pygame.sprite.Group()
    all_floors = pygame.sprite.Group()
    all_alunos = pygame.sprite.Group()
    all_atividades = pygame.sprite.Group()
    all_cafes = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    player = Humberto(groups, assets, 100, 70)
    # ativ = Atividade(assets, x, y)
    # cafe = Cafe(assets)
    all_sprites.add(player)
    ini = 105
    n_blocos = 10
    score = 0
    total_ativ = 0

    # fase=1
    # if fase==1:
    #     for l in range(len(cenario_1fase)):
    #         for c in range(len(cenario_1fase[l])):
    #             if cenario_1fase[l][c] == 'x':
    #                 isLeft = c == 0 or cenario_1fase[l][c-1] != 'x'
    #                 isRight = c == len(cenario_1fase[l])-1 or cenario_1fase[l][c+1] != 'x'
    #                 chao = Floor(groups, assets, (c)* FLOOR_WIDTH, (l+1)* FLOOR_WIDTH, isLeft, isRight)
    #                 all_sprites.add(chao)
    #                 all_floors.add(chao)
    #             if cenario_1fase[l][c] == 'a':
    #                 ativ = Atividade(assets, (c) * ATIV_WIDTH, (l+1)* ATIV_WIDTH)
    #                 all_sprites.add(ativ)
    #                 all_atividades.add(ativ)
    #                 total_ativ+=1
    #             if cenario_1fase[l][c] == 'c':
    #                 cafe = Cafe(assets, (c) * CAFE_WIDTH, (l+1)* CAFE_WIDTH)
    #                 all_sprites.add(cafe)
    #                 all_cafes.add(cafe)
    #             if cenario_1fase[l][c] == 'I':
    #                 aluno = Inimigo(assets, (c) * ALUNO_WIDTH, chao.rect.top + 1)
    #                 all_sprites.add(aluno)
    #                 all_cafes.add(aluno)
    # elif fase==2:
    #     for l in range(len(cenario_2fase)):
    #         for c in range(len(cenario_2fase[l])):
    #             if cenario_2fase[l][c] == 'x':
    #                 isLeft = c == 0 or cenario_2fase[l][c-1] != 'x'
    #                 isRight = c == len(cenario_2fase[l])-1 or cenario_2fase[l][c+1] != 'x'
    #                 chao = Floor(groups, assets, (c)* FLOOR_WIDTH, (l+1)* FLOOR_WIDTH, isLeft, isRight)
    #                 all_sprites.add(chao)
    #                 all_floors.add(chao)
    #             if cenario_2fase[l][c] == 'a':
    #                 ativ = Atividade(assets, (c) * ATIV_WIDTH, (l+1)* ATIV_WIDTH)
    #                 all_sprites.add(ativ)
    #                 all_atividades.add(ativ)
    #                 total_ativ+=1
    #             if cenario_2fase[l][c] == 'c':
    #                 cafe = Cafe(assets, (c) * CAFE_WIDTH, (l+1)* CAFE_WIDTH)
    #                 all_sprites.add(cafe)
    #                 all_cafes.add(cafe)
    #             if cenario_2fase[l][c] == 'I':
    #                 aluno = Inimigo(assets, (c) * ALUNO_WIDTH, chao.rect.top + 1)
    #                 all_sprites.add(aluno)
    #                 all_cafes.add(aluno)
    # elif fase==3:
    #     for l in range(len(cenario_3fase)):
    #         for c in range(len(cenario_3fase[l])):
    #             if cenario_3fase[l][c] == 'x':
    #                 isLeft = c == 0 or cenario_3fase[l][c-1] != 'x'
    #                 isRight = c == len(cenario_3fase[l])-1 or cenario_3fase[l][c+1] != 'x'
    #                 chao = Floor(groups, assets, (c)* FLOOR_WIDTH, (l+1)* FLOOR_WIDTH, isLeft, isRight)
    #                 all_sprites.add(chao)
    #                 all_floors.add(chao)
    #             if cenario_3fase[l][c] == 'a':
    #                 ativ = Atividade(assets, (c) * ATIV_WIDTH, (l+1)* ATIV_WIDTH)
    #                 all_sprites.add(ativ)
    #                 all_atividades.add(ativ)
    #                 total_ativ+=1
    #             if cenario_3fase[l][c] == 'c':
    #                 cafe = Cafe(assets, (c) * CAFE_WIDTH, (l+1)* CAFE_WIDTH)
    #                 all_sprites.add(cafe)
    #                 all_cafes.add(cafe)
    #             if cenario_3fase[l][c] == 'I':
    #                 aluno = Inimigo(assets, (c) * ALUNO_WIDTH, chao.rect.top + 1)
    #                 all_sprites.add(aluno)
    #                 all_cafes.add(aluno)


    cenario_1fase = [
        '                             ',
        '                             ',
        '                             ',
        '                             ',
        '                             ',
        '                             ',
        '                             ',
        '                           cx',
        '                         x   ',
        '     xxxa      x   a xxxa    ',
        'xxxx      xxxa  Ixxx         ',
        '                             ',
        '                             ',
        '                             ',
        '                             ',
        '                             ',
    ]

    for l in range(len(cenario_1fase)):
        for c in range(len(cenario_1fase[l])):
            if cenario_1fase[l][c] == 'x':
                isLeft = c == 0 or cenario_1fase[l][c-1] != 'x'
                isRight = c == len(cenario_1fase[l])-1 or cenario_1fase[l][c+1] != 'x'
                chao = Floor(groups, assets, (c)* FLOOR_WIDTH, (l+1)* FLOOR_WIDTH, isLeft, isRight)
                all_sprites.add(chao)
                all_floors.add(chao)
            if cenario_1fase[l][c] == 'a':
                ativ = Atividade(assets, (c) * ATIV_WIDTH, (l+1)* ATIV_WIDTH)
                all_sprites.add(ativ)
                all_atividades.add(ativ)
                total_ativ+=1
            if cenario_1fase[l][c] == 'c':
                cafe = Cafe(assets, (c) * CAFE_WIDTH, (l+1)* CAFE_WIDTH)
                all_sprites.add(cafe)
                all_cafes.add(cafe)
            if cenario_1fase[l][c] == 'I':
                aluno = Inimigo(assets, (c) * ALUNO_WIDTH, chao.rect.top + 1)
                all_sprites.add(cafe)
                all_cafes.add(cafe)

    #PRECISA DESCOMENTAR ESSE AQUI!!!!!!!!!!!        
    #aluno = Inimigo(assets, random.randint(ini+5, (n_blocos-1)*FLOOR_WIDTH+ini), chao.rect.top + 1)


    # for i in range(WIDTH):
    #     chao = Floor(groups, assets, ini + i * FLOOR_WIDTH, i == 0, i ==(WIDTH-1))
    #     all_sprites.add(chao)
    #     all_floors.add(chao)
    # for i in range(-HEIGHT):
    #     profundidade= Floor(groups, assets, -ini - i * FLOOR_HEIGHT, i == 0, i ==(-HEIGHT+1))
    #     all_sprites.add(profundidade)
    #     all_floors.add(profundidade)    
    #aluno = Inimigo(assets, random.randint(ini, (HEIGHT-1)*FLOOR_HEIGHT+ini), chao.rect.top + 1)
    #WIDTH = 1000
    #HEIGHT = 600
    ini=0
    # for i in range(WIDTH):
    #      chao = Floor(groups, assets, ini + i * FLOOR_WIDTH, 50 ,  i == 0, i ==(WIDTH-1))
    #      all_sprites.add(chao)
    #      all_floors.add(chao)    

    # --- Add plataforma ---
    width_plataform = 150
    # for i in range(width_plataform):
    #      chao= Floor(groups, assets, WIDTH + 15 + i * FLOOR_WIDTH,  150, i == 0, i ==(WIDTH-1))
    #      all_sprites.add(chao)
    #      all_floors.add(chao) 

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

    # pygame.mixer.music.play(loops=-1)
    #loop principal
    pygame.mixer.music.load('assets/sdx/Trilha_sonora.wav')
    pygame.mixer.music.play(-1)

    #assets["Trilha_sonora"].mixer.music.play()
    while state in [PLAYING]:
        
        #assets['Trilha_sonora'].set_volume(0.5)
        clock.tick(60)




        #COLOCAR O IF FASE AQUI????????
        # if fase==1:
        #     for l in range(len(cenario_1fase)):
        #         for c in range(len(cenario_1fase[l])):
        #             if cenario_1fase[l][c] == 'x':
        #                 isLeft = c == 0 or cenario_1fase[l][c-1] != 'x'
        #                 isRight = c == len(cenario_1fase[l])-1 or cenario_1fase[l][c+1] != 'x'
        #                 chao = Floor(groups, assets, (c)* FLOOR_WIDTH, (l+1)* FLOOR_WIDTH, isLeft, isRight)
        #                 all_sprites.add(chao)
        #                 all_floors.add(chao)
        #             if cenario_1fase[l][c] == 'a':
        #                 ativ = Atividade(assets, (c) * ATIV_WIDTH, (l+1)* ATIV_WIDTH)
        #                 all_sprites.add(ativ)
        #                 all_atividades.add(ativ)
        #                 total_ativ+=1
        #             if cenario_1fase[l][c] == 'c':
        #                 cafe = Cafe(assets, (c) * CAFE_WIDTH, (l+1)* CAFE_WIDTH)
        #                 all_sprites.add(cafe)
        #                 all_cafes.add(cafe)
        #             if cenario_1fase[l][c] == 'I':
        #                 aluno = Inimigo(assets, (c) * ALUNO_WIDTH, chao.rect.top + 1)
        #                 all_sprites.add(cafe)
        #                 all_cafes.add(cafe)
        # elif fase==2:
        #     for l in range(len(cenario_2fase)):
        #         for c in range(len(cenario_2fase[l])):
        #             if cenario_2fase[l][c] == 'x':
        #                 isLeft = c == 0 or cenario_2fase[l][c-1] != 'x'
        #                 isRight = c == len(cenario_2fase[l])-1 or cenario_2fase[l][c+1] != 'x'
        #                 chao = Floor(groups, assets, (c)* FLOOR_WIDTH, (l+1)* FLOOR_WIDTH, isLeft, isRight)
        #                 all_sprites.add(chao)
        #                 all_floors.add(chao)
        #             if cenario_2fase[l][c] == 'a':
        #                 ativ = Atividade(assets, (c) * ATIV_WIDTH, (l+1)* ATIV_WIDTH)
        #                 all_sprites.add(ativ)
        #                 all_atividades.add(ativ)
        #                 total_ativ+=1
        #             if cenario_2fase[l][c] == 'c':
        #                 cafe = Cafe(assets, (c) * CAFE_WIDTH, (l+1)* CAFE_WIDTH)
        #                 all_sprites.add(cafe)
        #                 all_cafes.add(cafe)
        #             if cenario_2fase[l][c] == 'I':
        #                 aluno = Inimigo(assets, (c) * ALUNO_WIDTH, chao.rect.top + 1)
        #                 all_sprites.add(cafe)
        #                 all_cafes.add(cafe)
        # elif fase==3:
        #     for l in range(len(cenario_3fase)):
        #         for c in range(len(cenario_3fase[l])):
        #             if cenario_3fase[l][c] == 'x':
        #                 isLeft = c == 0 or cenario_3fase[l][c-1] != 'x'
        #                 isRight = c == len(cenario_3fase[l])-1 or cenario_3fase[l][c+1] != 'x'
        #                 chao = Floor(groups, assets, (c)* FLOOR_WIDTH, (l+1)* FLOOR_WIDTH, isLeft, isRight)
        #                 all_sprites.add(chao)
        #                 all_floors.add(chao)
        #             if cenario_3fase[l][c] == 'a':
        #                 ativ = Atividade(assets, (c) * ATIV_WIDTH, (l+1)* ATIV_WIDTH)
        #                 all_sprites.add(ativ)
        #                 all_atividades.add(ativ)
        #                 total_ativ+=1
        #             if cenario_3fase[l][c] == 'c':
        #                 cafe = Cafe(assets, (c) * CAFE_WIDTH, (l+1)* CAFE_WIDTH)
        #                 all_sprites.add(cafe)
        #                 all_cafes.add(cafe)
        #             if cenario_3fase[l][c] == 'I':
        #                 aluno = Inimigo(assets, (c) * ALUNO_WIDTH, chao.rect.top + 1)
        #                 all_sprites.add(cafe)
        #                 all_cafes.add(cafe)



    
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                state = DONE
            if state == PLAYING:        
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
            

        all_sprites.update()

        if player.rect.bottom > HEIGHT +40:  #chao.rect.bottom:
            pygame.time.delay(TEMP_CAIR)
            state = VC_PERDEU

        #player.toca_chao = False
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
            pygame.time.delay(TEMP_MORRE)
            print('aquiiiiiii')
            assets["derrotado"].play()
            assets["derrotado"].set_volume(10)
            state = VC_PERDEU #tela vc perdeu
        
            #matando aluno
        if pygame.sprite.spritecollide(player,all_alunos,True):
            if pygame.sprite.spritecollide(player,all_alunos,True,pygame.sprite.collide_mask):
                aluno.kill()
                all_sprites.update() 
                all_alunos.update()           

    

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
            print('sooooommmmm')
            assets['coletando_exercicio'].play()
            assets['coletando_exercicio'].set_volume(1)
            #o maior valor é 1 hahaha
            ativ.kill()
            score+=1
        
        hits_cafe = pygame.sprite.spritecollide(player, all_cafes, True)
        if len(hits_cafe) > 0:
            #assets['coletando_exercicio'].play()
            cafe.kill()
            if score == total_ativ:
                fase+=1
                state = VC_PASSOU
            else:
                state = VC_PERDEU

        pygame.display.update()

        window.fill((255,255,255))
        #if fase == 1:
        window.blit(assets['background1'], (0, 0))
        # elif fase == 2:
        #     window.blit(assets['background2'], (0, 0))
        # elif fase == 3:
        #     window.blit(assets['background3'], (0, 0))



        # mapa.fill((0, 0, 0))  # Preenche com a cor branca
        # #camera 
        # poscamera = pygame.Rect(player.rect.centerx - WIDTH/2, player.rect.centery - HEIGHT/2,WIDTH,HEIGHT)
        # mapa.blit(assets['background1'], (poscamera[0]-100,poscamera[1] -100))
        all_sprites.draw(window)

        # pygame.Surface.blit(window, mapa, (0,0), poscamera)

        #print('score comeca aqui')
        text_surface = assets['score_font'].render("score: {:02d}".format(score), True, (255, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.topleft = (10, 10) #(WIDTH / 2,  10)
        window.blit(text_surface, text_rect)

#        window.blit(score_text, (400, 150))

        #mapa.blit(text_surface, text_rect)

    return state