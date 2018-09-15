import json

from src.tools.globals.global_paths import CONTAINERS_SLOTS_DATA_FILE
from collections import OrderedDict


with open(CONTAINERS_SLOTS_DATA_FILE, "a") as data:
    x_offset = 14
    y_offset = 262
    row_data = []
    for x in range(8):
        for y in range(4):
            row_data.append(OrderedDict(pixels_x=x * 32 + x_offset, pixels_y=y * 31 + y_offset, container_id=0))
    table = {"ContainerSlot": row_data}
    data.write(json.dumps(table))
