import json
from collections import OrderedDict

from database.dbtools import DbTool
from game.objects.db_objects import FieldType, Field, CreatureGroup, CreatureType, SpawnedCreature, BoundedItem, Item
from tools.global_paths import MAP_DATA_FILE, CREATURES_DATA_FILE, ITEMS_DATA_FILE


obj_file_dict = {
    MAP_DATA_FILE: OrderedDict(FieldType=FieldType, Field=Field),
    CREATURES_DATA_FILE:
        OrderedDict(CreatureGroup=CreatureGroup, CreatureType=CreatureType, SpawnedCreature=SpawnedCreature),
    ITEMS_DATA_FILE: OrderedDict(Item=Item, BoundedItem=BoundedItem)}


def load_initial_data():
    for file_path, table_group in obj_file_dict.items():
        with open(file_path) as f:
            json_data = json.loads(f.read())
            insert_to_database(json_data, table_group)


def insert_to_database(json_data, obj_dict):
    for table_name in obj_dict.keys():
        for row in json_data[table_name]:
            DbTool().insert_row(obj_dict[table_name](**row))
