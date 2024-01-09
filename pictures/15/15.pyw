import pygame, sys

pygame.init()

win = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]


def get_images():
    ImageList = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    ImageList[1] = pygame.image.load(".\images\i1.jpg")
    ImageList[2] = pygame.image.load(".\images\i2.jpg")
    ImageList[3] = pygame.image.load(".\images\i3.jpg")
    ImageList[4] = pygame.image.load(".\images\i4.jpg")
    ImageList[5] = pygame.image.load(".\images\i5.jpg")
    ImageList[6] = pygame.image.load(".\images\i6.jpg")
    ImageList[7] = pygame.image.load(".\images\i7.jpg")
    ImageList[8] = pygame.image.load(".\images\i8.jpg")
    ImageList[9] = pygame.image.load(".\images\i9.jpg")
    ImageList[10] = pygame.image.load(".\images\i10.jpg")
    ImageList[11] = pygame.image.load(".\images\i11.jpg")
    ImageList[12] = pygame.image.load(".\images\i12.jpg")
    ImageList[13] = pygame.image.load(".\images\i13.jpg")
    ImageList[14] = pygame.image.load(".\images\i14.jpg")
    ImageList[15] = pygame.image.load(".\images\i15.jpg")
    return ImageList


sp = get_images()


def print_blocks():
    x = 0
    y = 0
    for i in range(16):
        if deck[i] > 0:
            screen.blit(sp[deck[i]], (x, y))

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


deck = [0, 8, 3, 15, 1, 14, 11, 10, 7, 4, 13, 5, 12, 9, 2, 6]
black = 0, 0, 0
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
                sys.exit()

    screen.fill((0, 0, 0))
    print_blocks()
    pygame.display.flip()
