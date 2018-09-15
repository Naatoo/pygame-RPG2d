import pygame

from src.tools.globals.singleton import Singleton


class Display(metaclass=Singleton):

    def __init__(self):
        width = 1024
        height = 768
        self.display_window = pygame.display.set_mode((width, height))

    def get_display_window(self):
        return self.display_window
