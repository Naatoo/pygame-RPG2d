import json

from src.tools.globals.global_paths import FIELD_CONTAINERS_DATA_FILE
from collections import OrderedDict


with open(FIELD_CONTAINERS_DATA_FILE, "a") as data:
    row_data = [OrderedDict(x=x, y=y, container_type_id=2) for x in range(20) for y in range(20)]
    table = {"Container": row_data}
    data.write(json.dumps(table))
