import pygame

from src.events.display_tool import DisplayTool
from src.database.db_tool import DbTool
from src.events.mouse_events import check_mouse_button
from src.events.keys_events import check_key


class Game:

    def __init__(self):
        pygame.init()
        self.display_tool = DisplayTool()
        self.clock = pygame.time.Clock()
        self.crashed = False
        self.update = True
        self.fields_around = [coords for coords in DbTool().get_player.get_fields_around()]
        self.set_startup_config()
        self.display_on_startup()
        self.event_checker()

    @staticmethod
    def set_startup_config():
        pygame.display.set_caption('RPG')

    def display_on_startup(self):
        self.display_tool.startup_display()

    def event_checker(self):
        while not self.crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.crashed = True
                elif event.type == pygame.KEYDOWN:
                    check_key(event)
                    self.update = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    check_mouse_button(event)
                    self.update = True
                else:
                    pass
            if self.update:
                pygame.display.update()
                self.update = False
            self.clock.tick(60)
