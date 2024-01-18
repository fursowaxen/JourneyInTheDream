import pygame


WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 700, 700
FPS = 30
MAPS_DIR = 'data/maps'
TILE_SIZE = 70
FREE_TILES = [24, 41, 42, 43, 44, 45, 61, 62, 64, 84, 104, 124, 125, 105, 85, 144, 145, 164]
ALL_SPRITES = pygame.sprite.Group()
OBJECTS = {'map1.tmx': ('pictures/gem.png', (2 * TILE_SIZE, 0)),
           'map2.tmx': ('pictures/chars/npc.png', (9 * TILE_SIZE, 4 * TILE_SIZE)),
           'map3.tmx': ('pictures/bush.png', (0, 9 * TILE_SIZE)),
           'map4.tmx': ('pictures/dragon.png', (4 * TILE_SIZE, 4 * TILE_SIZE))}



