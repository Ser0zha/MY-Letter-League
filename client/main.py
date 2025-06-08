"""
main.py предназначен для кода всей игры
"""
import pygame
from pygame import Surface
from pygame.locals import *

from Enums.Enums import BACKGROUND_COLOR
from UI import display_creating, game_field_creating

pygame.init()

# CONSTANT
FPS = 60

# GLOBAL
SURFACE: Surface


def window_logic() -> None:
    """
    clock - константа для времени задержки 60 fps
    fl_running - индикатор для работы ГЛАВНОГО ЦИКЛЫ ОБРАБОТКИ СОБЫТИЯ
    :return:
    """
    global SURFACE

    clock = pygame.time.Clock()

    fl_running = True
    while fl_running:
        SURFACE.fill(BACKGROUND_COLOR)

        current_size = SURFACE.get_size()
        game_field_creating(SURFACE, *current_size)

        for event in pygame.event.get():
            if event.type == QUIT:
                fl_running = False
                pygame.quit()
            elif event.type == VIDEORESIZE:
                SURFACE = pygame.display.set_mode(event.size, RESIZABLE)

        pygame.display.flip()
        clock.tick(FPS)


def main_window() -> None:
    global SURFACE

    SURFACE = display_creating()

    window_logic()


def main() -> None:
    # надо добавить сюда, то есть в начало проверок на то, что всё ОК
    main_window()

    print("\nДобро пожаловать в Letter League!")


if __name__ == "__main__":
    main()
