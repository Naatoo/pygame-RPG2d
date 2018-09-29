from src.events import keys
from src.events.tools.action_examiner import ActionExaminer


class CheckInput:

    def __init__(self, mouse_input, keyboard_input):
        self.mouse_input = mouse_input
        self.keyboard_input = keyboard_input
        self.action_examiner = ActionExaminer()

    def update_inputs(self, mouse_input, keyboard_input):
        self.mouse_input = mouse_input
        self.keyboard_input = keyboard_input

    def check_call_key_down(self, **kwargs):
        key = kwargs['key']
        action = None
        if key in keys.move:
            if self.action_examiner.check_move_by_key(key):
                action = 'move_by_keys'
            else:
                pass  # TODO impossible to move in this direction
        elif key == keys.left_ctrl:
            pass  # nothing happens - CTRL is key down is collected in keyboard container
        else:
            pass  # TODO other keys
        return action

    def check_call_mouse_button_up(self, button_id: int, position: tuple):
        button = 'LMB' if button_id == 1 else 'RMB'
        action = None
        if button == 'LMB':
            if self.action_examiner.check_move_by_mouse(position, self.mouse_input.get_position('LMB')):
                action = 'move_by_mouse'
            else:
                pass  # TODO handle many actions items etc.
        elif button == 'RMB':
            if len(self.keyboard_input) == 0:
                pass  # TODO popup window when only RMB is clicked
            elif keys.left_ctrl in self.keyboard_input:
                if self.action_examiner.check_collect_item(position):
                    action = 'collect_item'
            else:
                pass  # TODO other keys

        return action

    def check_call_mouse_motion(self, position: tuple):
        pass
        # if 'LMB' in self.mouse_input:
        #     pass  # TODO item moving in real time
        # elif 'RMB' in self.mouse_input:
        #     pass  # no actions yet
        # else:
        #     pass

    def check_call_key_up(self, key: int):
        pass
        # if len(self.mouse_input) == 0:
        #     if key in keys.move:
        #         move_by_keys(key)
        # else:
        #     pass
