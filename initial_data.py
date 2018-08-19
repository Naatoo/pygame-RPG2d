from dbtools import DbTool
from game_objects import Field, Character, Equipment, Item
from map_creation import GenerateWeather, GenerateBiomes


def insert_initial_data():
    insert_fields()
    insert_characters()
    insert_equipments()
    insert_items()


def insert_fields():
    for biome, weather in zip(list(GenerateBiomes()), GenerateWeather().data):
        DbTool().insert_row(Field(biome=biome, weather=weather))


def insert_characters():
    DbTool().insert_many_rows([Character(name="Player1", field_id=25),
                              Character(name="Player2", field_id=78),
                              Character(name="Player3", field_id=145)])


def insert_equipments():
    DbTool().insert_many_rows([Equipment(capacity=250, character_id=1),
                              Equipment(capacity=125, character_id=2),
                              Equipment(capacity=450, character_id=3)])


def insert_items():
    for name, weight, value, equipment_id in zip(["Apple", "Potato", "Watermelon", 'Onion'],
                                                 [3, 2, 8, 2], [5, 3, 12, 5], [1, 1, 2, 3]):
        DbTool().insert_row(Item(name=name, weight=weight, value=value, equipment_id=equipment_id))



