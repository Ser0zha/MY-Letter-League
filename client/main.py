"""
main.py предназначен для кода всей игры
"""
import pygame
from pygame import Surface

pygame.init()


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


def display_creating() -> Surface:
    """
    display_creating - предназначен для корректного создания игрового окна
    :return:
    """
    width = 1600
    height = 900
    background_color = [246, 213, 172]
    path_icon = "iconLL.jpg"

    sc = pygame.display.set_mode((width, height), pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.HWSURFACE)

    sc.fill(background_color)
    pygame.display.set_caption("Letter League")
    pygame.display.set_icon(pygame.image.load(path_icon))
    pygame.display.update()

    return sc


def window_logic() -> None:
    """
    fps - время кадра
    clock - константа для времени задержки 60 fps
    fl_running - индикатор для работы ГЛАВНОГО ЦИКЛЫ ОБРАБОТКИ СОБЫТИЯ
    :return:
    """

    fps = 60
    clock = pygame.time.Clock()
    fl_running = True

    while fl_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                fl_running = False
        clock.tick(fps)


def main_window() -> None:
    surface = display_creating()
    game_field_creating(surface)

    window_logic()


def main() -> None:
    # надо добавить сюда, то есть в начало проверок на то, что всё ОК
    main_window()
    print("Добро пожаловать в Letter League!")


if __name__ == "__main__":
    main()
