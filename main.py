from game_objects import Field, Character, Equipment, Item, WorldMap
from map_creation import GenerateWeather, GenerateBiomes
from dbtools import DbTool


def insert_initial_data():
    for biome, weather in zip(list(GenerateBiomes()), GenerateWeather().data):
        dbtool.insert_row(Field(biome=biome, weather=weather))
    dbtool.insert_many_rows([Character(name="Player1", field_id=25),
                             Character(name="Player2", field_id=78),
                             Character(name="Player3", field_id=145)])
    dbtool.insert_many_rows([Equipment(capacity=250, character_id=1),
                             Equipment(capacity=125, character_id=2),
                             Equipment(capacity=450, character_id=3)])
    for name, weight, value, equipment_id in zip(["Apple", "Potato", "Watermelon", 'Onion'],
                                                 [3, 2, 8, 2], [5, 3, 12, 5], [1, 1, 2, 3]):
        dbtool.insert_row(Item(name=name, weight=weight, value=value, equipment_id=equipment_id))


def get_player():
    return dbtool.get_one_row(table_name=Character, first_to_eq=Character.id, second_to_eq=1)


try:
    dbtool = DbTool()
    insert_initial_data()
    player = get_player()
    world_map = WorldMap()


finally:
    DbTool().finish()
