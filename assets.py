import pygame
from config import *

# inicia assets 
def load_assets():
    assets = {}
    assets['background1']=pygame.image.load('assets/img/Entrada-p2-Insper.jpeg').convert()
    assets['background2']=pygame.image.load('assets/img/sala.jpg').convert()
    assets['background3']=pygame.image.load('assets/img/refeitorio-insper31.jpg').convert()
    assets['humberto']=pygame.image.load('assets/img/SpriteHumberto.png').convert_alpha()
    assets['humberto'] = pygame.transform.scale(assets['humberto'], (HUMBERTO_WIDTH, HUMBERTO_HEIGHT))
    assets['floor'] = pygame.image.load('assets/img/floor.png').convert_alpha()
    assets['floor'] = pygame.transform.scale(assets['floor'], (FLOOR_WIDTH, FLOOR_HEIGHT))
    assets['atividade'] = pygame.image.load('assets/img/atividade.png').convert_alpha()
    assets['humb esq'] = pygame.image.load('assets/img/Humberto_esquerda.png').convert_alpha()
    assets['humb dir'] = pygame.image.load('assets/img/Humberto_direita.png').convert_alpha()
    return assets
