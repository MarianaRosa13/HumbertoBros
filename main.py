import pygame

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((600, 300))
pygame.display.set_caption('Humberto Bros')

font = pygame.font.SysFont(None, 60)
text1 = font.render('Bem vindo!', True, (255, 0, 0))
text2 = font.render('Humberto Bros', True, (255, 0, 0))

game = True
while game==True:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branco
    window.blit(text1, (180, 80))
    window.blit(text2, (150, 150))

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