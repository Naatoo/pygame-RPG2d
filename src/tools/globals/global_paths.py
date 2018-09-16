import os

from pathlib import Path


MAIN_DIR = str(Path(__file__).parent.parent.parent.parent)
SRC_DIR = os.path.join(MAIN_DIR, "src/")
RESOURCES_DIR = os.path.join(SRC_DIR, "resources/")
DATA_DIR = os.path.join(RESOURCES_DIR, "data/")

CONTAINERS_DATA_DIR = os.path.join(DATA_DIR, "containers/")
CONTAINERS_SLOTS_DATA_FILE = os.path.join(CONTAINERS_DATA_DIR, "containers_slots_data.json")

CREATURES_DATA_DIR = os.path.join(DATA_DIR, "creatures/")
CREATURES_DATA_FILE = os.path.join(CREATURES_DATA_DIR, "creatures_data.json")

ITEMS_DATA_DIR = os.path.join(DATA_DIR, "items/")
ITEMS_DATA_FILE = os.path.join(ITEMS_DATA_DIR, "items_data.json")

MAP_DATA_DIR = os.path.join(DATA_DIR, "map/")
FIELDS_DATA_FILE = os.path.join(MAP_DATA_DIR, "field_data.json")
FIELDS_TYPE_DATA_FILE = os.path.join(MAP_DATA_DIR, "field_type_data.json")
