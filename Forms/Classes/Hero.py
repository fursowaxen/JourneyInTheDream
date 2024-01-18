import pygame
from Forms.services import load_image
from Forms.CONSTANTS import TILE_SIZE, FPS


class Hero:
    def __init__(self, pos, stay):
        image = load_image('pictures/chars/down_S.png')
        self.x, self.y = pos
        self.gem = False
        self.axe = False
        self.potion = False
        self.image = image
        self.dir = 'down'
        self.count = 0
        self.staying = stay

    def get_position(self):
        return self.x, self.y

    def set_position(self, pos):
        self.x, self.y = pos

    def render(self, screen):
        # screen.blit(self.image, (self.x * TILE_SIZE, self.y * TILE_SIZE))
        clock = pygame.time.Clock()
        self.count = (self.count + clock.tick(FPS)) % 500
        if not self.staying:
            if self.count % 500 > 250:
                self.image = load_image(f'pictures/chars/{self.dir}_L.png')
            else:
                self.image = load_image(f'pictures/chars/{self.dir}_R.png')

            # if self.dir == "right":
            #     if self.count % 500 > 250:
            #         self.image = load_image('pictures/chars/right_L.png')
            #     else:
            #         self.image = load_image('pictures/chars/right_R.png')
            #
            # if self.dir == "up":
            #     if self.count % 500 > 250:
            #         self.image = load_image('pictures/chars/up_L.png')
            #     else:
            #         self.image = load_image('pictures/chars/up_R.png')
            #
            # if self.dir == "down":
            #     if self.count % 500 > 250:
            #         self.image = load_image('pictures/chars/down_L.png')
            #     else:
            #         self.image = load_image('pictures/chars/down_R.png')
        else:
            self.image = load_image(f'pictures/chars/{self.dir}_S.png')
        screen.blit(self.image, (self.x * TILE_SIZE, self.y * TILE_SIZE))