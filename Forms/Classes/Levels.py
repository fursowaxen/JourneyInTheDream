import pytmx
from Forms.CONSTANTS import OBJECTS, MAPS_DIR
from Forms.Classes.Objects import Object, Fog, Dragon
from Forms.services import load_image


class Level:
    def __init__(self, filename, free_tiles):
        self.map = pytmx.load_pygame(f"{MAPS_DIR}/{filename}")
        self.filename = filename
        self.height = self.map.height
        self.width = self.map.width
        self.tile_size = self.map.tilewidth
        self.free_tiles = free_tiles
        self.picked_up = False

        self.puzzle_solved = False
        self.obj = OBJECTS[filename]

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


class Level1(Level):
    def __init__(self, filename, free_tiles):
        super().__init__('map1.tmx', free_tiles)
        self.filename = 'map1.tmx'
        self.can_light = False

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                image = self.map.get_tile_image(x, y, 0)
                screen.blit(image, (x * self.tile_size, y * self.tile_size))
        if not self.puzzle_solved:
            g = Object(self.filename)
            g.render(screen)
        if not self.can_light:
            f = Fog()
            f.render(screen)


class Level2(Level):
    def __init__(self, filename, free_tiles):
        super().__init__('map2.tmx', free_tiles)
        self.filename = 'map2.tmx'
        self.can_remove = False

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                image = self.map.get_tile_image(x, y, 0)
                screen.blit(image, (x * self.tile_size, y * self.tile_size))
        if not self.puzzle_solved:
            g = Object(self.filename)
            g.render(screen)
        if not self.can_remove:
            screen.blit(load_image("pictures/branches.png"), (4 * self.tile_size, 9 * self.tile_size))


class Level3(Level):
    def __init__(self, filename, free_tiles):
        super().__init__('map3.tmx', free_tiles)
        self.filename = 'map3.tmx'
        self.can_go = False


class FinalLevel(Level):
    def __init__(self, filename, free_tiles):
        super().__init__('map4.tmx', free_tiles)
        self.filename = 'map4.tmx'

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                image = self.map.get_tile_image(x, y, 0)
                screen.blit(image, (x * self.tile_size, y * self.tile_size))
        if not self.puzzle_solved:
            dragon = Dragon()
            dragon.render(screen)


