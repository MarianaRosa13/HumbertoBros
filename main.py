import pygame

pygame.init()
pygame.mixer.init()

#tela principal
WIDTH = 1000
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Humberto Bros')


HUMBERTO_WIDTH= 400
HUMBERTO_HEIGHT=400
# inicia assets 
def load_assets():
    assets = {}
    assets['background']=pygame.image.load('assets/img/Entrada-p2-Insper.jpeg').convert()
    assets['humberto']=pygame.image.load('assets/img/SpriteHumberto.png').convert_alpha()
    assets['humberto'] = pygame.transform.scale(assets['humberto'], (HUMBERTO_WIDTH, HUMBERTO_HEIGHT))
    return assets
#estrutura de dados
class Humberto(pygame.sprite.Sprite):
    def __init__(self,groups, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['humberto']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.groups = groups
        self.assets = assets 
    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        
def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()
    #criando jogador
    all_sprites = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    player = Humberto(groups, assets)
    all_sprites.add(player)

    # Criando os meteoros
    

    DONE = 0
    PLAYING = 1
    EXPLODING = 2
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
                        player.shoot()
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_LEFT:
                            player.speedx += 8
                        if event.key == pygame.K_RIGHT:
                            player.speedx -= 8 

        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(assets['background'], (0, 0))
        all_sprites.draw(window)
        # Desenhando meteoros
        
        pygame.display.update()

game_screen(window)  
pygame.quit()       



























'''#import pygame
#import os

#pygame.init()
#pygame.mixer.init()

#window = pygame.display.set_mode((700, 500))
#pygame.display.set_caption('Humberto Bros')

#fase=''
#INIT = 0
#GAME = 1
#QUIT = 2

#state=INIT

#window2 = pygame.display.set_mode((1000, 650))
#might have to do pygame.display.quit() followed by pygame.display.init()
#background_1fase = pygame.image.load('assets\\img\\Entrada-p2-Insper.jpeg').convert()
#window.blit(background_1fase, (-200, -100))




#assets = {}
#assets['background'] = pygame.image.load('referencia\\assets\\img\\starfield.png').convert()
#assets['Humberto'] = pygame.image.load('assets\\img\\SpriteHumberto.png').convert_alpha()
# assets['meteor_img'] = pygame.transform.scale(assets['meteor_img'], (METEOR_WIDTH, METEOR_HEIGHT))
# assets['ship_img'] = pygame.image.load('referencia\\assets\\img\\playerShip1_orange.png').convert_alpha()
# assets['ship_img'] = pygame.transform.scale(assets['ship_img'], (SHIP_WIDTH, SHIP_HEIGHT))
# assets['bullet_img'] = pygame.image.load('referencia\\assets\\img\\laserRed16.png').convert_alpha()


#ISSO AQUI TA DANDO PROBLEMA PORQUE O TAMANHO DAS TELAS DE CADA FASE
#VAI SER DIFERENTE E NAO SEI COMO VAI FAZER COM A POSIÇÃO DO PERSONAGEM
#class Humberto(pygame.sprite.Sprite):
#    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
#        pygame.sprite.Sprite.__init__(self)

#        self.image = assets['Humberto']
#        self.rect = self.image.get_rect()
#        self.rect.centerx = 350 #WIDTH / 2
#        self.rect.bottom = 400 #HEIGHT - 10
#        self.speedx = 0

    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > 600: #WIDTH:
            self.rect.right = 600 #WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

# # ----- Inicia estruturas de dados
game = True
state=INIT
# ----- Inicia assets
def init_screen(screen):
    font1 = pygame.font.SysFont(None, 60)
    font2 = pygame.font.SysFont(None, 80)
    font3 = pygame.font.SysFont(None, 40)
    text1 = font1.render('Bem vindo!', True, (255, 0, 0))
    text2 = font2.render('Humberto Bros', True, (255, 0, 0))
    text3 = font3.render('Pressione enter para começar', True, (255, 0, 0))
    backgroud_init = pygame.image.load('assets/img/Fachada-do-Insper-2.png').convert()
    window.fill((255, 255, 255))  # Preenche com a cor branco
    window.blit(backgroud_init, (0, -50))
    window.blit(text1, (250, 120))
    window.blit(text2, (170, 200))
    window.blit(text3, (170, 320))
    
    player = Humberto(assets['Humberto'])
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    all_sprites.draw(window)
    #Processa os eventos (mouse, teclado, botão, etc).
    #running = True
    # while running:
    #     #Ajusta a velocidade do jogo.
    #     #clock.tick(FPS)
    #     #Processa os eventos (mouse, teclado, botão, etc).
    #     for event in pygame.event.get():
    #         # Verifica se foi fechado.
    #         if event.type == pygame.QUIT:
    #             state = QUIT
    #             running = False

    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_KP_ENTER:
    #                 state = GAME
    #                 fase='1'
    #                 running = False
    

    return screen
tela_ini = init_screen(window)


player = Humberto(assets['Humberto'])
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.draw(window)


# while state != QUIT:
#     if state == INIT:
#         state = init_screen(window)
#     elif state == GAME:
#         if fase=='1':
#             tela=funcao(window2)
#             #state = game_screen(window)
#         elif fase=='2':
#             tela=funcao(window3)
#         elif fase=='3':
#             tela=funcao(window4)
#     else:
#         state = QUIT

# ===== Loop principal =====
# state = GAME
# while state==GAME:
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False


    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()'''  # Função do PyGame que finaliza os recursos utilizados