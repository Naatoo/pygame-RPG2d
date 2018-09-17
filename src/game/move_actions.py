import pygame

from src.database.db_tool import DbTool


def player_move(event):
    player = DbTool().get_player

    if event.type == pygame.KEYDOWN:
        x_change = 0
        y_change = 0
        if event.key == pygame.K_LEFT:
            x_change = -1
        elif event.key == pygame.K_RIGHT:
            x_change = 1
        elif event.key == pygame.K_UP:
            y_change = -1
        elif event.key == pygame.K_DOWN:
            y_change = 1
        if player.x + x_change in range(20) and player.y + y_change in range(20):
            player.x += x_change
            player.y += y_change
        return True

    print(event)
