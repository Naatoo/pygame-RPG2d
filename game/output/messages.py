from game.output.display_formatter import move_mes, items_mes


def forbidden_field_to_move(direction: str):
    cardinal_directions = dict(zip(("w", "s", "a", "d"), ("north", "south", "west", "east")))
    message = "You cannot go {}.".format(cardinal_directions[direction])
    print(move_mes(message))


def items_on_the_ground(items: dict):
    fmt = "You can see {} on the ground.".format(" ".join(['{},' for _ in items])[:-1])
    message = fmt.format(*('{} {}'.format(quantity, name) if quantity == 1
                           else '{} {}'.format(quantity, name + "s") for name, quantity in items.items()))
    print(items_mes(message))
