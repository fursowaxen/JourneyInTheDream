import pygame
from Forms.Screens.start_screen import start_screen
from Forms.CONSTANTS import WINDOW_SIZE


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Journey in The Dream")
    start_screen(screen)
