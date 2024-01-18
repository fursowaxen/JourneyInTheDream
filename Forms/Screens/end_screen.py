import sys
import pygame
from Forms.CONSTANTS import FPS, WINDOW_WIDTH, WINDOW_HEIGHT
from Forms.services import load_image
from Forms.main_gameplay import playing, TIME


def end_screen(screen):
    screen.fill((0, 0, 0))
    pg = load_image("pictures/bcg_logo.png")
    # sb = load_image("pictures/start_btn.png")
    screen.blit(pg, (0, 0))
    font = pygame.font.Font(None, 50)
    txt1 = font.render(f'Вы прошли игру', 1, (50, 70, 0))
    txt2 = font.render(f'за {TIME} секунд.', 1, (50, 70, 0))

    txt_x1 = WINDOW_WIDTH // 2 - txt1.get_width() // 2
    txt_y1 = WINDOW_HEIGHT // 2 - txt1.get_height() // 2

    txt_x2 = WINDOW_WIDTH // 2 - txt2.get_width() // 2
    txt_y2 = WINDOW_HEIGHT // 2 - txt2.get_height() // 2 + 60

    # screen.blit(sb, (195, 350)
    # btn_x, btn_y = 195, 350
    screen.blit(txt1, (txt_x1, txt_y1))
    screen.blit(txt2, (txt_x2, txt_y2))

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            # elif event.type == pygame.MOUSEBUTTONDOWN:
                # mouse_x, mouse_y = pygame.mouse.get_pos()
                # if btn_x <= mouse_x <= btn_x + 300 and btn_y <= mouse_y <= btn_y + 129:
                #     print('начинаем')
                #     return playing('map1.tmx', screen)
        pygame.display.flip()
        clock.tick(FPS)