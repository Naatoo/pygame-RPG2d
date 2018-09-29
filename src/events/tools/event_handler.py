import pygame

from src.events.input_collectors.keyboard_input import KeyboardInput
from src.events.input_collectors.mouse_input import MouseInput
from src.events.tools.check_input import CheckInput
from src.events.tools.action_invoker import ActionInvoker
from src.events.tools.display import Display


class EventHandler:

    def __init__(self):
        self.crashed = False
        self.keyboard_input = KeyboardInput()
        self.mouse_input = MouseInput()
        self.input_checker = CheckInput(self.mouse_input, self.keyboard_input)
        self.action_invoker = ActionInvoker()
        self.display = Display()

    def handle_event(self, event: pygame.event):
        action = None
        event_data = None
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_input.add_element(button_id=event.button, position=event.dict['pos'])
        elif event.type == pygame.KEYDOWN:
            self.keyboard_input.add_element(key=event.key)
        elif event.type == pygame.QUIT:
            self.crashed = True
        else:
            pass

        self.input_checker.update_inputs(self.mouse_input, self.keyboard_input)
        if event.type == pygame.MOUSEBUTTONUP:
            event_data = dict(button_id=event.button, position=event.dict['pos'])
            action = self.input_checker.check_call_mouse_button_up(**event_data)
            self.mouse_input.clear()

        elif event.type == pygame.KEYDOWN:
            event_data = dict(key=event.key)
            action = self.input_checker.check_call_key_down(**event_data)

        elif event.type == pygame.KEYUP:
            self.input_checker.check_call_key_up(key=event.key)
            self.keyboard_input.remove_element(event.key)

        elif event.type == pygame.MOUSEMOTION:
            self.input_checker.check_call_mouse_motion(position=event.dict['pos'])

        elif event.type == pygame.ACTIVEEVENT:
            pass
        else:
            pass
            print("Unknown event")
        # TODO send camera position instead of click position
        if action is not None:
            fn = getattr(self.action_invoker, action)
            fn(**event_data)
