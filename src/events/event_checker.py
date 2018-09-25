import pygame

from src.events.mouse_events import move_player_by_mouse, move_item
from src.events.move_actions import move_by_keys
from src.events.items_actions import action_collect_item


class EventChecker:

    def __init__(self):
        self.crashed = False
        self.update = True
        self.mouse_clicked = None
        self.mouse_moved = None
        self.pressed_keys = []

    def check_event(self, event: pygame.event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.event_mouse_button_down(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            self.event_mouse_button_up(event)
        elif event.type == pygame.MOUSEMOTION:
            self.event_mouse_motion(event)
        elif event.type == pygame.KEYDOWN:
            self.event_key_pressed(event)
        elif event.type == pygame.KEYUP:
            self.event_key_released(event)
        elif event.type == pygame.QUIT:
            self.crashed = True
        else:
            print("Unknown event")

    def event_mouse_button_down(self, event):
        self.mouse_clicked = event

    def event_mouse_button_up(self, event):
        if self.mouse_moved is not None:
            move_item(self.mouse_clicked, event)
            self.mouse_moved = None
        elif pygame.K_LCTRL in self.pressed_keys:
            action_collect_item(event)
        else:
            move_player_by_mouse(self.mouse_clicked)
        self.update = True
        self.mouse_clicked = None

    def event_mouse_motion(self, event):
        if self.mouse_clicked:
            self.mouse_moved = True

    def event_key_pressed(self, event):
        self.pressed_keys.append(event.key)
        if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
            move_by_keys(event)
            self.update = True
        else:
            print("This key has no immediate action assigned.")

    def event_key_released(self, event):
        self.pressed_keys.remove(event.key)

# TODO mouse events in one data structure
# TODO specific keys, buttons checking in another module
# TODO item moving in real time
