import pygame

from src.events.move_actions import move_by_keys


key_choices = {
    'move': [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
}


def check_key(event: pygame.event):
    if event.key in key_choices['move']:
        move_by_keys(event)
