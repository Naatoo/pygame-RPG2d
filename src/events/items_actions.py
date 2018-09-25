from src.database.db_tool import DbTool
from src.events.display_tool import DisplayTool


def items_in_player_range(fields_around):
    items = [DbTool().get_one_row_where_two_conditions(('src.objects.fields', 'Field', ('x', 'y')), fields).items
             for fields in fields_around]
    return items


def action_collect_item(position: tuple):
    clicked_coordinates = tuple(coordinate // 32 for coordinate in position)
    if clicked_coordinates in (coordinates for coordinates in DbTool().get_player.get_fields_around_and_self()):
        field = DbTool().get_one_row_where_two_conditions(
            ('src.objects.fields', 'Field', ('x', 'y')), clicked_coordinates)
        item = DbTool().get_one_row_where(('src.objects.items', 'BoundedItem', 'field_id'), field.id_field)
        check_if_item_in_coordinates(item)


def check_if_item_in_coordinates(item):
    if item is not None:
        add_item_from_field_to_player_eq(item)


def add_item_from_field_to_player_eq(item):
    coordinates = item.x, item.y
    player = DbTool().get_player
    columns_to_update = {
        'field_id': None,
        'container_id': player.equipment.id_bounded_item,
        'container_slot_id': player.free_eq_slots[0]
    }
    DbTool().update_row(('src.objects.items', 'BoundedItem', 'id_bounded_item'), item.id_bounded_item,
                        columns_to_update)
    DisplayTool().display_tiles_items(refresh=True)
    DisplayTool().display_eq_items(refresh=True)
    DisplayTool().update_one_tile(coordinates)


def move_item_on_the_ground(from_position: tuple, to_position: tuple):
    from_coordinates = tuple(coordinate // 32 for coordinate in from_position)
    to_coordinates = tuple(coordinate // 32 for coordinate in to_position)
    if from_coordinates in (coordinates for coordinates in DbTool().get_player.get_fields_around_and_self()):
        initial_field = DbTool().get_one_row_where_two_conditions(
            ('src.objects.fields', 'Field', ('x', 'y')), from_coordinates)
        target_field = DbTool().get_one_row_where_two_conditions(
            ('src.objects.fields', 'Field', ('x', 'y')), to_coordinates)
        columns_to_update = {'field_id': target_field.id_field}
        DbTool().update_row(('src.objects.items', 'BoundedItem', 'field_id'), initial_field.id_field,
                            columns_to_update)
        DisplayTool().display_tiles_items(refresh=True)
        DisplayTool().update_one_tile(from_coordinates)
    else:
        print("Item with coordinates: {} is out of player's range".format(from_coordinates))

# TODO out of screen handling
