from src.events import keys
from src.events.move_actions import move_by_keys, move_by_mouse
from src.events.items_actions import action_collect_item, move_item_on_the_ground


class ActionInvoker:

    def __init__(self, mouse_input, keyboard_input):
        self.mouse_input = mouse_input
        self.keyboard_input = keyboard_input

    def update_inputs(self, mouse_input, keyboard_input):
        self.mouse_input = mouse_input
        self.keyboard_input = keyboard_input

    def check_call_mouse_button_up(self, button_id: int, position: tuple):
        button = 'LMB' if button_id == 1 else 'RMB'
        if button == 'LMB':
            if self.mouse_input.get_position(button) == position:
                move_by_mouse(position)
            else:
                move_item_on_the_ground(self.mouse_input.get_position(button), position)
        elif button == 'RMB':
            if len(self.keyboard_input) == 0:
                pass
            elif keys.left_ctrl in self.keyboard_input:
                action_collect_item(position)
        else:
            print("This mouse button is not used")

    def check_call_mouse_motion(self, position: tuple):
        if 'LMB' in self.mouse_input:
            pass  # TODO item moving in real time
        elif 'RMB' in self.mouse_input:
            pass  # no actions yet
        else:
            pass

    def check_call_key_up(self, key: int):
        if len(self.mouse_input) == 0:
            if key in keys.move:
                move_by_keys(key)
        else:
            pass
