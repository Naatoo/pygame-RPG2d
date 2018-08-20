from database.dbtools import DbTool
from game.objects.db_objects import SpawnedCreature
import game.output.messages as messages


class Actions:

    def __init__(self):
        self.player = DbTool().get_one_row(SpawnedCreature, SpawnedCreature.id, 1)

    def player_move(self, direction):
        fields_changer = {"w": -20, "s": 20, "a": -1, "d": 1}
        forbidden_range = self.get_forbidden_fields_check_map_borders(direction)
        if self.player.field_id + fields_changer[direction] not in forbidden_range:
            self.player.field_id += fields_changer[direction]
        else:
            messages.forbidden_field_to_move(direction)

    @staticmethod
    def get_forbidden_fields_check_map_borders(direction):
        forbidden_fields = {"w": range(1, 21), "s": range(381, 401), "a": range(1, 382, 20), "d": range(20, 401, 20)}
        for possible_direction, forbidden_range in forbidden_fields.items():
            if direction == possible_direction:
                return forbidden_range
