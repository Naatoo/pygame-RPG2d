from dbtools import DbTool
from game_objects import Character


class Actions:

    def __init__(self):
        self.player = DbTool().get_one_row(Character, Character.id, 1)

    def player_move(self, direction):
        fields_changer = {"n": -20, "s": 20, "w": -1, "e": 1}
        forbidden_range = self.get_forbidden_fields_check_map_borders(direction)
        if self.player.field_id + fields_changer[direction] not in forbidden_range:
            self.player.field_id += fields_changer[direction]

    @staticmethod
    def get_forbidden_fields_check_map_borders(direction):
        forbidden_fields = {"n": range(1, 21), "s": range(381, 401), "w": range(1, 382, 20), "e": range(20, 401, 20)}
        for possible_direction, forbidden_range in forbidden_fields.items():
            if direction == possible_direction:
                return forbidden_range
