import pygame

from src.events.input_collectors.keyboard_input import KeyboardInput
from src.events.input_collectors.mouse_input import MouseInput
from src.events.action_invoker import ActionInvoker


class EventChecker:

    def __init__(self):
        self.crashed = False
        self.keyboard_input = KeyboardInput()
        self.mouse_input = MouseInput()
        self.action_invoker = ActionInvoker(self.mouse_input, self.keyboard_input)

    def handle_event(self, event: pygame.event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_input.add_element(button_id=event.button, position=event.dict['pos'])
        elif event.type == pygame.KEYDOWN:
            self.keyboard_input.add_element(key=event.key)
        elif event.type == pygame.QUIT:
            self.crashed = True
        else:
            self.action_invoker.update_inputs(self.mouse_input, self.keyboard_input)
            if event.type == pygame.MOUSEBUTTONUP:
                self.action_invoker.check_call_mouse_button_up(button_id=event.button, position=event.dict['pos'])
                self.mouse_input.clear()
            elif event.type == pygame.KEYUP:
                self.action_invoker.check_call_key_up(key=event.key)
                self.keyboard_input.remove_element(event.key)
            elif event.type == pygame.MOUSEMOTION:
                self.action_invoker.check_call_mouse_motion(position=event.dict['pos'])
            elif event.type == pygame.ACTIVEEVENT:
                pass
            else:
                print("Unknown event")
