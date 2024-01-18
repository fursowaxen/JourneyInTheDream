import pygame
from Forms.CONSTANTS import FREE_TILES, FPS
from Forms.Classes.Levels import *
from Forms.Classes.Hero import Hero
from Forms.Classes.Game import Game
from Forms.services import show_message, show_time
from Forms.Minigame.minigame import Minigame
from Forms.Screens.end_screen import end_screen
from Forms.use_data import save_data


TIME = 0


def playing(filename, screen):
    global TIME
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
        hero = Hero((3, 0), False)
    elif filename == 'map1.tmx':
        hero = Hero((0, 5), True)
    else:
        hero = Hero((0, 5), False)

    game = Game(lvl, hero)          # создаем класс для игры
    running = True          # начинаем игру
    clock = pygame.time.Clock()
    m = Minigame(int(filename[3]))
    first_phrase = True

    hold_btn = 0
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if game.minigame in (True, None) and event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                m.pos = pos

            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and lvl.puzzle_solved:
                        lvl.picked_up = True
                    if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT):
                        hero.staying = False
                        hold_btn += 1
                if event.type == pygame.KEYUP:
                    if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT) and hold_btn != 0:
                        hold_btn -= 1
                    if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT) and hold_btn == 0:
                        hero.staying = True


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

        if lvl.filename == 'map4.tmx':
            if 3 < hero.x < 5 and 3 < hero.y < 5:
                game.minigame = True
                if game.minigame in (True, None):
                    m.play(m.pos, screen)
                    game.minigame = m.play(m.pos, screen)
                    lvl.puzzle_solved = not game.minigame
            if lvl.puzzle_solved:
                save_data(TIME)
                return end_screen(screen, TIME)
            show_message(screen, lvl.filename, True, lvl.picked_up)

        TIME += 1/FPS
        show_time(screen, TIME)
        pygame.display.flip()
        clock.tick(FPS)
