import pygame
from Forms.Minigame.minigame import Minigame
from Forms.CONSTANTS import FREE_TILES


class Game:
    def __init__(self, level, hero):
        self.lvl = level
        self.hero = hero
        self.minigame = False

    def render(self, screen):
        self.lvl.render(screen)
        self.hero.render(screen)

    def update_hero(self):
        if self.minigame == False:
            next_x, next_y = self.hero.get_position()
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                self.hero.dir = 'left'
                if next_x - 0.1 >= 0:
                    if int(next_y) == next_y:

                        if self.lvl.get_tile_id((int(next_x), int(next_y))) in FREE_TILES:
                            next_x -= 0.1

                    else:
                        if self.lvl.get_tile_id((int(next_x), int(next_y))) in FREE_TILES and self.lvl.get_tile_id((int(next_x), int(next_y) + 1)) in FREE_TILES:
                            next_x -= 0.1

            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                self.hero.dir = 'right'

                if next_x + 0.1 <= 9:
                    if int(next_y) == next_y:

                        if self.lvl.get_tile_id((int(next_x) + 1, int(next_y))) in FREE_TILES:
                            next_x += 0.1
                    else:
                        if self.lvl.get_tile_id((int(next_x) + 1, int(next_y))) in FREE_TILES and self.lvl.get_tile_id((int(next_x) + 1, int(next_y) + 1)) in FREE_TILES:
                            next_x += 0.1

            if pygame.key.get_pressed()[pygame.K_DOWN]:
                self.hero.dir = 'down'
                if next_y + 0.1 <= 9:
                    if int(next_x) == next_x:

                        if self.lvl.get_tile_id((int(next_x), int(next_y) + 1)) in FREE_TILES:
                            next_y += 0.1
                    else:
                        if self.lvl.get_tile_id((int(next_x), int(next_y) + 1)) in FREE_TILES and self.lvl.get_tile_id((int(next_x) + 1, int(next_y) + 1)) in FREE_TILES:
                            next_y += 0.1

            if pygame.key.get_pressed()[pygame.K_UP]:
                self.hero.dir = 'up'
                if next_y - 0.1 >= 0:
                    if int(next_x) == next_x:
                        if self.lvl.get_tile_id((int(next_x), int(next_y))) in FREE_TILES:
                            next_y -= 0.1
                    else:
                        if self.lvl.get_tile_id((int(next_x), int(next_y))) in FREE_TILES and self.lvl.get_tile_id((int(next_x) + 1, int(next_y))) in FREE_TILES:
                            next_y -= 0.1

            next_x, next_y = round(next_x, 1), round(next_y, 1)
            condition1 = not self.lvl.puzzle_solved and self.lvl.filename == 'map1.tmx'
            condition2 = next_x in (8, 9)
            if condition1 and condition2:
                next_x -= 0.1
            if self.lvl.is_free((next_x, next_y)):
                self.hero.set_position((next_x, next_y))

    def get_object(self, obj, screen):
        if obj == 'gem':
            self.minigame = True
            self.hero.gem = True

        if obj == 'axe':
            self.minigame = True
            self.hero.axe = True

        if obj == 'bush':
            self.minigame = True
            self.hero.bush = True

