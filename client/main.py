"""
main.py предназначен для кода всей игры
"""
import pygame

pygame.init()


def display_creating() -> None:
    width = 1600
    height = 900

    pygame.display.set_mode((width, height))
    pygame.display.set_caption("Letter League")


def main_window() -> None:
    """
    fps - время кадра
    clock - константа для времени задержки 60 fps
    fl_running - индикатор для работы ГЛАВНОГО ЦИКЛЫ ОБРАБОТКИ СОБЫТИЯ
    :return:
    """
    display_creating()
    fps = 60
    clock = pygame.time.Clock()
    fl_running = True

    while fl_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                fl_running = False
        clock.tick(fps)


def main() -> None:
    # надо добавить сюда, то есть в начало проверок на то, что всё ОК
    main_window()
    print("Добро пожаловать в Letter League!")


if __name__ == "__main__":
    main()
