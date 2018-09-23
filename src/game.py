import pygame

from src.events.display_tool import DisplayTool
from src.events.mouse_events import check_mouse_button
from src.events.keys_events import check_key
from src.events.items_actions import check_if_coordinates_in_range


class Game:

    def __init__(self):
        pygame.init()
        self.display_tool = DisplayTool()
        self.clock = pygame.time.Clock()
        self.crashed = False
        self.update = True
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
                elif any(pygame.key.get_pressed()) and event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.key.get_pressed()[pygame.K_LCTRL] and event.button == 3:
                        check_if_coordinates_in_range(event)
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
