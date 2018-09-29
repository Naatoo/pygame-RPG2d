import pygame

from src.events.tools.event_handler import EventHandler


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('RPG')
        self.event_handler = EventHandler()
        self.event_loop()

    def event_loop(self):
        clock = pygame.time.Clock()
        while not self.event_handler.crashed:
            events = pygame.event.get()
            for event in events:
                self.event_handler.handle_event(event)
            clock.tick(60)
