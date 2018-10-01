import pygame

from src.events.input_collectors.keyboard_input import KeyboardInput
from src.events.input_collectors.mouse_input import MouseInput
from src.events.event_interpreter import EventInterpreter
from src.display.display_tool import DisplayTool


class EventHandler:

    def __init__(self):
        self.crashed = False
        self.keyboard_input = KeyboardInput()
        self.mouse_input = MouseInput()
        self.event_interpreter = EventInterpreter()
        self.display_tool = DisplayTool()

    def handle_event(self, event: pygame.event):
        self.update_input_containers(event)
        self.check_event(event)

    def update_input_containers(self, event: pygame.event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_input.add_element(button_id=event.button, position=event.dict['pos'])
        elif event.type == pygame.KEYDOWN:
            self.keyboard_input.add_element(key=event.key)
        elif event.type == pygame.QUIT:
            self.crashed = True
        else:
            pass

    def check_event(self, event: pygame.event):
        if event.type == pygame.MOUSEBUTTONUP:
            self.event_interpreter.check_call_mouse_button_up(keyboard_input=self.keyboard_input,
                                                              mouse_input=self.mouse_input,
                                                              button_id=event.button, position=event.dict['pos'])
            self.mouse_input.clear()

        elif event.type == pygame.KEYDOWN:
            self.event_interpreter.check_call_key_down(key=event.key)

        # elif event.type == pygame.KEYUP:
        #     self.event_interpreter.check_call_key_up(key=event.key)
        #     self.keyboard_input.remove_element(event.key)

        elif event.type == pygame.MOUSEMOTION:
            self.event_interpreter.check_call_mouse_motion(keyboard_input=self.keyboard_input,
                                                           mouse_input=self.mouse_input,
                                                           position=event.dict['pos'])
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.event_interpreter.check_call_mouse_button_down(keyboard_input=self.keyboard_input,
                                                                mouse_input=self.mouse_input,
                                                                button_id=event.button, position=event.dict['pos'])
        elif event.type == pygame.ACTIVEEVENT:
            pass
        else:
            pass
            # print("Unknown event")
        # TODO send camera position instead of click position
