import json

from src.tools.globals.global_paths import FIELDS_DATA_FILE
from collections import OrderedDict


with open(FIELDS_DATA_FILE, "a") as data:
    row_data = [OrderedDict(x=x, y=y, field_type_id=1) for y in range(100) for x in range(100)]
    table = {"Field": row_data}
    data.write(json.dumps(table))
