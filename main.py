import pygame

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((600, 300))
pygame.display.set_caption('Humberto Bros')

INIT = 0
GAME = 1
QUIT = 2

state=INIT

def init_screen(screen):
    #background_ini = pygame.image.load(path.join(IMG_DIR, 'inicio.png')).convert()
    #background_ini_rect = background.get_rect()
    font1 = pygame.font.SysFont(None, 60)
    font2 = pygame.font.SysFont(None, 40)
    text1 = font1.render('Bem vindo!', True, (255, 0, 0))
    text2 = font1.render('Humberto Bros', True, (255, 0, 0))
    text3 = font2.render('Pressione enter para começar', True, (255, 0, 0))
    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branco
    window.blit(text1, (180, 80))
    window.blit(text2, (150, 150))
    window.blit(text3, (140, 230))


state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    #elif state == GAME:
        #state = game_screen(window)
    # else:
    #     state = QUIT

state = GAME
while state==GAME:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # # ----- Gera saídas
    # window.fill((255, 255, 255))  # Preenche com a cor branco
    # window.blit(text1, (180, 80))
    # window.blit(text2, (150, 150))
    # window.blit(text3, (150, 150))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
if pygame.KEYUP:
    pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

# # assets = {}
# # assets['background'] = pygame.image.load('referencia\\assets\\img\\starfield.png').convert()
# # assets['meteor_img'] = pygame.image.load('referencia\\assets\\img\\meteorBrown_med1.png').convert_alpha()
# # assets['meteor_img'] = pygame.transform.scale(assets['meteor_img'], (METEOR_WIDTH, METEOR_HEIGHT))
# # assets['ship_img'] = pygame.image.load('referencia\\assets\\img\\playerShip1_orange.png').convert_alpha()
# # assets['ship_img'] = pygame.transform.scale(assets['ship_img'], (SHIP_WIDTH, SHIP_HEIGHT))
# # assets['bullet_img'] = pygame.image.load('referencia\\assets\\img\\laserRed16.png').convert_alpha()