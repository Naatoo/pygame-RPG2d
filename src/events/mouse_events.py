import pygame

from src.events.items_actions import move_item_on_the_ground


def move_item(event_button_pressed: pygame.event, event_button_released: pygame.event):
    initial_coordinates = tuple(coordinate // 32 for coordinate in event_button_pressed.dict['pos'])
    target_coordinates = tuple(coordinate // 32 for coordinate in event_button_released.dict['pos'])
    if initial_coordinates != target_coordinates:
        move_item_on_the_ground(initial_coordinates, target_coordinates)
    else:
        print('Initial coordinates: {} and target coordinates: {} are identical'.
              format(initial_coordinates, target_coordinates))
