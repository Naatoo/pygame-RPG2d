from business_logic import LogicException

from src.events import keys
import src.logic.logic as logic
from src.events.input_collectors.keyboard_input import KeyboardInput
from src.events.input_collectors.mouse_input import MouseInput
from src.database.db_tool import DbTool
from src.display.display_tool import DisplayTool


class EventInterpreter:

    def __init__(self):
        self.item_move = False

    def check_call_key_down(self, key):
        if key in keys.move:
            try:
                logic.move_by_keys(key)
            except LogicException as e:
                print(u"You cannot go there, because: {}".format(str(e)))
        elif key == keys.left_ctrl:
            pass  # nothing happens - CTRL is key down is collected in keyboard container
        else:
            pass  # TODO other keys

    def check_call_mouse_button_up(self, keyboard_input: KeyboardInput, mouse_input: MouseInput,
                                   button_id: int, position: tuple):
        button = 'LMB' if button_id == 1 else 'RMB'
        if button == 'LMB':
            if position == mouse_input.LMB_position:
                try:
                    logic.move_by_mouse(position)
                except LogicException as e:
                    print("You cannot got there, because {}".format(str(e)))
            elif self.item_move:
                try:
                    logic.drop_item(mouse_input.LMB_position, position)
                except LogicException as e:
                    print(u'You cannot drop this item here, because {}'.format(str(e)))
                finally:
                    self.item_move = False
                    DisplayTool().refresh()
        elif button == 'RMB':
            if keys.left_ctrl in keyboard_input and is_item_in_field(position):
                try:
                    logic.collect_item(position)
                except LogicException as e:
                    print(u"You cannot collect this item, because {}".format(str(e)))
            else:
                pass  # TODO other keys

    def check_call_mouse_button_down(self, keyboard_input: KeyboardInput, mouse_input: MouseInput,
                                     button_id: int, position: tuple):
        button = 'LMB' if button_id == 1 else 'RMB'
        if button == 'LMB':
            if is_item_in_field(position):
                try:
                    logic.drag_item(mouse_input, position)
                    self.item_move = True
                except LogicException as e:
                    print(u"You cannot drag this item, because {}".format(str(e)))
            else:
                pass
        elif button == 'RMB':
            pass

    def check_call_mouse_motion(self, keyboard_input: KeyboardInput, mouse_input: MouseInput,
                                position: tuple):
        if self.item_move:
            try:
                logic.display_move_dragged_item(position)
            except LogicException as e:
                print(u"You cannot move this item, because {}".format(str(e)))
        elif 'RMB' in mouse_input:
            pass  # no actions yet

    # def check_call_key_up(self, key: int):
    #     pass
        # if len(self.mouse_input) == 0:
        #     if key in keys.move:
        #         move_by_keys(key)
        # else:
        #     pass


def is_item_in_field(position):
    player = DbTool().get_player
    item = DbTool().get_element_in_coordinates(('src.objects.items', 'BoundedItem'), player.x - 7 + position[0] // 64,
                                               player.y - 7 + position[1] //64)
    return True if item else False
