import pygame

from src.database.db_tool import DbTool
from src.events.display_tool import DisplayTool


move_choices = {
    (0, -1): pygame.K_UP,
    (0, 1): pygame.K_DOWN,
    (-1, 0): pygame.K_LEFT,
    (1, 0): pygame.K_RIGHT
}


def move_by_keys(pressed_key: pygame.key):
    player = DbTool().get_player
    coordinates_initial = player.x, player.y,
    coordinates_change = 0, 0,
    for co, key in move_choices.items():
        if key == pressed_key:
            coordinates_change = co
    update_display(coordinates_initial, coordinates_change)


def move_by_mouse(position):
    x, y = (coordinate // 32 for coordinate in position)
    player = DbTool().get_player
    x_to_change = [(1, 0) if x - player.x > 0 else (-1, 0) for _ in range(abs(x - player.x))]
    y_to_change = [(0, 1) if y - player.y > 0 else (0, -1) for _ in range(abs(y - player.y))]
    for coordinates_change in (*x_to_change, *y_to_change):
        coordinates_initial = player.x, player.y,
        update_display(coordinates_initial, coordinates_change)


def update_display(coordinates_initial: tuple, coordinates_change: tuple):
    change_player_coordinates(coordinates_change)
    DisplayTool().update_one_tile(coordinates_initial)
    DisplayTool().display_creatures()
    DisplayTool().display_tiles_items()


def change_player_coordinates(coordinates_change: tuple):
    player = DbTool().get_player
    x, y = coordinates_change
    if player.x + x in range(20) and player.y + y in range(20):
        player.x += x
        player.y += y
    else:
        pass
