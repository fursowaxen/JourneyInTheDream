import os
import sys
import pygame
from Forms.CONSTANTS import WINDOW_WIDTH, WINDOW_HEIGHT


def show_message(screen, filename, can_go, end=False):
    if not end:
        if not can_go:
            if filename == 'map1.tmx':
                txt = 'нужно освещение'
            if filename == 'map2.tmx':
                txt = 'нужен топор'
            if filename == 'map3.tmx':
                txt = 'нужно зелье  против дракона'
            if filename == 'map4.tmx':
                txt = 'ааааа'
        else:
            if filename == 'map1.tmx':
                txt = 'этот камень так ярко светится!'
            if filename == 'map2.tmx':
                txt = 'держи топор. пока'
            if filename == 'map3.tmx':
                txt = 'из этих ягод можно сделать зелье'
            if filename == 'map4.tmx':
                txt = 'ааааа'
        if filename == 'intro':
            txt = 'нужно уходить отсюда!'
        if filename == 'too_long':
            txt = 'не будем задерживаться!'

        font = pygame.font.Font(None, 50)
        text = font.render(txt, 1, (50, 70, 0))
        txt_w = text.get_width()
        txt_h = text.get_height()
        txt_x = WINDOW_WIDTH // 2 - txt_w//2
        txt_y = WINDOW_HEIGHT // 2 - txt_h//2
        pygame.draw.rect(screen, (200, 150, 50), (txt_x - 10, txt_y - 10, txt_w + 20, txt_h + 20))
        screen.blit(text, (txt_x, txt_y))


def show_time(screen, time):
    font = pygame.font.Font(None, 23)
    txt = f'Вы играете: {str(int(time))} секунд'
    text = font.render(txt, 1, (50, 70, 0))
    pygame.draw.rect(screen, (200, 150, 50), (0, 0, text.get_width(), 20))
    screen.blit(text, (0, 3))


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)

    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)

    else:
        image = image.convert_alpha()
    return image


def terminate():
    pygame.quit()
    sys.exit()