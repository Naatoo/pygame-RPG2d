import json

from tools.global_paths import FIELD_CONTAINERS_DATA_FILE
from collections import OrderedDict


with open(FIELD_CONTAINERS_DATA_FILE, "a") as data:
    row_data = [(OrderedDict(id_container=field_id, container_type_id=2, container_field_id=field_id)) for field_id in range(1, 401)]
    table = {"Container": row_data}
    data.write(json.dumps(table))
