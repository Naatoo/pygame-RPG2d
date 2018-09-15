import json

from src.tools.global_paths import FIELD_CONTAINERS_DATA_FILE
from collections import OrderedDict


with open(FIELD_CONTAINERS_DATA_FILE, "a") as data:
    row_data = []
    for x in range(1, 11):
        for y in range(1, 11):
            row_data.append(OrderedDict(x=x, y=y, container_type_id=2))
            row_data.append(OrderedDict(x=-x, y=y, container_type_id=2))
            row_data.append(OrderedDict(x=x, y=-y, container_type_id=2))
            row_data.append(OrderedDict(x=-x, y=-y, container_type_id=2))
    table = {"Container": row_data}
    data.write(json.dumps(table))
