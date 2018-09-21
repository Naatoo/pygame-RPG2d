import pygame

from src.items_to_display import display_tiles, display_creatures, display_eq_items, display_player_eq_tile,\
    display_tiles_items
from src.display import Display
from src.move_actions import player_move
from src.possibilities import items_in_player_range
from src.database.db_tool import DbTool
from src.keys import key_choices


class Game:

    def __init__(self):
        pygame.init()
        self.game_display = Display()
        self.clock = pygame.time.Clock()
        self.crashed = False
        self.fields_around = [coords for coords in DbTool().get_player.get_fields_around()]

        self.set_startup_config()
        self.display_on_startup()
        self.event_checker()

    @staticmethod
    def set_startup_config():
        pygame.display.set_caption('RPG')
        pygame.event.set_blocked(pygame.MOUSEMOTION)

    def display_on_startup(self):
        self.display()

    def event_checker(self):
        while not self.crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.crashed = True
                elif event.type == pygame.KEYDOWN and event.key in key_choices['move']:
                    self.move_player(event)
                    self.check_after_move()
                else:
                    pass
            pygame.display.update()
            self.clock.tick(60)

    @staticmethod
    def move_player(event):
        player_move(event)

    def check_after_move(self):
        self.fields_around = [coords for coords in DbTool().get_player.get_fields_around()]
        self.display()

    @staticmethod
    def display():
        display_tiles()
        display_creatures()
        display_tiles_items()
        display_player_eq_tile()
        display_eq_items()
