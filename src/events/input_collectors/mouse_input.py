from src.events.input_collectors.event_container import EventContainer


class MouseInput(EventContainer):

    def __init__(self):
        self.__buttons = {
            "LMB": None,
            "RMB": None
        }

    def __repr__(self):
        fmt = "LMB clicked={}, RMB clicked={}"
        return fmt.format(True if 'LMB' in self else False, True if 'RMB' in self else False)

    def __contains__(self, button_name: str):
        return True if self.__buttons[button_name] is not None else False

    def __len__(self):
        return len([position for position in self.__buttons.values() if position is not None])

    def add_element(self, button_id: int, position: tuple):
        button_name = self.get_button_str(button_id)
        self.__buttons[button_name] = position

    def remove_element(self, button_name: str):
        self.__buttons[button_name] = None

    def clear(self):
        for button_name in self.__buttons.keys():
            self.__buttons[button_name] = None

    @staticmethod
    def get_button_str(button: int) -> str:
        return 'LMB' if button == 1 else 'RMB'

    @property
    def any_clicked(self) -> bool:
        return 'LMB' in self or 'RMB' in self

    def get_position(self, button_name: str) -> tuple:
        return self.__buttons[button_name]
