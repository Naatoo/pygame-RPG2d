import json

from src.tools.global_paths import FIELDS_DATA_FILE
from collections import OrderedDict


with open(FIELDS_DATA_FILE, "a") as data:
    row_data = []
    for x in range(1, 11):
        for y in range(1, 11):
            row_data.append(OrderedDict(x=x, y=y, field_type_id=1))
            row_data.append(OrderedDict(x=-x, y=y, field_type_id=1))
            row_data.append(OrderedDict(x=x, y=-y, field_type_id=1))
            row_data.append(OrderedDict(x=-x, y=-y, field_type_id=1))
    table = {"Field": row_data}
    data.write(json.dumps(table))

