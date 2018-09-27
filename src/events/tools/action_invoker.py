import pygame
from src.database.db_tool import DbTool
from src.events.tools.display import Display


move_choices = {
    (0, -1): pygame.K_UP,
    (0, 1): pygame.K_DOWN,
    (-1, 0): pygame.K_LEFT,
    (1, 0): pygame.K_RIGHT
}


class ActionInvoker:

    def __init__(self):
        self.pixel_changer = Display().pixels_changer
        self.player = DbTool().get_player

    @staticmethod
    def change_player_coordinates(coordinates_change: tuple):
        player = DbTool().get_player
        x, y = coordinates_change
        player.x += x
        player.y += y
        Display().reload_background()
        Display().reload_sprites()

    def move_by_keys(self, key: pygame.key):
        coordinates_change = 0, 0,
        for co, bounded_key in move_choices.items():
            if bounded_key == key:
                coordinates_change = co
        self.change_player_coordinates(coordinates_change)

    def move_by_mouse(self, button_id, position):
        x, y = (coordinate // self.pixel_changer for coordinate in position)
        x_to_change = [(1, 0) if x - self.player.x > 0 else (-1, 0) for _ in range(abs(x - self.player.x))]
        y_to_change = [(0, 1) if y - self.player.y > 0 else (0, -1) for _ in range(abs(y - self.player.y))]
        for coordinates_change in (*x_to_change, *y_to_change):
            self.change_player_coordinates(coordinates_change)

    def action_collect_item(self, position: tuple):
        item = DbTool().get_element_in_coordinates(('src.objects.items', 'BoundedItem'), *position)
        clicked_coordinates = tuple(coordinate // 32 for coordinate in position)
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
