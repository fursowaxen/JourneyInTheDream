import sys
import pygame
from Forms.CONSTANTS import FPS
from Forms.services import load_image
from Forms.main_gameplay import playing


def start_screen(screen):
    screen.fill((0, 0, 0))
    pg = load_image("pictures/bcg_logo.png")
    sb = load_image("pictures/start_btn.png")
    screen.blit(pg, (0, 0))
    screen.blit(sb, (195, 350))
    btn_x, btn_y = 195, 350
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if btn_x <= mouse_x <= btn_x + 300 and btn_y <= mouse_y <= btn_y + 129:
                    print('начинаем')
                    return playing('map1.tmx', screen)
        pygame.display.flip()
        clock.tick(FPS)