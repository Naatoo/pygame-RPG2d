import pygame

from src.game.items_to_display import tiles, player_icon
from src.game.display import Display
from src.game.move_actions import player_move


def game_loop():
    pygame.init()

    black = (0, 0, 0)
    white = (255, 255, 255)
    game_display = Display()
    pygame.display.set_caption('RPG')
    clock = pygame.time.Clock()

    crashed = False

    while not crashed:
        for event in pygame.event.get():
            result = player_move(event)

        crashed = result
        game_display.get_display_window().fill(white)
        tiles()
        player_icon()

        pygame.display.update()
        clock.tick(60)
