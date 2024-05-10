import pygame
from config import *
from assets import *
from tela_inicial import *
from game_screen import *

pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Humberto Bros')

estado = 0
while estado != -1:
    if estado == 0:
        estado = init_screen(window)
    if estado == 1:
        estado = game_screen(window)
  
pygame.quit()       









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

    # def update(self):
    #     # Atualização da posição da nave
    #     self.rect.x += self.speedx

    #     # Mantem dentro da tela
    #     if self.rect.right > 600: #WIDTH:
    #         self.rect.right = 600 #WIDTH
    #     if self.rect.left < 0:
    #         self.rect.left = 0

# # ----- Inicia estruturas de dados
# game = True
# state=INIT
# # ----- Inicia assets
# def init_screen(screen):
#     font1 = pygame.font.SysFont(None, 60)
#     font2 = pygame.font.SysFont(None, 80)
#     font3 = pygame.font.SysFont(None, 40)
#     text1 = font1.render('Bem vindo!', True, (255, 0, 0))
#     text2 = font2.render('Humberto Bros', True, (255, 0, 0))
#     text3 = font3.render('Pressione enter para começar', True, (255, 0, 0))
#     backgroud_init = pygame.image.load('assets/img/Fachada-do-Insper-2.png').convert()
#     window.fill((255, 255, 255))  # Preenche com a cor branco
#     window.blit(backgroud_init, (0, -50))
#     window.blit(text1, (250, 120))
#     window.blit(text2, (170, 200))
#     window.blit(text3, (170, 320))
    
#     player = Humberto(assets['Humberto'])
#     all_sprites = pygame.sprite.Group()
#     all_sprites.add(player)
#     all_sprites.draw(window)
#     #Processa os eventos (mouse, teclado, botão, etc).
#     running = True
#     while running:
#         #Ajusta a velocidade do jogo.
#         #clock.tick(FPS)
#         #Processa os eventos (mouse, teclado, botão, etc).
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 #state = QUIT
#                 running = False

#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_KP_ENTER:
#                     #state = GAME
#                     fase='1'
#                     running = False
    

#     return screen
# tela_ini = init_screen(window)


# player = Humberto(assets['Humberto'])
# all_sprites = pygame.sprite.Group()
# all_sprites.add(player)
# all_sprites.draw(window)


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
# while game:
#     # ----- Trata eventos
#     for event in pygame.event.get():
#         # ----- Verifica consequências
#         if event.type == pygame.QUIT:
#             game = False


#     # ----- Atualiza estado do jogo
#     pygame.display.update()  # Mostra o novo frame para o jogador

# # ===== Finalização =====
# pygame.quit()'''  # Função do PyGame que finaliza os recursos utilizados