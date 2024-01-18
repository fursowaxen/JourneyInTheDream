import pygame
from Forms.CONSTANTS import FREE_TILES, FPS
from Forms.Classes.Levels import *
from Forms.Classes.Hero import Hero
from Forms.Classes.Game import Game
from Forms.services import show_message, show_time
from Forms.Minigame.minigame import Minigame


def playing(filename, screen):
    try:
        pygame.mixer.music.load('data/kevin-macleod-8bit-dungeon-level.mp3')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.2)
    except Exception:
        pass
    # создаем карту лвла и героя
    if filename == 'map1.tmx':
        lvl = Level1(filename, FREE_TILES)
    elif filename == 'map2.tmx':
        lvl = Level2(filename, FREE_TILES)
    elif filename == 'map3.tmx':
        lvl = Level3(filename, FREE_TILES)
    else:
        lvl = FinalLevel(filename, FREE_TILES)

    if filename == 'map3.tmx':
        hero = Hero((3, 0))
    else:
        hero = Hero((0, 5))

    game = Game(lvl, hero)          # создаем класс для игры
    running = True          # начинаем игру
    clock = pygame.time.Clock()
    m = Minigame(int(filename[3]))
    first_phrase = True

    TIME = 0
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if game.minigame in (True, None) and event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                m.pos = pos

            else:
                if event.type == pygame.KEYUP:
                    if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT):
                        hero.staying = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        lvl.picked_up = True
                    if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT):
                        hero.staying = False

        game.update_hero()
        game.render(screen)
        if first_phrase and filename == 'map1.tmx' and TIME <= 3:
            show_message(screen, 'intro', False)

        if lvl.get_tile_id(hero.get_position()) in (144, 164):
            show_message(screen, lvl.filename, lvl.puzzle_solved)

        if lvl.filename == 'map1.tmx':
            if (int(hero.x), int(hero.y)) == (2, 0):
                game.get_object('gem', screen)
                game.minigame = True
                if game.minigame in (True, None):
                    m.play(m.pos, screen)
                    game.minigame = m.play(m.pos, screen)
                    lvl.puzzle_solved = not game.minigame

            if lvl.puzzle_solved:
                if 7 < hero.x < 9:
                    lvl.can_light = True
                else:
                    lvl.can_light = False
                if int(hero.x) == 9:
                    return playing('map2.tmx', screen)
                show_message(screen, lvl.filename, True, lvl.picked_up)

        if lvl.filename == 'map2.tmx':
            if (int(hero.x), int(hero.y)) == (9, 4):
                game.get_object('axe', screen)
                game.minigame = True
                if game.minigame in (True, None):
                    m.play(m.pos, screen)
                    game.minigame = m.play(m.pos, screen)
                    lvl.puzzle_solved = not game.minigame

            if lvl.puzzle_solved:
                if 7 < hero.y < 9:
                    lvl.can_remove = True
                if int(hero.y) == 9:
                    return playing('map3.tmx', screen)
                show_message(screen, lvl.filename, True, lvl.picked_up)

        if lvl.filename == 'map3.tmx':
            if (int(hero.x), int(hero.y)) == (0, 9):
                game.get_object('bush', screen)
                game.minigame = True
                if game.minigame in (True, None):
                    m.play(m.pos, screen)
                    game.minigame = m.play(m.pos, screen)
                    lvl.puzzle_solved = not game.minigame
            if lvl.puzzle_solved:
                if hero.x == 9:
                    return playing('map4.tmx', screen)
                show_message(screen, lvl.filename, True, lvl.picked_up)

        TIME += 1/FPS
        show_time(screen, TIME)
        pygame.display.flip()
        clock.tick(FPS)
