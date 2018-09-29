import pygame
from src.database.db_tool import DbTool
from src.tools.globals.constants import pixels_changer
from src.events.tools.display import Display

move_choices = {
    (0, -1): pygame.K_UP,
    (0, 1): pygame.K_DOWN,
    (-1, 0): pygame.K_LEFT,
    (1, 0): pygame.K_RIGHT
}


class ActionInvoker:

    def __init__(self):
        self.player = DbTool().get_player

    @staticmethod
    def change_player_coordinates(coordinates_change: tuple):
        player = DbTool().get_player
        x, y = coordinates_change
        player.x += x
        player.y += y
        Display().refresh()

    def move_by_keys(self, key: pygame.key):
        coordinates_change = 0, 0,
        for co, bounded_key in move_choices.items():
            if bounded_key == key:
                coordinates_change = co
        self.change_player_coordinates(coordinates_change)

    def move_by_mouse(self, button_id, position):
        x, y = (coordinate // pixels_changer for coordinate in position)
        x_to_change = [(1, 0) if x - 7 > 0 else (-1, 0) for _ in range(abs(x - 7))]
        y_to_change = [(0, 1) if y - 7 > 0 else (0, -1) for _ in range(abs(y - 7))]
        for coordinates_change in (*x_to_change, *y_to_change):
            self.change_player_coordinates(coordinates_change)

    def collect_item(self, button_id, position: tuple):
        player = DbTool().get_player

        item = DbTool().get_element_in_coordinates(('src.objects.items', 'BoundedItem'),
                                                   player.x - 7 + position[0] // 64,
                                                   player.y - 7 + position[1] // 64)
        clicked_coordinates = tuple(coordinate // pixels_changer for coordinate in position)
        if clicked_coordinates in (coordinates for coordinates in
                                   DbTool().get_player.get_fields_around_and_self()):
            columns_to_update = {
                'x': None,
                'y': None,
                'container_id': self.player.equipment.id_bounded_item,
                'container_slot_id': self.player.free_eq_slots[0]
            }
            DbTool().update_row(('src.objects.items', 'BoundedItem', 'id_bounded_item'), item.id_bounded_item,
                                columns_to_update)
        else:
            print("Player is too far away")
