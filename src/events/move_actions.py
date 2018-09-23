import pygame

from src.database.db_tool import DbTool
from src.events.items_to_display import display_creatures
from src.events.items_to_display import update_tile


move_choices = {
    (0, -1): pygame.K_UP,
    (0, 1): pygame.K_DOWN,
    (-1, 0): pygame.K_LEFT,
    (1, 0): pygame.K_RIGHT
}


def move_by_keys(event: pygame.event):
    player = DbTool().get_player
    coordinates_initial = player.x, player.y,
    coordinates_change = 0, 0,
    for co, event_type in move_choices.items():
        if event_type == event.key:
            coordinates_change = co
    update_display(coordinates_initial, coordinates_change)


def move_by_mouse(x: int, y: int):
    player = DbTool().get_player
    x_to_change = [(1, 0) if x - player.x > 0 else (-1, 0) for _ in range(abs(x - player.x))]
    y_to_change = [(0, 1) if y - player.y > 0 else (0, -1) for _ in range(abs(y - player.y))]
    for coordinates_change in (*x_to_change, *y_to_change):
        coordinates_initial = player.x, player.y,
        update_display(coordinates_initial, coordinates_change)


def update_display(coordinates_initial: tuple, coordinates_change: tuple):
    change_player_coordinates(coordinates_change)
    update_tile(coordinates_initial)
    display_creatures()


def change_player_coordinates(coordinates_change: tuple):
    player = DbTool().get_player
    x, y = coordinates_change
    if player.x + x in range(20) and player.y + y in range(20):
        player.x += x
        player.y += y
    else:
        pass
