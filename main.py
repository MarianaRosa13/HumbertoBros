import pygame

pygame.init()

window = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Humberto Bros')


INIT = 0
GAME = 1
QUIT = 2

state=INIT

#background_1fase = pygame.image.load('C:\\Users\\mariv\\OneDrive\\Insper\\DesignSoft\\Pygame\\HumbertoBros\\assets\\img\\WhatsApp Image 2024-05-08 at 17.45.04').convert()
#background_1fase = pygame.image.load('Pygame\\HumbertoBros\\assets\\img\\WhatsApp Image 2024-05-08 at 17.45.04').convert()

# # ----- Inicia estruturas de dados
game = True
#state=INIT
# ----- Inicia assets
def init_screen(screen):
    font1 = pygame.font.SysFont(None, 60)
    font2 = pygame.font.SysFont(None, 40)
    text1 = font1.render('Bem vindo!', True, (255, 0, 0))
    text2 = font1.render('Humberto Bros', True, (255, 0, 0))
    text3 = font2.render('Pressione enter para começar', True, (255, 0, 0))
    backgroud_init = pygame.image.load('C:\\Users\\mariv\\OneDrive\\Insper\\DesignSoft\\Pygame\\HumbertoBros\\assets\\img\\Fachada-do-Insper-2.png').convert()
    window.fill((255, 255, 255))  # Preenche com a cor branco
    window.blit(backgroud_init, (0, 0))
    window.blit(text1, (180, 100))
    window.blit(text2, (150, 180))
    window.blit(text3, (100, 250))
#     # Processa os eventos (mouse, teclado, botão, etc).
# for event in pygame.event.get():
#         # Verifica se foi fechado.
#     if event.type == pygame.QUIT:
#         state = QUIT
#             #running = False
#     if event.type == pygame.KEYUP:
#         if event.key == pygame.K_KP_ENTER:
#             state = GAME
    return screen
tela_ini = init_screen(window)

# state = INIT
# while state != QUIT:
#     if state == INIT:
#         state = init_screen(window)
    #elif state == GAME:
        #state = game_screen(window)
    # else:
    #     state = QUIT

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
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados




# # assets = {}
# # assets['background'] = pygame.image.load('referencia\\assets\\img\\starfield.png').convert()
# # assets['meteor_img'] = pygame.image.load('referencia\\assets\\img\\meteorBrown_med1.png').convert_alpha()
# # assets['meteor_img'] = pygame.transform.scale(assets['meteor_img'], (METEOR_WIDTH, METEOR_HEIGHT))
# # assets['ship_img'] = pygame.image.load('referencia\\assets\\img\\playerShip1_orange.png').convert_alpha()
# # assets['ship_img'] = pygame.transform.scale(assets['ship_img'], (SHIP_WIDTH, SHIP_HEIGHT))
# # assets['bullet_img'] = pygame.image.load('referencia\\assets\\img\\laserRed16.png').convert_alpha()