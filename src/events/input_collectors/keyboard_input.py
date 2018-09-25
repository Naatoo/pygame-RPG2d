from src.events.input_collectors.event_container import EventContainer


class KeyboardInput(EventContainer):

    def __init__(self):
        self.__keys = []

    def __repr__(self):
        fmt = 'Currently pressed keys: {}'
        return fmt.format(self.__keys)

    def __contains__(self, key: int):
        if key in self.__keys:
            return True
        else:
            return False

    def __len__(self):
        return len(self.__keys)

    def add_element(self, key: int):
        self.__keys.append(key)

    def remove_element(self, key: int):
        if key in self:
            self.__keys.remove(key)
        else:
            raise NameError('This key was never pressed')

    def clear(self):
        self.__keys.clear()

