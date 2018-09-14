import json

from random import choice
from tools.global_paths import MAP_DATA_FILE
from collections import OrderedDict


class GenerateFields:

    def __init__(self):
        self.types = {}
        self.cities()
        self.mountains()
        self.plains()

    def cities(self):
        for _ in range(3):
            self.types[choice(range(1, 401))] = 4

    def mountains(self):
        for _ in range(3):
            index = choice(range(1, 370))
            [self.types.update({x: 3}) for x in range(index, index + 20)]

    def plains(self):
        for index in range(1, 401):
            if index not in self.types.keys():
                self.types[index] = 1


with open(MAP_DATA_FILE, "a") as data:
    fields = GenerateFields().types
    row_data = []
    for index, field_type in fields.items():
        row_data.append(OrderedDict(id=index, type_id=field_type))
    table = {"Field": row_data}
    data.write(json.dumps(table))

