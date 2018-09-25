import pygame

from src.events.move_actions import move_by_mouse
from src.events.items_actions import move_item_on_the_ground

LEFT = 1
RIGHT = 3


def move_player_by_mouse(event: pygame.event):
    x, y = (coordinate // 32 for coordinate in event.dict['pos'])
    if event.button == LEFT:
        move_by_mouse(x=x, y=y)
    elif event.button == RIGHT:
        print("Right mouse  button is not implemented yet")
    else:
        print("This button is not implemented yet")


def move_item(event_button_pressed: pygame.event, event_button_released: pygame.event):
    initial_coordinates = tuple(coordinate // 32 for coordinate in event_button_pressed.dict['pos'])
    target_coordinates = tuple(coordinate // 32 for coordinate in event_button_released.dict['pos'])
    if initial_coordinates != target_coordinates:
        move_item_on_the_ground(initial_coordinates, target_coordinates)
    else:
        print('Initial coordinates: {} and target coordinates: {} are identical'.
              format(initial_coordinates, target_coordinates))
