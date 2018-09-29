from src.database.db_tool import DbTool


class ActionExaminer:

    def __init__(self):
        self.x = 0
        self.y = 0

    def update_coordinates(self, position: tuple):
        self.x, self.y = position

    def check_move_by_mouse(self, position: tuple, lmb_click_down_position: tuple):
        if position == lmb_click_down_position:  # TODO and when field is accessible
            return True
        else:
            return False

    def check_move_by_key(self, key):
        if True:  # TODO check if field is accessible
            return True
        else:
            return None

    def check_collect_item(self, position: tuple):
        if self.item_in_field(position) is not None:
            return True
        else:
            return False

    @staticmethod
    def item_in_field(position):
        player = DbTool().get_player
        print(player.x - 7 + position[0] // 64)
        return DbTool().get_element_in_coordinates(('src.objects.items', 'BoundedItem'), player.x - 7 + position[0] // 64,
                                                   player.y - 7 + position[1] //64)

