import pygame
from Forms.CONSTANTS import FPS
from Forms.services import show_message


def get_images(n):
    ImageList = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    for i in range(1, 16):
        ImageList[i] = pygame.image.load(f"Forms/Minigame/images/{n}/i{i}.jpg")
    return ImageList


class Minigame:
    def __init__(self, num):
        self.num = num
        self.clock = pygame.time.Clock()
        self.count = 0
        self.win = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
        self.lst = ['', [1, 2, 3, 4, 5, 6, 7, 8, 15, 14, 0, 11, 9, 13, 10, 12],
               [1, 2, 3, 4, 5, 6, 12, 7, 9, 14, 10, 15, 13, 0, 8, 11],
               [1, 2, 3, 4, 10, 9, 8, 12, 5, 0, 11, 6, 13, 7, 14, 15],
               [3, 15, 4, 11, 7, 8, 14, 1, 9, 6, 2, 5, 10, 12, 13, 0]]
        self.pix = get_images(self.num)
        self.deck = self.lst[num]
        self.pos = (0, 0)

    def render(self, screen):
        x = 150
        y = 150
        for i in range(16):
            if self.deck[i] > 0:
                screen.blit(self.pix[self.deck[i]], (x, y))

            x = x + 100
            if i == 3 or i == 7 or i == 11:
                x = 150
                y = y + 100

    def possible_moves(self, new_game):
        moves = []
        ind = new_game.index(0)
        if ind == 0:
            moves.append(new_game[1])
            moves.append(new_game[4])
        elif ind == 1:
            moves.append(new_game[0])
            moves.append(new_game[2])
            moves.append(new_game[5])
        elif ind == 2:
            moves.append(new_game[1])
            moves.append(new_game[3])
            moves.append(new_game[6])
        elif ind == 3:
            moves.append(new_game[2])
            moves.append(new_game[7])
        elif ind == 4:
            moves.append(new_game[0])
            moves.append(new_game[5])
            moves.append(new_game[8])
        elif ind == 5:
            moves.append(new_game[1])
            moves.append(new_game[4])
            moves.append(new_game[6])
            moves.append(new_game[9])
        elif ind == 6:
            moves.append(new_game[2])
            moves.append(new_game[5])
            moves.append(new_game[7])
            moves.append(new_game[10])
        elif ind == 7:
            moves.append(new_game[3])
            moves.append(new_game[6])
            moves.append(new_game[11])
        elif ind == 8:
            moves.append(new_game[4])
            moves.append(new_game[9])
            moves.append(new_game[12])
        elif ind == 9:
            moves.append(new_game[5])
            moves.append(new_game[8])
            moves.append(new_game[10])
            moves.append(new_game[13])
        elif ind == 10:
            moves.append(new_game[6])
            moves.append(new_game[9])
            moves.append(new_game[11])
            moves.append(new_game[14])
        elif ind == 11:
            moves.append(new_game[7])
            moves.append(new_game[10])
            moves.append(new_game[15])
        elif ind == 12:
            moves.append(new_game[8])
            moves.append(new_game[13])
        elif ind == 13:
            moves.append(new_game[9])
            moves.append(new_game[12])
            moves.append(new_game[14])
        elif ind == 14:
            moves.append(new_game[10])
            moves.append(new_game[13])
            moves.append(new_game[15])
        else:
            moves.append(new_game[11])
            moves.append(new_game[14])

        return moves

    def play(self, pos, screen):
        moves = self.possible_moves(self.deck)
        if 150 <= pos[0] <= 550 and 150 <= pos[1] <= 550:
            xod = int((pos[0] - 150) / 100) + (int((pos[1] - 150) / 100)) * 4
            if xod < len(self.deck):
                if self.deck[xod] in moves:
                    nul = self.deck.index(0)
                    self.deck[nul] = self.deck[xod]
                    self.deck[xod] = 0

            if self.deck == self.win:
                return False

        self.clock.tick(FPS)
        self.count += 1
        if self.count // FPS >= 60:
            show_message(screen, 'too_long', False)
            return False

        self.render(screen)

    size = width, height = 700, 700




