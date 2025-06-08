"""
main.py предназначен для кода всей игры
"""
from UI import *

pygame.init()


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
