from Forms.CONSTANTS import OBJECTS, TILE_SIZE
from Forms.services import load_image


class Dragon:
    def __init__(self, map_name='map4.tmx'):
        self.image_name = OBJECTS[map_name][0]
        self.x, self.y = OBJECTS[map_name][1]
        self.image = load_image(f'{self.image_name}')

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))


class Object:
    def __init__(self, map_name):
        self.image_name = OBJECTS[map_name][0]
        self.x, self.y = OBJECTS[map_name][1]
        self.image = load_image(f'{self.image_name}')

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))


class Fog:
    def render(self, screen):
        for x in range(8, 10):
            for y in range(0, 10):
                if x == 8:
                    screen.blit(load_image('pictures/weak_fog.png'), (x * TILE_SIZE, y * TILE_SIZE))
                else:
                    screen.blit(load_image('pictures/strong_fog.png'), (x * TILE_SIZE, y * TILE_SIZE))