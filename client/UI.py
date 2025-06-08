import pygame
from pygame import Surface
from pygame.locals import *

from Enums.Enums import BACKGROUND_COLOR

ICON_PATH = "LetterLeagueIcon.png"
FIELD_COLOR = (254, 227, 197)


def display_creating() -> Surface:
    """
    display_creating - предназначен для корректного создания игрового окна
    :return:
    """
    width = 1600
    height = 900

    sc = pygame.display.set_mode((width, height), RESIZABLE | DOUBLEBUF | HWSURFACE)

    sc.fill(BACKGROUND_COLOR)
    pygame.display.set_caption("Letter League")
    pygame.display.set_icon(pygame.image.load(ICON_PATH))
    pygame.display.update()

    return sc


def game_field_creating(sc: Surface, width=30, height=30) -> None:
    grid_w = 27
    grid_h = 19
    field_resolution_x = width // grid_w
    field_resolution_y = height // grid_h

    # for y in range(grid_h):
    #     for x in range(grid_w):
    #         pygame.draw.rect(sc,
    #                          FIELD_COLOR,
    #                          (x * field_resolution_x,
    #                           y * field_resolution_y,
    #                           field_resolution_x - 2,
    #                           field_resolution_y - 2
    #                           )
    #                          )
    #         pygame.display.update()

    for y in range(grid_h):
        for x in range(grid_w):
            rect = pygame.Rect(
                x * field_resolution_x,
                y * field_resolution_y,
                field_resolution_x - 2,
                field_resolution_y - 2
            )
            pygame.draw.rect(sc, FIELD_COLOR, rect)
