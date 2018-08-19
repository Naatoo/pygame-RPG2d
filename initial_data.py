from dbtools import DbTool
from game_objects import Field, Character, BoundedItem, Item
from map_creation import GenerateWeather, GenerateBiomes


def insert_initial_data():
    insert_fields()
    insert_characters()
    insert_bounded_items()
    insert_items()


def insert_fields():
    for biome, weather in zip(list(GenerateBiomes()), GenerateWeather().data):
        DbTool().insert_row(Field(biome=biome, weather=weather))


def insert_characters():
    DbTool().insert_many_rows([Character(name="Player1", field_id=25),
                              Character(name="Player2", field_id=78),
                              Character(name="Player3", field_id=145)])


def insert_items():
    for name, weight, value in zip(["Apple", "Potato", "Watermelon", 'Onion'], [3, 2, 8, 2], [5, 3, 12, 5]):
        DbTool().insert_row(Item(name=name, weight=weight, value=value))


def insert_bounded_items():
    DbTool().insert_many_rows([BoundedItem(item_id=1, quantity=2, character_id=1),
                               BoundedItem(item_id=2, quantity=13, character_id=1),
                               BoundedItem(item_id=4, quantity=23, character_id=1),
                               BoundedItem(item_id=3, quantity=1, character_id=2),
                               BoundedItem(item_id=2, quantity=5, character_id=2)])
