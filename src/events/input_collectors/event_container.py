import abc


class EventContainer(abc.ABC):

    @abc.abstractmethod
    def __len__(self):
        """Return number of pressed keys/buttons"""

    @abc.abstractmethod
    def add_element(self, **kwargs):
        """Add input to input container"""

    @abc.abstractmethod
    def remove_element(self, **kwargs):
        """Remove input from input container"""

    @abc.abstractmethod
    def clear(self):
        """Clear input container"""
