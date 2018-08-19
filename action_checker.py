from actions import Actions

possible_actions_registry = []


def action(func):
    if func.__name__[-1] not in [f.__name__[-1] for f in possible_actions_registry]:
        possible_actions_registry.append(func)
        return func
    else:
        raise ValueError("This letter is already in use")


class ActionChecker:

    def __init__(self):
        self.player_input = None
        self.action = Actions()

    def __call__(self, player_input):
        self.player_input = player_input
        for func in possible_actions_registry:
            if self.player_input == func.__name__[-1]:
                func(player_input)

    @staticmethod
    @action
    def move_north_n(player_input):
        Actions().player_move(player_input)

    @staticmethod
    @action
    def move_south_s(player_input):
        Actions().player_move(player_input)

    @staticmethod
    @action
    def move_west_w(player_input):
        Actions().player_move(player_input)

    @staticmethod
    @action
    def move_east_e(player_input):
        Actions().player_move(player_input)