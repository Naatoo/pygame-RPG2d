import pygame

from src.events.move_actions import move_by_mouse

LEFT = 1
RIGHT = 3


def check_mouse_button(event: pygame.event):
    x, y = (coordinate // 32 for coordinate in event.dict['pos'])
    if event.button == LEFT:
        move_by_mouse(x=x, y=y)
    elif event.button == RIGHT:
        print("Right mouse  button is not implemented yet")
    else:
        print("This button is not implemented yet")
