import pygame

from src.events.display_tool import DisplayTool
from src.events.event_checker import EventChecker


class Game:

    def __init__(self):
        pygame.init()
        self.display_tool = DisplayTool()
        self.event_checker = EventChecker()
        self.set_startup_config()
        self.event_loop()

    def set_startup_config(self):
        pygame.display.set_caption('RPG')
        self.display_tool.startup_display()

    def event_loop(self):
        clock = pygame.time.Clock()
        while not self.event_checker.crashed:
            events = pygame.event.get()
            for event in events:
                self.event_checker.handle_event(event)
            clock.tick(60)
