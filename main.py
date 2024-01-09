import os
import sys
import pygame
import pytmx


WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 700, 700
FPS = 15
MAPS_DIR = 'data/maps'
TILE_SIZE = 70
FREE_TILES = [40, 41, 42, 43, 44, 60, 61, 63, 83, 103, 123, 143, 163]
objects = {'map1.tmx': ('pictures/gem.png', (2 * TILE_SIZE, 0)),
           'map2.tmx': ('pictures/npc.png', (9 * TILE_SIZE, 4 * TILE_SIZE)),
           'map3.tmx': ('pictures/bush.png', (0, 9 * TILE_SIZE))}


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Journey in The Dream")


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
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


class Level:
    def __init__(self, filename, free_tiles):
        self.map = pytmx.load_pygame(f"{MAPS_DIR}/{filename}")
        self.filename = filename
        self.height = self.map.height
        self.width = self.map.width
        self.tile_size = self.map.tilewidth
        self.free_tiles = free_tiles

        self.puzzle_solved = False
        self.obj = objects[filename]

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                image = self.map.get_tile_image(x, y, 0)
                screen.blit(image, (x * self.tile_size, y * self.tile_size))
        if not self.puzzle_solved:
            g = Object(self.filename)
            g.render(screen)

    def get_tile_id(self, position):
        return self.map.tiledgidmap[self.map.get_tile_gid(*position, 0)]

    def is_free(self, position):
        return self.get_tile_id(position) in self.free_tiles


all_sprites = pygame.sprite.Group()


class Hero:
    def __init__(self, pos):
        self.x, self.y = pos
        self.gem = False
        self.axe = False
        self.potion = False
        self.image = load_image('pictures/mc.png')

    def get_position(self):
        return self.x, self.y

    def set_position(self, pos):
        self.x, self.y = pos

    def render(self, screen):
        screen.blit(self.image, (self.x * TILE_SIZE, self.y * TILE_SIZE))


class Object:
    def __init__(self, map_name):
        self.image_name = objects[map_name][0]
        self.x, self.y = objects[map_name][1]
        self.image = load_image(f'{self.image_name}')

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))


class Game:
    def __init__(self, level, hero):
        self.lvl = level
        self.hero = hero

    def render(self, screen):
        self.lvl.render(screen)
        self.hero.render(screen)

    def update_hero(self):
        next_x, next_y = self.hero.get_position()
        if pygame.key.get_pressed()[pygame.K_LEFT] and next_x - 0.5 >= 0:
            next_x -= 0.5
        if pygame.key.get_pressed()[pygame.K_RIGHT] and next_x + 0.5 <= 9:
            next_x += 0.5
        if pygame.key.get_pressed()[pygame.K_DOWN] and next_y + 0.5 <= 9:
            next_y += 0.5
        if pygame.key.get_pressed()[pygame.K_UP] and next_y - 0.5 >= 0:
            next_y -= 0.5
        if self.lvl.is_free((next_x, next_y)):
            self.hero.set_position((next_x, next_y))

    def get_object(self, obj):
        if obj == 'gem':
            self.hero.gem = True
            self.lvl.puzzle_solved = True
        if obj == 'axe':
            self.hero.axe = True
            self.lvl.puzzle_solved = True
        if obj == 'bush':
            self.hero.bush = True
            self.lvl.puzzle_solved = True


def terminate():
    pygame.quit()
    sys.exit()


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
                    return 1
        pygame.display.flip()
        clock.tick(FPS)


def main(filename):
    lvl = Level(filename, [41, 42, 43, 44, 45, 61, 62, 64, 84, 104, 124, 125, 105, 85, 144, 145, 164])
    hero = Hero((0, 5))
    if filename == 'map3.tmx':
        hero = Hero((3, 0))
    game = Game(lvl, hero)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        game.update_hero()
        game.render(screen)
        if lvl.get_tile_id(hero.get_position()) in (144, 164):
            show_message(screen, lvl.filename)
        if (int(hero.x), int(hero.y)) == (2, 0) and lvl.filename == 'map1.tmx':
            game.get_object('gem')
            return main('map2.tmx')
        if (int(hero.x), int(hero.y)) == (9, 4) and lvl.filename == 'map2.tmx':
            game.get_object('axe')
            return main('map3.tmx')
        if (int(hero.x), int(hero.y)) == (0, 9) and lvl.filename == 'map3.tmx':
            game.get_object('bush')
            show_error(screen)
        pygame.display.flip()
        clock.tick(FPS)


def show_message(screen, filename):
    if filename == 'map1.tmx':
        txt = 'нужно освещение'
    if filename == 'map2.tmx':
        txt = 'нужен топор'
    if filename == 'map3.tmx':
        txt = 'нужно зелье'
    if filename == 'end':
        txt = 'дальше битва с драконом... но она в разработке'
    font = pygame.font.Font(None, 50)
    text = font.render(txt, 1, (50, 70, 0))
    txt_x = WINDOW_WIDTH // 2 - text.get_width()//2
    txt_y = WINDOW_HEIGHT // 2 - text.get_height()//2
    txt_w = text.get_width()
    txt_h = text.get_height()
    pygame.draw.rect(screen, (200, 150, 50), (txt_x - 10, txt_y - 10, txt_w + 20, txt_h + 20))
    screen.blit(text, (txt_x, txt_y))


def show_error(screen):
    txt1 = 'дальше битва с драконом...'
    font = pygame.font.Font(None, 50)
    text = font.render(txt1, 1, (50, 70, 0))
    txt_x = WINDOW_WIDTH // 2 - text.get_width()//2
    txt_y = WINDOW_HEIGHT // 2 - text.get_height()//2
    txt_w = text.get_width()
    txt_h = text.get_height()
    pygame.draw.rect(screen, (200, 150, 50), (txt_x - 10, txt_y - 10, txt_w + 20, txt_h + 20))
    screen.blit(text, (txt_x, txt_y))
    txt1 = 'но она в разработке'
    font = pygame.font.Font(None, 50)
    text = font.render(txt1, 1, (50, 70, 0))
    txt_x = WINDOW_WIDTH // 2 - text.get_width()//2
    txt_y = WINDOW_HEIGHT // 2 - text.get_height()//2
    txt_w = text.get_width()
    txt_h = text.get_height()
    pygame.draw.rect(screen, (200, 150, 50), (txt_x - 10, txt_y + 60, txt_w + 20, txt_h + 20))
    screen.blit(text, (txt_x, txt_y + 60))
    txt1 = 'как и многое другое...'
    font = pygame.font.Font(None, 50)
    text = font.render(txt1, 1, (50, 70, 0))
    txt_x = WINDOW_WIDTH // 2 - text.get_width() // 2
    txt_y = WINDOW_HEIGHT // 2 - text.get_height() // 2
    txt_w = text.get_width()
    txt_h = text.get_height()
    pygame.draw.rect(screen, (200, 150, 50), (txt_x - 10, txt_y + 120, txt_w + 20, txt_h + 20))
    screen.blit(text, (txt_x, txt_y + 120))


if __name__ == '__main__':
    pygame.init()
    start_screen(screen)
    main('map1.tmx')
