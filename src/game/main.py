import pygame

from src.game.items_to_display import display_tiles, display_creatures, display_eq_items, display_player_eq_tile,\
    display_tiles_items
from src.game.display import Display
from src.game.move_actions import player_move


def game_loop():
    pygame.init()

    game_display = Display()
    pygame.display.set_caption('RPG')
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    clock = pygame.time.Clock()

    crashed = False
    refresh = True

    display_player_eq_tile()
    display_eq_items()

    while not crashed:
        if refresh:
            display_tiles()
            display_creatures()
            display_tiles_items()
            refresh = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            else:
                refresh = player_move(event)

        pygame.display.update()
        clock.tick(60)
