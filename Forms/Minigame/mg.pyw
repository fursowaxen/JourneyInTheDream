import pygame
import sys


def minigame(num):
    clock = pygame.time.Clock()
    count = 0
    win = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
    lst = ['', [1, 2, 3, 4, 5, 6, 7, 8, 15, 14, 0, 11, 9, 13, 10, 12],
           [1, 2, 3, 4, 5, 6, 12, 7, 9, 14, 10, 15, 13, 0, 8, 11], [1, 2, 3, 4, 10, 9, 8, 12, 5, 0, 11, 6, 13, 7, 14, 15],
           [3, 15, 4, 11, 7, 8, 14, 1, 9, 6, 2, 12, 13, 5, 10]]

    #   предлагаю сделать переменную num, в которой будет записан номер уровня(1-4) и эту переменную
    #   вставить в 35 сроке и в 122

    def get_images(n):
        ImageList = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        for i in range(1, 16):
            ImageList[i] = pygame.image.load(f".\\images\\{n}\\i{i}.jpg")
        # ImageList[2] = pygame.image.load(f".\images\\{n}\i2.jpg")
        # ImageList[3] = pygame.image.load(f".\images\\{n}\i3.jpg")
        # ImageList[4] = pygame.image.load(f".\images\\{n}\i4.jpg")
        # ImageList[5] = pygame.image.load(f".\images\\{n}\i5.jpg")
        # ImageList[6] = pygame.image.load(f".\images\\{n}\i6.jpg")
        # ImageList[7] = pygame.image.load(f".\images\\{n}\i7.jpg")
        # ImageList[8] = pygame.image.load(f".\images\\{n}\i8.jpg")
        # ImageList[9] = pygame.image.load(f".\images\\{n}\i9.jpg")
        # ImageList[10] = pygame.image.load(f".\images\\{n}\i10.jpg")
        # ImageList[11] = pygame.image.load(f".\images\\{n}\i11.jpg")
        # ImageList[12] = pygame.image.load(f".\images\\{n}\i12.jpg")
        # ImageList[13] = pygame.image.load(f".\images\\{n}\i13.jpg")
        # ImageList[14] = pygame.image.load(f".\images\\{n}\i14.jpg")
        # ImageList[15] = pygame.image.load(f".\images\\{n}\i15.jpg")
        return ImageList


    pix = get_images(2)  # в этой строчке изменяется папка с картинками


    def print_blocks():
        x = 0
        y = 0
        for i in range(16):
            if deck[i] > 0:
                screen.blit(pix[deck[i]], (x, y))

            x = x + 100
            if i == 3 or i == 7 or i == 11:
                x = 0
                y = y + 100


    def possible_moves(new_game):
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


    deck = lst[2]
    size = width, height = 399, 399
    screen = pygame.display.set_mode(size)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            movies = possible_moves(deck)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                xod = int(pos[0] / 100) + (int(pos[1] / 100)) * 4
                if deck[xod] in movies:
                    nul = deck.index(0)
                    deck[nul] = deck[xod]
                    deck[xod] = 0

                if deck == win:
                    print(1)
                    sys.exit()
        clock.tick(60)
        count += 1
        screen.fill((0, 0, 0))
        print_blocks()
        pygame.display.flip()
        if count / 60 >= 180:
            print(2)
            break
