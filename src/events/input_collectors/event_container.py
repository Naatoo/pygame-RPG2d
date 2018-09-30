import abc


class EventContainer(abc.ABC):

    @abc.abstractmethod
    def __len__(self):
        """Return number of pressed keys/buttons"""

    @abc.abstractmethod
    def __bool__(self):
        """Returns True if any button/key was pressed, otherwise return False"""

    @abc.abstractmethod
    def add_element(self, **kwargs):
        """Add input to input container"""

    @abc.abstractmethod
    def remove_element(self, **kwargs):
        """Remove input from input container"""

    @abc.abstractmethod
    def clear(self):
        """Clear input container"""
