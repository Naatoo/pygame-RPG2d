from src.database.db_tool import DbTool


def items_in_player_range(fields_around):
    items = [DbTool().get_one_row_where_two_conditions(('src.objects.fields', 'Field', ('x', 'y')), fields).items
             for fields in fields_around]
    return items
