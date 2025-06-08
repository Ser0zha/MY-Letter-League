import pygame
from pygame import Surface

ICON_PATH = "LetterLeagueIcon.png"


def display_creating() -> Surface:
    """
    display_creating - предназначен для корректного создания игрового окна
    :return:
    """
    width = 1600
    height = 900
    background_color = [246, 213, 172]

    sc = pygame.display.set_mode((width, height), pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.HWSURFACE)

    sc.fill(background_color)
    pygame.display.set_caption("Letter League")
    pygame.display.set_icon(pygame.image.load(ICON_PATH))
    pygame.display.update()

    return sc


def game_field_creating(sc: Surface) -> None:
    w = 27
    h = 19
    field_resolution_x = 50
    field_resolution_y = 50
    field_color = (254, 227, 197)

    for y in range(h):
        for x in range(w):
            pygame.draw.rect(sc,
                             field_color,
                             (x * 52 + field_resolution_x,
                              y * 52 + field_resolution_y,
                              field_resolution_x,
                              field_resolution_y
                              )
                             )
            pygame.display.update()
